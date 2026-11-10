# Codex skills

Seven skills from Wallace's local development workflow, published with their
supporting references, scripts, and available source attribution.

These are snapshots of the installed versions, including local customizations.
They are not an official OpenAI, Microsoft, or Tech Leads Club distribution,
and publishing this repository does not change the active local installation.

## Included skills

| Skill | Purpose | Local snapshot source |
| --- | --- | --- |
| [coding-guidelines](skills/coding-guidelines/SKILL.md) | Focused implementation and proportional testing | `~/.codex/skills/coding-guidelines` |
| [codenavi](skills/codenavi/SKILL.md) | Source-grounded investigation of unfamiliar code | `~/.codex/skills/codenavi` |
| [tlc-spec-driven](skills/tlc-spec-driven/SKILL.md) | Explicit spec-driven work and requirements traceability | `~/.codex/skills/tlc-spec-driven` |
| [security-review](skills/security-review/SKILL.md) | Review a change set for actionable security issues | `~/.codex/skills/security-review` |
| [playwright-cli](skills/playwright-cli/SKILL.md) | Browser automation through Playwright CLI | `~/.agents/skills/playwright-cli` |
| [commit-push](skills/commit-push/SKILL.md) | Atomic commits and explicitly authorized publication | `~/.codex/skills/commit-push` |
| [whatsapp-reader](skills/whatsapp-reader/SKILL.md) | Bounded WhatsApp reading, media downloads, and transcription | `~/.codex/skills/whatsapp-reader` |

Each directory preserves its installed `references/`, `scripts/`, and `agents/`
files when present. See [provenance and credits](PROVENANCE.md) for upstream
links, customization notes, and licensing boundaries. The
[snapshot manifest](snapshot.json) records SHA-256 hashes for the 39 imported
files; it excludes repository documentation and the separately retrieved
upstream license notices, as well as the local license files added after the
initial snapshot.

## Use a skill

Inspect the selected skill and its dependencies before installing it. For Codex,
copy the complete selected directory into your user skill directory, commonly
`~/.agents/skills/`. Check for an existing installation first; do not overwrite
an existing skill or install the same name in multiple discovery locations.
Use the skill location supported by your client and version.

For example, from the repository root, when the destination does not exist:

```bash
mkdir -p ~/.agents/skills
test ! -e ~/.agents/skills/codenavi && \
  cp -R skills/codenavi ~/.agents/skills/codenavi
```

Invoke an installed skill explicitly with its name, such as `$codenavi`.
Automatic selection depends on the client and the skill's invocation policy.
See [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills).

This repository does not install software, configure MCP servers, create
accounts, grant permissions, or automatically update your skills.

## External dependencies and limitations

- `playwright-cli` requires the separate
  [Microsoft Playwright CLI](https://github.com/microsoft/playwright-cli) and a
  supported browser. Browser profiles, cookies, traces, and screenshots are not
  included.
- `whatsapp-reader` expects a separately configured, read-only `waha-native` MCP,
  a local `whatsapp-reader` MCP for media/audio, and the session name `personal`.
  Its transcription instructions expect a local ASR service with
  `parakeet-npu` and `whisper-medium-npu`. Those services, MCP source code,
  configuration, credentials, session data, and model files are not included.
  Copying the skill alone does not provide a working WhatsApp integration.
- `tlc-spec-driven/scripts/` requires Python 3. Its validators inspect artifact
  structure; passing them does not prove runtime correctness, security, an
  independent review, UAT, or deployment. `lessons.py` has state-writing
  commands; invoke them only for an authorized project.
- Instructions are not a sandbox. A skill cannot enforce access control,
  prevent all unsafe actions, or replace the client's permission system.

## Publication scope

Only the seven listed skills are included. The WhatsApp sender, memory-derived
procedures, other installed skills, Codex configuration, histories, messages,
media, secrets, installer metadata, and generated caches are excluded.

Imported skill files are preserved byte-for-byte. Export-added license files do
not change their instructions or runtime behavior.

## Licensing

The following locally maintained skill packages are MIT licensed, with
`Copyright (c) 2026 Wallace Patrick`:

- [security-review](skills/security-review/LICENSE)
- [commit-push](skills/commit-push/LICENSE)
- [whatsapp-reader](skills/whatsapp-reader/LICENSE)

Each license is included inside its skill directory so it travels with a copied
installation. The WhatsApp license covers this skill's instructions and UI
metadata, not WAHA, MCP implementations, ASR models, or other dependencies.

There is no single blanket license for this mixed-origin collection. The other
skills retain their upstream licenses and credits. Follow the per-source terms
in [PROVENANCE.md](PROVENANCE.md); the MIT grants above do not relicense
third-party material.
