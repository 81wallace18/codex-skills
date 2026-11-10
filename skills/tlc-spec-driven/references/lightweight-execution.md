# Lightweight execution

Use this path for a clear implementation that does not justify persistent SDD
artifacts.

1. State the objective, acceptance criteria, affected scope, and relevant risk
   inline.
2. Inspect the existing implementation and tests before choosing the change.
3. For persistence, auth, payments, concurrency, or integrations, cover failure
   behavior and authorization ordering explicitly.
4. Implement the smallest coherent change that meets the criteria and preserves
   unrelated work.
5. Add or update tests that assert observable outcomes, including the important
   failure path.
6. Run the narrow relevant test first, then the repository's broader practical
   gate. Report exactly what ran and what remains unproved.

Do not create `.specs/`, commits, documentation, sub-agents, lessons, mutation
tests, or UAT unless the user or repository explicitly requires them. Do not
load the comprehensive `implement.md` or `validate.md` guides for this path.
