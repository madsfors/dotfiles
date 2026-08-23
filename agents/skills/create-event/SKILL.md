---
name: create-event
description: Creates, updates, reschedules, or removes Apple Calendar events with Mads's calendar and title conventions. Use whenever Mads asks to add, book, block, schedule, move, rename, or remove calendar time, including natural-language requests that do not name this skill.
---

# Create calendar event

Make the requested calendar change without expanding it into a planning session.

## Rules

- Use Swift EventKit for calendar reads and writes. AppleScript hangs for event queries on this Mac.
- Read the relevant date range before changing anything.
- Do not invent blocks or add related Things tasks.
- Ask when date, time, duration, calendar, or event type is materially unclear.
- Present the exact title, date, time, duration, calendar, and conflicts before writing. The user's approval authorizes the mutation.
- Deduplicate by title, start, and end.
- Verify every mutation by reading the affected interval again.

## Calendar routing

- `Calendar`: Work.
- `Privat`: Personal.
- `❤️`: Family and shared plans.
- `Træning`: Exercise.

Use the calendar implied by the request. Ask rather than guessing between personal and shared-family events.

## Agent marker

End every agent-created title with exactly one `🤖`.

Do not add the marker to manually created events, external invitations, or unrelated existing events. Preserve it when updating an agent-created event.

## Deep work

Use:

`👨‍💻 Deep Work - [Topic] - [Duration] Focus Work 🤖`

The title duration must match the event. Give the block one topic and one definition of done in its notes.

Admin, email, errands, and quick follow-ups stay in Things unless Mads explicitly asks to block calendar time.

## Conflicts and invitations

1. Read events covering the interval and relevant travel or buffer time.
2. Report overlaps before writing.
3. Do not create an overlap without explicit approval.
4. Treat broad `Time Blocked` events as intentional context.
5. Respect work boundaries, family commitments, travel, and the 21:00 device-off routine.

EventKit can maintain local calendar events but is not a reliable way to create Outlook or Teams invitations with attendees. For invitations, draft the details and let Mads create or update the invitation in Outlook. Do not add a duplicate local placeholder unless requested.

## Updates and recurring events

- Change or remove an event only when explicitly requested.
- Update an existing event when rescheduling instead of creating a duplicate.
- Change one occurrence of a recurring event unless the full series is explicitly requested.
- Never alter organizer-owned attendee details.
- Let declined or cancelled Outlook events synchronize from Outlook unless Mads requests a local calendar action.

## Execute

1. Parse create, update, move, rename, or remove.
2. Resolve title, calendar, date, start, end, duration, and notes.
3. Query EventKit for the relevant interval and writable calendars.
4. Present the exact proposal and any conflicts.
5. Wait for approval.
6. Apply the smallest requested mutation with the correct recurrence span.
7. Query the interval again and verify title, calendar, start, end, notes, and recurrence scope.

Never claim success before verification.

## Confirm

Respond with the final title, date and time, calendar, and any remaining Outlook action.
