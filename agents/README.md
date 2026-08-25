# Agent Configuration

Shared configuration for coding agents.

## Layout

- `skills/` is the single source of truth for reusable agent skills.
- `agents/` contains custom agent definitions.
- `rules/cursor/mads-preferences.mdc` contains shared, non-coding preferences for Cursor and Codex.
- `rules/cursor/work-boundary.mdc` contains the Cursor-only work-boundary rating.
- `rules/code/` contains the shared instructions used inside `~/Code`.
- `settings/claude/` contains Claude Code-specific settings and scripts.

The global preferences route agents to `~/Code/AGENTS.md` inside code
workspaces. Repository-level instructions add to or override that file.

Tool-specific settings belong under `settings/<tool>/`, but shared skills stay in
`skills/` so Claude, Cursor, and future agents can use the same source.

## Installed Links

`script/setup` links:

- `agents/rules/cursor/*.mdc` -> `~/.cursor/rules/`
- `agents/rules/cursor/mads-preferences.mdc` -> `~/.codex/AGENTS.md`
- `agents/rules/code/{AGENTS,CLAUDE}.md` -> `~/Code/`
- `agents/skills` -> `~/.claude/skills`
- `agents/skills/<name>` -> `~/.agents/skills/<name>` for Codex, excluding the legacy Claude-specific `skill-creator`
- `agents/agents` -> `~/.claude/agents`
- `agents/settings/claude/settings.json` -> `~/.claude/settings.json`
- `agents/settings/claude/statusline.sh` -> `~/.claude/statusline.sh`
