---
name: tlc-spec-driven
description: Plan, implement, resume, or validate work that explicitly needs spec-driven development, formal requirements, or traceability, or that already belongs to an existing project spec. Do not invoke merely because a repository contains .specs or for an ordinary small development task.
license: CC-BY-4.0
metadata:
  author: Felipe Rodrigues - github.com/felipfr
  version: 3.4.0-local
---

# Tech Lead's Club - Spec-Driven Development

Use the least ceremony that preserves the evidence and decisions the work
actually needs. Reuse the repository's existing specification convention; do
not migrate or rewrite valid project artifacts into this skill's preferred
layout.

## Invocation boundary

Use this skill when the user explicitly asks for SDD, a formal specification,
requirements traceability, or work on an existing spec. A nearby `.specs/`
directory alone does not activate it.

Requests to explain code, perform a simple fix, or implement a small,
well-defined change stay in the repository's normal workflow unless the user
chooses SDD.

## Choose the smallest durable shape

- **Small and clear:** keep the objective, acceptance criteria, affected scope,
  and verification inline. Do not create SDD files.
- **Moderate but low-risk:** use a brief spec or the project's existing issue or
  plan. Add design or task files only when they resolve a real decision or
  dependency.
- **Risky or cross-component:** persist requirements, dependencies, decisions,
  and evidence. This normally includes data migration, auth or authorization,
  payments, concurrency, critical external integrations, or changes spanning
  multiple components.
- **Existing formal spec:** update only the artifacts required by that
  convention. Do not scaffold missing optional phases.

Design and task breakdowns are conditional. Their absence is correct when the
phase is not justified.

## Evidence and authorization

1. Derive tests and checks from acceptance criteria, not implementation shape.
2. Distinguish structural validation of Markdown from executed tests and from
   independent review. A `PASS` word or `file:line` citation is evidence
   metadata, not proof that behavior ran.
3. Never claim an independent verifier unless another reviewer actually ran.
4. Do not create commits, dispatch sub-agents, write project lessons, push,
   deploy, or mutate external systems unless the user request or established
   project workflow authorizes that action.
5. Preserve unrelated work and reconcile resumed state with Git and current
   artifacts; live evidence wins over stale handoff text.

## Workflow

1. Establish objective, testable acceptance criteria, scope, assumptions, and
   validation level.
2. Inspect repository conventions and any existing spec before choosing
   artifacts.
3. Resolve ambiguous high-risk behavior before implementation.
4. Add design and dependency-aware tasks only where they reduce execution risk.
5. Implement in coherent slices and run the relevant checks.
6. Record requirement-to-evidence traceability for formal work, clearly
   separating checks run from checks merely described.

## References

Read only what the current phase needs:

- small or moderate implementation without persistent SDD artifacts:
  [lightweight-execution.md](references/lightweight-execution.md); do not also
  read the comprehensive `implement.md` or `validate.md` guides;
- requirements and EARS guidance: [specify.md](references/specify.md);
- ambiguous product behavior: [discuss.md](references/discuss.md);
- architecture decisions: [design.md](references/design.md);
- dependency-aware breakdown: [tasks.md](references/tasks.md);
- formal task-file execution or advanced gate mechanics:
  [implement.md](references/implement.md);
- formal validation report, interactive UAT, or explicitly requested
  discrimination testing: [validate.md](references/validate.md);
- resume or explicit decision recording: [memory.md](references/memory.md);
- optional, authorized lessons: [lessons.md](references/lessons.md);
- optional, authorized delegation: [sub-agents.md](references/sub-agents.md).

The references follow this entrypoint's proportional artifact, authorization,
and evidence rules.

## Deterministic helpers

Run helpers only for artifacts that exist and are in scope:

- `validate_spec.py`: structural checks for a formal `spec.md`;
- `validate_tasks.py`: structural checks for a formal `tasks.md`;
- `check_commit.py`: commit-message validation when commits are authorized;
- `validate_state.py`: structural inspection of a selected formal validation
  report;
- `lessons.py`: project lessons only when writing them is authorized.

No-target discovery is not success evidence. An explicitly named missing
feature must fail.
