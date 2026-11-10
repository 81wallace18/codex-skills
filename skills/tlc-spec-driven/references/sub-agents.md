# Optional sub-agent delegation

Delegation is an execution option, not an SDD phase or completion gate.

Use sub-agents only when the user or project workflow already authorizes them
and one of these conditions holds:

- two or more workstreams are genuinely independent and parallel execution is
  useful;
- a bounded specialist investigation can proceed without conflicting writes;
- independent review materially improves assurance for a high-risk change.

Do not trigger delegation from a numeric task threshold. Do not split cohesive
work merely to create workers. Avoid parallel edits to overlapping files or
shared mutable state.

Give each worker a bounded objective, scope, relevant requirements, permitted
actions, and expected evidence. The coordinator remains responsible for
reconciling results with the current worktree and acceptance criteria.

An independent verifier must actually be a separate reviewer. If none ran, say
that validation was an author self-check. Commits, mutations, persisted reports,
and nested delegation remain separately conditional.
