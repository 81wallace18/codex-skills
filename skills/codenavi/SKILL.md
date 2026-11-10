---
name: codenavi
description: Navigate and investigate an unfamiliar or poorly documented codebase by tracing the relevant flow and reporting source-grounded findings. Use when repository orientation is genuinely needed; do not use as a mandatory wrapper for familiar edits, greenfield work, CI/CD, or infrastructure provisioning.
license: CC-BY-4.0
metadata:
  author: Felipe Rodrigues - github.com/felipfr
  version: '1.1.0-local'
---

# CodeNavi

Build just enough understanding of unfamiliar code to answer or implement the
requested task without collateral changes.

## Investigate

1. Read local instructions and existing canonical documentation relevant to the
   request, including `.notebook/INDEX.md` when it already exists.
2. Start at the nearest observable entry point and trace only the imports,
   calls, data paths, contracts, tests, and configuration needed to explain the
   behavior.
3. Distinguish facts supported by source from hypotheses and unresolved
   uncertainty. Verify mutable framework or API behavior in current primary
   documentation when it affects the result.
4. Preserve the user's scope and existing worktree. Analysis and diagnosis do
   not authorize edits.

For implementation, reuse an already approved plan when one exists. Otherwise
state a proportional approach and proceed when the user's request already
authorizes the work; do not manufacture a second approval ceremony.

## Durable notes

Do not create `.notebook/` automatically. Add or update project knowledge only
when the user requests it or the repository already treats it as a maintained
canonical artifact and the current task authorizes documentation changes.

When notes are appropriate, record expensive-to-rediscover knowledge as
pointers such as `path:function` or `path:line`, not copied source. Do not
duplicate better canonical docs.

## Completion

For an explanation, cite the relevant source locations and remaining
uncertainty. For a change, verify the behavior at the level the repository can
actually prove and report that level accurately; local tests do not prove UAT,
deployment, or production behavior.
