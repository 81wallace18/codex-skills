---
name: security-review
description: Review the actual current change set for high-confidence exploitable security issues. Use when the user requests a security review, or when an implementation materially changes authentication, authorization, tenant isolation, command execution, uploads, secrets, sensitive data, or another trust boundary. Keep automatic reviews diff-scoped; this is not a generic ceremony or formal compliance audit.
---

# Security Review

Review the change that actually exists and return actionable findings grounded
in repository evidence.

## Establish scope

1. Read repository instructions and identify the current branch and worktree.
2. Resolve the comparison base from the repository or PR context. Prefer the
   actual target branch and merge-base; do not assume `origin/HEAD`.
3. Include every requested local surface:
   - committed branch diff from the resolved merge-base;
   - staged changes;
   - unstaged changes;
   - relevant untracked files.
4. For an automatic implementation-time review, inspect only the relevant
   changed surface and directly connected trust boundary. Do not expand it into
   a repository-wide audit.
5. Record the exact refs and commands used. If the base is ambiguous, say so and
   review the known local changes without pretending they represent a PR.

## Analyze exploit paths

Trace changed data from an attacker-controlled or less-trusted source to a
security-relevant effect. Check the categories supported by the diff, including:

- authentication, authorization, tenant or object boundaries;
- injection, unsafe parsing, deserialization, filesystem and command execution;
- secrets, cryptography, sensitive data exposure, logging, and transport;
- browser security, CSRF, XSS, redirects, SSRF, CORS, and uploads;
- dependency or build-chain trust;
- races, replay, state transitions, payment or business-logic abuse;
- availability and resource exhaustion when an attacker can trigger meaningful
  impact;
- unsafe Rust or FFI where memory-safety assumptions are crossed;
- shell, environment, CI, agent instructions, and prompts when their inputs can
  cross a trust boundary or cause tool/action manipulation.

Tests, docs, regexes, prompts, shell scripts, environment variables, and
availability issues are not automatically findings and are not automatically
excluded. Evaluate the concrete trust boundary and exploitability.

## Findings

Report only findings with a plausible attack path and concrete evidence. For
each finding include:

- severity and confidence;
- affected file and line;
- attacker-controlled source, vulnerable behavior, and impact;
- a practical remediation and relevant test.

Separate confirmed findings from questions or defense-in-depth suggestions.
State when no high-confidence finding was found and list material areas that
were outside the reviewed diff. Never claim an independent review unless a
separate reviewer actually performed it.
