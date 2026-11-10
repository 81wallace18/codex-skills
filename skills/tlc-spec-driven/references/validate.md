# Validate formal work

Validation should prove accepted behavior at the level the task requires. It is
not a reason to add every available ceremony.

## Core pass

1. Re-read the accepted requirements and current diff or implementation.
2. Map each in-scope acceptance criterion to concrete evidence: a focused test,
   integration check, build, inspection, or observed runtime result.
3. Run project-native checks proportional to the changed surface and risk.
4. Inspect edge cases, regression exposure, documentation drift, and material
   trust-boundary changes.
5. Report PASS only for criteria supported by evidence. Mark gaps, failures, and
   unexecuted checks plainly.

Local tests do not establish UAT, deployment, real-provider behavior, or
production state. Structural validators prove only artifact shape.

## Additional assurance

Use these only when requested, required by the project, or included in an
approved risk-based plan:

- an independent verifier or separate reviewer;
- mutation or fault-injection testing;
- a persisted `.specs/features/<feature>/validation.md` report;
- interactive browser/device UAT;
- full compliance or repository-wide security audit;
- project lesson distillation.

An automatic security review is appropriate when the implementation materially
changes a trust boundary, but keep it scoped to the relevant diff.

## Optional report template

```markdown
# Validation: <feature> - PASS | FAIL

## Scope
- Requirements:
- Diff or implementation boundary:
- Evidence level:

## Acceptance evidence
| Criterion | Evidence executed | Result | Limitation |
| --- | --- | --- | --- |

## Checks
- `<command>` -> exit <code>

## Remaining gaps
- none | <gap and next action>
```

If this report exists, `validate_state.py` may check its structure. A structural
PASS is not independent or runtime proof.
