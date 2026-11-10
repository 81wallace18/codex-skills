#!/usr/bin/env python3
"""Structural checks for an in-scope formal tasks.md.

Checks that a task breakdown exists, every parsed task declares Tests and Gate,
and dependencies reference known tasks without self-dependencies. If a diagram
is present and parseable, its task edges must agree with Depends on fields.

Tasks may span multiple files. Diagrams, phase plans, coverage matrices, and
separate gate tables are optional. This script validates Markdown structure; it
does not prove plan adequacy, execute tests, or establish completion.

Usage:
  python3 validate_tasks.py [target] [--root DIR] [--strict]

Exit codes: 0 valid, 1 invalid (or warnings under --strict), 2 usage/target error.
"""

import argparse
import os
import re
import sys

TASK_RE = re.compile(r"^#{2,4}\s+(T\d+)\s*:", re.IGNORECASE)
EDGE_RE = re.compile(r"\bT\d+\b", re.IGNORECASE)


def _autodetect(root):
    base = os.path.join(root, ".specs", "features")
    if not os.path.isdir(base):
        return None
    paths = [
        os.path.join(base, name, "tasks.md")
        for name in sorted(os.listdir(base))
        if os.path.isfile(os.path.join(base, name, "tasks.md"))
    ]
    if len(paths) == 1:
        return paths[0]
    if len(paths) > 1:
        raise SystemExit(
            "validate_tasks: multiple task files found; pass one explicitly:\n  "
            + "\n  ".join(paths)
        )
    return None


def resolve_tasks(target, root):
    if not target:
        return _autodetect(root)
    if os.path.isfile(target):
        return target
    if os.path.isdir(target):
        direct = os.path.join(target, "tasks.md")
        return direct if os.path.isfile(direct) else _autodetect(target)
    candidate = os.path.join(root, ".specs", "features", target, "tasks.md")
    return candidate if os.path.isfile(candidate) else None


def parse_tasks(lines):
    tasks = {}
    current = None
    for line in lines:
        match = TASK_RE.match(line.strip())
        if match:
            current = match.group(1).upper()
            tasks[current] = {"deps": set(), "tests": None, "gate": None}
            continue
        if current is None:
            continue
        stripped = line.strip()
        dep = re.match(r"^-?\s*\*{0,2}Depends on\*{0,2}\s*:\s*(.*)$", stripped, re.IGNORECASE)
        if dep:
            body = dep.group(1)
            if "none" not in body.lower():
                tasks[current]["deps"].update(x.upper() for x in EDGE_RE.findall(body))
        tests = re.match(r"^-?\s*\*{0,2}Tests\*{0,2}\s*:\s*(.*)$", stripped, re.IGNORECASE)
        if tests:
            tasks[current]["tests"] = tests.group(1).strip()
        gate = re.match(r"^-?\s*\*{0,2}Gate\*{0,2}\s*:\s*(.*)$", stripped, re.IGNORECASE)
        if gate:
            tasks[current]["gate"] = gate.group(1).strip()
    return tasks


def parse_diagram_edges(lines):
    edges = set()
    in_fence = False
    saw_arrow = False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            continue
        normalized = line.replace("→", "->")
        if "->" not in normalized:
            continue
        parts = normalized.split("->")
        sequence = []
        for part in parts:
            ids = EDGE_RE.findall(part.upper())
            sequence.append(ids[-1].upper() if ids else None)
        for source, target in zip(sequence, sequence[1:]):
            if source and target:
                edges.add((source, target))
                saw_arrow = True
    return edges, saw_arrow


def check(tasks_path):
    with open(tasks_path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    errors = []
    warnings = []

    has_breakdown = any(
        re.match(r"^#{1,4}\s+Task Breakdown\b", line.strip(), re.IGNORECASE)
        for line in lines
    )
    if not has_breakdown:
        errors.append("missing required section: ## Task Breakdown")

    tasks = parse_tasks(lines)
    if not tasks:
        errors.append("no tasks (### T1: ...) parsed")
        return errors, warnings

    for task_id, task in tasks.items():
        if not task["tests"]:
            errors.append(f"{task_id}: missing or empty `Tests` field")
        elif task["tests"].lower().startswith("none"):
            warnings.append(f"{task_id}: Tests: none - ensure Gate names the appropriate non-test check")
        if not task["gate"]:
            errors.append(f"{task_id}: missing or empty `Gate` field")
        for dep in sorted(task["deps"]):
            if dep == task_id:
                errors.append(f"{task_id}: self-dependency is not allowed")
            elif dep not in tasks:
                errors.append(f"{task_id}: dependency {dep} does not name a known task")

    diagram_edges, has_diagram = parse_diagram_edges(lines)
    if has_diagram:
        dependency_edges = {
            (dep, task_id)
            for task_id, task in tasks.items()
            for dep in task["deps"]
            if dep in tasks and dep != task_id
        }
        for source, target in sorted(diagram_edges - dependency_edges):
            if source in tasks and target in tasks:
                errors.append(f"diagram shows {source} -> {target} without matching Depends on")
        for source, target in sorted(dependency_edges - diagram_edges):
            errors.append(f"{target} depends on {source}, but the diagram omits that edge")

    return errors, warnings


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="validate_tasks.py",
        description="Structural checker for an in-scope formal tasks.md.",
    )
    parser.add_argument("target", nargs="?", default=None)
    parser.add_argument("--root", default=".")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)

    try:
        tasks_path = resolve_tasks(args.target, args.root)
    except SystemExit as exc:
        print(exc, file=sys.stderr)
        return 2
    if not tasks_path:
        print("validate_tasks: could not locate a tasks.md; pass one explicitly", file=sys.stderr)
        return 2

    errors, warnings = check(tasks_path)
    for warning in warnings:
        print(f"  WARN  {warning}")
    for error in errors:
        print(f"  ERROR {error}")
    failed = bool(errors or (args.strict and warnings))
    print(f"\nvalidate_tasks: {len(errors)} error(s), {len(warnings)} warning(s) in {tasks_path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
