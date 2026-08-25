# Code-wide agent rules

## General

- Keep things simple. Channel "yagni" energy unless told otherwise.
- Typesafety is useful, take advantage of it.
- Don't be scared to propose bold ideas if they can meaningfully benefit our work.
- Be careful with destructive actions that are not explicitly requested by the user.
- Tests are good! Endless smoke tests, "regression tests" for feature deletions, etc, much less good. Tests should be focused, not slop.
- Comments are a great way to clarify functionality and how code is used. Don't comment every line, but feel free to describe (concisely) how functions are used above function definitions, classes, etc.
- Keep comments up to date! When making changes, it's important to keep things in sync.
- Use `knip` to find unused files, dependencies, and exports after changes that may leave dead code, or during targeted cleanup.
- Use the package manager already configured by the repo. If the repo does not clearly specify one, prefer `bun`, then `npm`. Do not switch package managers casually.

## Coding preferences (Typescript focused)

- `any` is the enemy. Inferred types are our friend. Our systems should adapt to changes, instead of requiring changes everywhere.
- If your TS code looks like a Python dev wrote it, it is bad TS code.
- Avoid one-line functions that are just casting wrappers.
- Write TypeScript in ways that Matt Pocock and Mads would be proud of.
- If not already specified in project, I generally like to use the following tech: `Tailwind`, `React`, `Vite`, `Motion`. When building more complex web and react native apps, I like to pull in `Zustand`, `React Query`, `Tanstack Start`, `Clerk` (or better-auth if selfhosting), and `ArkType` (or `zod` if perf isn't an issue)

## UX and visual design work

- Use `ux-flow-plan` before implementation when a user-facing feature's behavior, ownership, or architecture is not yet clear.
- `emil-prototype` is an explicit divergence workflow. Use it when Mads invokes it to explore genuinely different visual or interaction directions before production implementation.
- Standing visual constraints: dark mode, true black (`#000`) background, white primary text, information-dense layouts, minimal copy, no decorative card or pill chrome, no light-gray subtitle lines above sections, and no em dashes.
- Avoid continuously repainting CSS animations such as pulse, shimmer, blur, and spinners; they can peg the GPU on high-refresh displays.
- Do not add subtitles, helper text, or descriptive copy beneath headings, labels, cards, or settings by default. Add supporting copy only when it prevents misunderstanding or error, and never use it to restate the heading.

## Match ceremony to the task

- Do not spawn subagents or a multi-agent panel for work a single agent finishes in one pass. Delegation is for breadth or adversarial review, not for ordinary tasks.
- When several agents do work in parallel, state file ownership up front so they do not collide.

## Blast radius

- Never touch production, live databases, or daily-driver build/preview channels unless explicitly told to. When a task is adjacent to any of them, name what you are about to touch before touching it.

## Pull Requests

- Make sure titles follow conventions from the repo. They should be simple and easy to understand. Conventional commit styles in projects that use them, i.e."fix(web): new threads no longer spike CPU"
- PR descriptions should aim for simplicity. Open with a minimal, clear description of the problem. Follow up with how you solved it.
- Add a blurb to the end of the PR description about what model and harness is making the changes.
- **Open a real PR, not a draft.** Drafts do not get review-bot coverage.
- **Rebase onto latest `main` before opening.** Stale branches conflict and waste a review round.
- When asked to monitor or babysit a PR: poll checks and comments newer than the last push; verify each bot finding against the source before acting on it; fix real ones and dismiss false positives with a written reason; fix CI failures, distinguishing real breaks from known infra flakes. If nothing is new, stay quiet — do not post filler comments. Stop when the repo's review bots are green on the latest commit.
- Merge only per the disposition given in the request (merge when green, or stop and report). If none was given, report and ask.
