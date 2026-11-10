# Optional project lessons

Use project lessons only when the repository already treats them as canonical
or the user explicitly asks to create or update them. Reading this skill does
not authorize new `.specs/lessons.json` or `.specs/LESSONS.md` files.

When applicable:

1. Load only relevant confirmed lessons.
2. Record a new lesson only from concrete project evidence such as a repeated
   regression, acceptance gap, or failed gate.
3. Phrase it as a terse, reusable, project-local rule and cite the source.
4. Use `scripts/lessons.py` for repositories that adopted its store; do not
   hand-edit generated state.
5. Keep candidates distinct from confirmed guidance and avoid methodology
   opinions that belong in the skill itself.

A clean validation produces no lesson. Do not write lessons automatically after
every feature, and do not delete lesson files as a way to toggle behavior.
