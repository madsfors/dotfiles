---
name: workflow
description: Orchestrate complex coding implementations, bug fixes, refactors, and architectural changes that genuinely require a multi-step plan and verification. Use when work spans several dependent changes or the user asks for structured execution. Do not use for read-only questions, research, audits, strategy discussions, or ordinary one-pass edits.
---

# Workflow orchestration

Use this skill only when structure materially improves a complex coding task. Match the ceremony to the work instead of turning every multi-step request into a project-management exercise.

## Plan

- Inspect the relevant code and constraints before committing to an approach.
- Define the outcome, dependent steps, risks, and verification.
- Track the plan with the environment's plan mechanism when available.
- Create `tasks/todo.md`, `tasks/lessons.md`, or similar repository files only when the repository already uses them or the user asks for them.
- If evidence invalidates the approach, stop and revise the plan.

## Delegation

- Default to one agent when the task can be completed coherently in one pass.
- Delegate only when parallel breadth, independent investigation, or adversarial review adds meaningful value.
- Give each delegated task a bounded scope and clear file ownership.
- Do not delegate merely to satisfy this workflow.

## Execute

- Prefer the smallest root-cause change that solves the problem.
- Keep changes scoped to the requested outcome and preserve unrelated work.
- For bug reports, inspect the evidence and fix the issue autonomously when authority is clear.
- Reconsider the design when a fix adds another workaround layer or unnecessary abstraction.

## Verify

- Prove the relevant behavior before reporting completion.
- Run focused tests, checks, or comparisons proportional to the risk.
- Distinguish verified results from checks that could not be run.
- Review the final diff for unnecessary complexity and unintended blast radius.

## Learn from corrections

- Apply user corrections to the current work immediately.
- Propose a durable rule only when the pattern is likely to recur.
- Do not write lessons, memories, or project instructions unless the user authorizes that persistence.

## Report

- Lead with the outcome.
- Summarize material changes and verification.
- Name unresolved risks or decisions without narrating routine tool use.
