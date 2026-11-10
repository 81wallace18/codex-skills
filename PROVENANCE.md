# Provenance and credits

This repository publishes selected local skill snapshots, not pristine upstream
releases. Original author metadata and existing notices are preserved.
`snapshot.json` identifies the local installation paths and imported-file hashes.
No credentials or machine-wide configuration are part of these references.

## Tech Leads Club sources

Upstream repository: [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills).
The source locations and license notice were checked on November 10, 2026,
against revision `8658b6658c762b9e5efd3956ed35a51c41bdf6c3`.
This is a reference revision, not a claim that the installed files came from
that commit. The original installed revisions are not recorded in the local
installer metadata.

| Imported skill | Upstream location | Attribution and local changes |
| --- | --- | --- |
| `coding-guidelines` | [Original skill](https://github.com/tech-leads-club/agent-skills/tree/8658b6658c762b9e5efd3956ed35a51c41bdf6c3/packages/skills-catalog/skills/%28development%29/coding-guidelines) | Metadata credits `ale` and identifies the source as Karpathy Guidelines. Local changes clarify evidence-backed assumptions, proportional testing, and security-review triggers. The testing reference has separate Superpowers attribution below. |
| `codenavi` | [Original skill](https://github.com/tech-leads-club/agent-skills/tree/8658b6658c762b9e5efd3956ed35a51c41bdf6c3/packages/skills-catalog/skills/%28development%29/codenavi) | Metadata credits Felipe Rodrigues, [felipfr](https://github.com/felipfr), and declares `CC-BY-4.0`. Local version `1.1.0-local` narrows activation, avoids automatic notebook creation, and distinguishes observed evidence from assumptions. |
| `tlc-spec-driven` | [Original skill](https://github.com/tech-leads-club/agent-skills/tree/8658b6658c762b9e5efd3956ed35a51c41bdf6c3/packages/skills-catalog/skills/%28development%29/tlc-spec-driven) | Metadata credits Felipe Rodrigues and declares `CC-BY-4.0`. Local version `3.4.0-local` makes formal artifacts and delegation conditional, clarifies authorization, and distinguishes structural validation from runtime proof. References and Python helpers include local adaptations. |

The upstream repository has mixed licensing: its software source is MIT, while
maintainer-created `SKILL.md` content is CC BY 4.0 unless an individual file
specifies otherwise. Preserve the
[upstream license and boundary notice](LICENSES/tech-leads-club-agent-skills.txt),
the existing per-file declarations, and these source/change credits.
The [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/) is linked
here for the skills that use it. Local adaptation does not erase upstream rights
or imply endorsement by the original authors.

## Proportional testing reference

`skills/coding-guidelines/references/testing.md` credits ideas from the
`test-driven-development` skill in Superpowers 6.3.0, by Jesse Vincent.
See [obra/superpowers](https://github.com/obra/superpowers) and its
[TDD skill](https://github.com/obra/superpowers/tree/main/skills/test-driven-development).
The original installed revision was not recorded. The existing
[MIT notice](skills/coding-guidelines/references/superpowers-mit-license.txt)
is preserved. This is an adapted testing reference, not the full Superpowers
plugin or an unmodified copy of its workflow.

## Microsoft Playwright CLI

Upstream: [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli).
Skill: [skills/playwright-cli](https://github.com/microsoft/playwright-cli/tree/9c95a500e59b354c3e76135e5686f42cedb28391/skills/playwright-cli).

The source location and [Apache 2.0 license](LICENSES/microsoft-playwright-cli.txt)
were checked against revision `9c95a500e59b354c3e76135e5686f42cedb28391` on
November 10, 2026. This reference revision does not establish the installed
version. The installed entrypoint and nine supporting references are copied
without changes in this export. This repository does not bundle the CLI,
browsers, user profiles, or Microsoft services.

## Locally maintained workflows

| Skill | What is established | Source references |
| --- | --- | --- |
| `security-review` | Local installed review workflow. No original third-party repository or license could be established from the exported file; no external authorship is asserted. | The installed `SKILL.md` is the source of this snapshot. |
| `commit-push` | Local installed Git workflow. No original third-party repository or license could be established from the exported file; no external authorship is asserted. | [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) describes the referenced commit convention, not the origin of this skill. |
| `whatsapp-reader` | Locally maintained instructions for the existing WAHA and local media/transcription setup. This is not a WAHA-distributed skill. | [WAHA native MCP](https://waha.devlike.pro/docs/apps/mcp/), [chat operations](https://waha.devlike.pro/docs/how-to/chats/), and [GOWS engine](https://waha.devlike.pro/docs/engines/gows/). These are dependency documentation, not a claim of copied implementation. |

No repository-wide license is assigned to these locally maintained materials by
this publication. Do not infer a reuse license for unattributed material from
the licenses of neighboring third-party files. This export preserves available
provenance; it does not certify complete authorship or legal provenance.
