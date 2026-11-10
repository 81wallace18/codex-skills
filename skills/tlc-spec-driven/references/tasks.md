# Formal tasks

Create a `tasks.md` only when dependency ordering, traceability, handoff, or
multi-session execution benefits from a durable breakdown. Keep small obvious
work inline.

## Authoring rules

- Each task represents one coherent, independently verifiable outcome.
- A task may span multiple files or layers when those changes are inseparable.
- Split work by independent intent, dependency, risk, or review boundary, not by
  arbitrary file or task-count quotas.
- Name dependencies explicitly. They must reference known tasks and must not be
  self-dependencies.
- Include a `Tests` field describing proportional evidence and a `Gate` field
  naming the repository-native command or direct check.
- Use `Tests: none` only when another check is more appropriate; state that check
  in `Gate`.
- Add phases, diagrams, a coverage matrix, or separate quick/full/build gates
  only when they make a real dependency or assurance relationship clearer.
- Do not ask the user to choose tools that can be derived from the repository.

## Minimal template

```markdown
# <Feature> tasks

## Task Breakdown

### T1: <coherent outcome>
- **Depends on**: none
- **Where**: `path/a`, `path/b`
- **Requirements**: R1, AC-1
- **Tests**: focused regression test for <behavior>
- **Gate**: `<project-native command>`
- **Done when**: <observable result and evidence>

### T2: <next outcome>
- **Depends on**: T1
- **Where**: `path/c`
- **Requirements**: R2, AC-2
- **Tests**: characterization before and after refactor
- **Gate**: `<project-native command>`
- **Done when**: <observable result and evidence>
```

Optional sections may include an execution plan, test coverage matrix, gate
commands, risk notes, or a dependency diagram. Keep them only if useful.

## Structural validation

For a persisted task file, run:

```bash
python3 <skill-dir>/scripts/validate_tasks.py <tasks-path-or-feature>
```

The helper checks task structure, required fields, dependency references, and
diagram parity when a diagram exists. It does not prove design adequacy, test
execution, or completion.
