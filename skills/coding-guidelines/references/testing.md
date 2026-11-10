# Proportional testing

Use the smallest test strategy that can distinguish the requested behavior from
a plausible defect.

## Choose the testing mode

- **Reproducible bug:** add or identify a regression test, observe the expected
  failure, implement the fix, then observe it pass.
- **Important new rule or behavior:** prefer test-first development in small
  red-green steps. Test observable behavior, not incidental implementation.
- **Explicit TDD request:** work test-first unless a genuine blocker makes the
  red step impossible; explain that blocker briefly and preserve equivalent
  evidence.
- **Refactor:** establish existing or characterization coverage before and after
  the change. Do not create an artificial red test when behavior must remain
  unchanged.
- **Docs, mechanical configuration, generated files, or purely visual work:**
  use the relevant parser, build, render, smoke check, or inspection. Do not add
  artificial unit tests.
- **Implementation already exists:** preserve valid work. Add the missing
  verification instead of deleting code merely because the test was written
  later.

## Red-green discipline

1. Express the behavior or regression with a focused test.
2. Run it and confirm it fails for the expected reason, not due to setup noise.
3. Make the minimum coherent implementation change.
4. Run the focused test, then the smallest broader project-native gate justified
   by the affected surface.
5. Stop when acceptance criteria and material risks are covered.

Prefer real behavior. Mock external boundaries when isolation, determinism,
cost, or safety requires it. Assertions about calls, order, or arguments are
appropriate when that interaction is itself the contract.

Never weaken a valid requirement merely to make a test green. A test may be
corrected when repository evidence, the accepted requirement, or observed
behavior shows that the test is wrong; state the evidence and keep the intended
coverage. Do not require user confirmation for an ordinary evidence-backed test
correction that stays within the authorized implementation.

Mutation testing is optional. Use it only when explicitly requested, required by
the project, or included in an approved high-risk validation plan.

## Attribution

This guidance adapts ideas from the `test-driven-development` skill in
Superpowers 6.3.0 by Jesse Vincent. The source is MIT licensed; see
[superpowers-mit-license.txt](superpowers-mit-license.txt).
