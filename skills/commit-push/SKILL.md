---
name: commit-push
description: Commit local changes as small independent-intent commits and push only when the user explicitly asked to push. Use for requests to commit, save work in Git, or push. Preserve unrelated work and never infer external publication from commit authorization.
---

# Commit and Push

Create a reviewable Git history without absorbing unrelated work.

## Inspect

Before staging, inspect:

- `git status --short --branch`
- staged, unstaged, and relevant untracked content;
- recent commit style and the current branch/upstream;
- repository, worktree, and submodule boundaries.

Stop on unresolved conflicts or detached HEAD and report the condition. Treat
pre-staged files as user intent to inspect, not permission to mix them into an
unrelated commit.

## Plan atomic commits

Split by independent intent: each commit should be understandable, reviewable,
revertible, and bisectable on its own. A repository boundary, frontend/backend,
package, module, submodule, or file is a container, not automatically a commit.
Split hunks when one file contains independent changes.

Keep changes together when separating them would produce broken behavior,
misleading history, or an incomplete migration. A single narrow logical change
may remain one commit.

Use one-line English Conventional Commit messages without scopes, bodies,
footers, or co-author lines:

`type: concise imperative description`

Use `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, or `style`
according to the change.

## Commit safely

For each unit:

1. stage explicit files or hunks; never use `git add .` or `git add -A`;
2. inspect `git diff --cached`;
3. commit only the planned unit;
4. re-check `git status --short`.

Do not include secrets, build output, logs, dependency directories, or
unrelated changes. Include relevant untracked source files only after reading
them.

## Publication boundary

- If the user asked only to commit or save locally, stop after commits.
- Push only when the user explicitly asked to push or publish.
- Before pushing, report the destination branch and remote. On `main` or
  `master`, require explicit push authorization in the current request.
- Use `git push` for an existing upstream or `git push -u origin HEAD` when
  the requested branch has no upstream.

Report the commits created, remaining worktree changes, and whether anything
was pushed.
