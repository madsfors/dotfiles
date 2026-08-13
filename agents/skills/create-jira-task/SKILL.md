---
name: create-jira-task
description: Creates concise Jira tasks on Mads's behalf. Use whenever Mads asks to create, add, file, capture, or assign a Jira task or work item, including requests that do not explicitly invoke /create-jira-task.
---

# Create Jira task

Turn the conversation into a Jira task the assignee can execute without filler.

## Defaults

- Write Jira content in English.
- Use the `UX` project unless Mads names another project.
- Use the `Task` issue type unless Mads explicitly requests another type.
- If Mads does not name an assignee, ask before drafting.
- Infer priority, labels, and due date using best judgment. Set only fields that add useful signal.
- Include only links the assignee needs to complete the work.

## Writing

- Use a short title in the form `[Area or system]: [action]`.
- A title can stand alone when it gives the assignee enough direction.
- Otherwise add one short sentence. Add bullets only when Mads supplied a checklist or the task would otherwise be ambiguous.
- Do not add a `Done when` section unless Mads asks for one.
- Do not force a template or add empty sections.
- Do not restate the title as context, scope, objective, and deliverables.
- Ask when a material ambiguity would change the work instead of inventing scope.

Every task must include this attribution at the end of its description:

`🤖 Created by Cursor on behalf of Mads Fors (MAFO).`

When the title needs no supporting description, use the attribution as the entire description.

## Workflow

1. Read enough conversation context to understand the requested outcome.
2. Search the target project for similar open work.
3. If a likely duplicate exists, show its Jira link and ask whether Mads still wants a new task.
4. Resolve the named assignee to the correct Jira account.
5. Draft the smallest task that remains independently actionable.
6. If the action, project, and assignee are clear, create the task directly.
7. Ask one focused question only when a missing decision would materially change the task.
8. Verify the created issue's title, description, project, type, assignee, attribution, and inferred metadata.

## Response

After creation, respond with one short line containing the title, assignee, and Jira link. Mention non-default inferred metadata only when Mads should know about it.

## Calibration

Good title-only task:

`ODS: Define publishing and governance process`

Bad title:

`Legacy SharePoint cleanup`

Good title:

`UX SharePoint: Archive and unpublish legacy pages`

Bad description:

`The goal of this task is to ensure that deprecated legacy SharePoint pages are handled through a structured archival and retirement process.`

Good description:

`Back up each page and its linked assets, remove old links, then unpublish it and test visitor access.`
