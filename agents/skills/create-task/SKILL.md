---
name: create-task
description: Creates, routes, schedules, and verifies Things3 tasks using Mads's list semantics and task-writing conventions. Use whenever Mads asks to create, add, capture, schedule, or remember a task or to-do in Things, including natural-language requests that do not name this skill.
---

# Create Things task

Create only the requested task or tasks. Planning and prioritization belong in `/prioritize` when that vault skill is available.

## Rules

- Preserve the language of the request.
- Write a specific title beginning with an action.
- Put context, links, constraints, and definition of done in notes.
- Things notes support Markdown. Use sentence-case headings and bullets when structure helps; do not use all-caps section labels.
- Create separate tasks for separate actions unless Mads requests one checklist.
- Search open tasks for exact and near duplicates before creating anything.
- Use the most specific existing project, then its area. Read live Things names instead of guessing.
- Do not rewrite, complete, cancel, or delete unrelated tasks.
- A request to create a task authorizes that task. Ask only when timing or destination would materially change the result.

## List semantics

- `Today`: Mads intends to do it today.
- `Anytime`: Mads intends to do it this week.
- `Upcoming`: The task cannot be acted on before a specific future date.
- `Someday`: Deliberately deferred beyond this week.
- `Inbox`: Intentional quick capture or unresolved routing.

Use a deadline only for a real consequence date. Keep an actionable task in Anytime even when Mads expects to do it on a particular day. Schedule it only when it cannot be acted on before that date.

## Tags

Use only when supported by context:

- `⭐ Top 3`: One of the current three weekly outcomes.
- `💬 Discuss`: Agenda item for a named person or meeting.
- `⏳ Waiting`: Mads has acted and awaits someone or something.

For waiting work, record what is awaited and when Mads acted. Add a follow-up date only when requested or agreed.

## Execute

1. Read conversation context for action, timing, destination, notes, and tags.
2. Inspect Things for duplicates and live area/project names.
3. Create through Things3 AppleScript. Never write to the Things database.
4. Route to Today, Anytime, Someday, or a future date.
5. For a genuinely unavailable-until date, use `schedule task for date`; setting `activation date` directly is unreliable. Never schedule a task merely because its deadline or intended workday is in the future.
6. When parking a task in a project under Someday, move it to Someday first and then attach it to the project. Reversing the order can detach it.
7. Use `linefeed` when constructing multiline AppleScript notes.
8. Verify title, notes, area/project, tags, scheduled date, and deadline in Things.

If AppleScript cannot write, use the documented Things URL scheme only after duplicate and routing checks succeed through AppleScript or a read-only database query. Percent-encode values with spaces as `%20`; do not use form encoding that turns spaces into `+`. Verify the created task through AppleScript or a read-only database query. If verification is impossible, report that and do not claim success.

## Confirm

Respond with the title, destination, and timing or deadline when relevant. Do not repeat all notes unless asked.
