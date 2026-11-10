# Coding principles

Use these as judgment, not as a checklist.

## Before coding

- Inspect the relevant code, project instructions, tests, and current worktree.
- Resolve discoverable technical facts yourself.
- State assumptions that affect behavior or risk. Choose a safe reversible
  technical default when evidence supports it.
- Ask only when a missing product, scope, or authority decision would materially
  change the outcome.
- Prefer the simplest implementation that satisfies the accepted requirements.

## During implementation

- Keep changes traceable to the requested outcome; preserve unrelated work.
- Match repository conventions and avoid speculative abstraction.
- Work in coherent slices. A slice may span several files when they form one
  inseparable behavior.
- Apply the proportional testing guidance from `coding-guidelines`. Bugs should
  normally get a regression test; important new behavior should normally use
  test-first steps; refactors need before-and-after evidence.
- Never weaken an accepted requirement just to make a test pass. Correct a test
  when evidence shows the expectation is wrong, while preserving the intended
  coverage and explaining the evidence.
- Do not delete valid pre-existing tests or code merely because test-first order
  was not followed.

## After implementation

- Run the smallest project-native checks that cover the changed behavior and
  material risks.
- Distinguish checks actually run from checks described, and local evidence from
  UAT, deployment, provider, or production proof.
- Stop when acceptance criteria have sufficient evidence. Additional reviewers,
  mutation tests, reports, commits, and UAT are conditional, not automatic.

## Writing

Lead with the result. Use direct language, short sentences, and only the detail
needed to support a decision or evidence claim.
