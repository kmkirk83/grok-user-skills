# Grok User Skills Suite

[![Validate Skills](https://github.com/kmkirk83/grok-user-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/kmkirk83/grok-user-skills/actions/workflows/validate-skills.yml)

A collection of specialized skills designed to maximize **autonomy**, **thoroughness**, and **effectiveness** when working with Grok.

## Included Skills

| Skill | Purpose |
|-------|---------|
| **project-autonomy-bootstrap** | Unified entry point for starting chats/projects with the full high-effort workflow |
| **task-decomposition-verifier** | Hierarchical decomposition + multi-stage verification + adversarial critique |
| **skill-gap-analyzer** | Detect capability gaps and recommend/create new skills |
| **agent-eval-improver** | Score agent outputs and generate concrete improvement proposals |
| **autonomous-research-synthesizer** | Long-horizon multi-source research with quality scoring and synthesis |
| **realtime-agent-orchestra** | Setup of realtime multi-agent systems (LangGraph, CrewAI, voice, browser, etc.) |
| **background-completion-swarm** | Fully autonomous finishing of unfinished work across codebases |
| **vibe-coding-maximizer** | Elite practices for production-quality vibe coding and promoting AI products |

## Installation

Copy the desired skill directories into your Grok user skills folder (typically `~/.grok/skills/` or the platform-equivalent path).

```bash
git clone https://github.com/kmkirk83/grok-user-skills.git
cp -r grok-user-skills/<skill-name> ~/.grok/skills/
```

## Local Validation

The same checks that run in CI can be executed locally:

```bash
pip install pyyaml
python .github/scripts/validate_skills.py
```

## Continuous Integration

- **Validate Skills** workflow runs on every pull request and push to `main` that touches `SKILL.md` files.
- It enforces skill-creator rules (kebab-case name, description constraints, directory/name match, no placeholder TODOs, valid frontmatter).
- Results appear as annotations and in the job summary.

## Contributing

1. Follow the skill-creator conventions for any new or updated `SKILL.md`.
2. Ensure the directory name exactly matches the `name` field in frontmatter.
3. Run the local validation script before opening a PR.
4. Keep descriptions free of `: ` (colon-space) and angle brackets.

## License

These skills are provided for personal and collaborative use with Grok. Adapt as needed.
