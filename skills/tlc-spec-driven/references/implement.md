# Implement a formal spec

Use this reference only when a persisted spec or formal task file is already in
scope. For a small clear implementation, use `lightweight-execution.md`.

## Establish the slice

1. Read the accepted requirements, relevant design decisions, current task, and
   repository instructions.
2. Reconcile them with the current Git/worktree state. Preserve valid work that
   already exists.
3. Identify the behavior, affected files, dependencies, risk, and evidence that
   will make the slice complete.
4. Resolve discoverable technical questions from the repository. Ask only for a
   missing decision that materially changes product behavior, scope, or
   authority.

A task is a coherent outcome, not a file quota. It may change multiple files
when implementation, tests, contracts, and documentation are inseparable.

## Execute

1. Use proportional TDD:
   - bug: reproduce with a failing regression test when feasible;
   - important new behavior: prefer a focused red-green step;
   - refactor: establish characterization or existing coverage before and after;
   - non-behavioral work: use the relevant structural, build, render, or smoke
     check instead of an artificial test.
2. Implement the minimum coherent change.
3. Run the task's focused check, then the smallest broader gate justified by the
   affected surface.
4. Review the diff for scope, regressions, documentation impact, and material
   trust-boundary changes.
5. Record task status and requirement evidence when the project's formal
   convention requires it.

If an existing test conflicts with accepted requirements or current canonical
behavior, investigate. Correct the test when evidence shows it is wrong; never
weaken the intended requirement merely to obtain green output.

## Conditional mechanisms

- **Sub-agents:** use only when already authorized and independent work or review
  has clear value. There is no task-count trigger.
- **Independent verification:** use when requested, project-required, or part of
  the approved validation plan. Never claim it otherwise.
- **Mutation testing:** use only when requested, project-required, or justified
  by an approved high-risk plan.
- **Interactive UAT:** run only when access and authorization exist and the
  acceptance criteria require user-facing runtime proof.
- **Commits and push:** follow `commit-push`; task boundaries do not create
  implicit commit or publication authorization.
- **Lessons and validation reports:** persist only when the project convention or
  approved plan requires them.

## Completion

Report what changed, checks actually executed and their results, acceptance
criteria covered, documentation/security impact, and any material limitation.
Do not inflate structural Markdown validation into behavioral proof.
