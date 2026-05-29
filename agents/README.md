# Agent Configuration

Shared configuration for coding agents.

## Layout

- `skills/` is the single source of truth for reusable agent skills.
- `agents/` contains custom agent definitions.
- `settings/claude/` contains Claude Code-specific settings and scripts.

Tool-specific settings belong under `settings/<tool>/`, but shared skills stay in
`skills/` so Claude, Cursor, and future agents can use the same source.

## Installed Links

`script/setup` links:

- `agents/skills` -> `~/.claude/skills`
- `agents/agents` -> `~/.claude/agents`
- `agents/settings/claude/settings.json` -> `~/.claude/settings.json`
- `agents/settings/claude/statusline.sh` -> `~/.claude/statusline.sh`
