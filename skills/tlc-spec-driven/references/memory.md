# Optional SDD state and resume

Use `.specs/STATE.md` only when the project already adopted it or explicitly
requests a durable handoff. Do not create it merely because this skill was read.

## Minimal shape

```markdown
# STATE

## Decisions
### AD-001
- **Decision**: <durable project-level decision>
- **Reason**: <why>
- **Trade-off**: <cost accepted>
- **Scope**: <affected areas>
- **Status**: active

## Handoff
- **Feature**: <name/path>
- **Current slice**: <task or outcome>
- **Completed**: <evidence-backed items>
- **Next step**: <one concrete action>
- **Blockers**: none | <description>
- **Uncommitted files**: <paths or none>
- **Branch**: <branch>
```

Record only hard-to-reverse, cross-feature decisions that would be surprising
without context. Feature-local decisions stay with the feature design.

## Resume

Treat handoff text as a hypothesis. Before editing, reconcile it with the current
branch, worktree, recent changes, task state, and available gate evidence. Live
state wins. Preserve unexplained local work and ask only when ownership or safe
intent cannot be resolved.

Update a handoff when work is genuinely pausing and the project benefits from a
durable resume point. Do not force commits or stashes; use the authorization and
Git workflow already in effect.
