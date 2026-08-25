---
name: ux-flow-plan
description: Plan user-facing features by mapping current and desired UX and system flows before attaching code-level anchors. Use when behavior, ownership, or architecture of a user-facing change is not yet clear. Do not use for mechanical implementation work with a settled flow.
---

# UX flow plan

Create a read-only implementation plan that begins with the experience and ends with concrete code anchors. Do not edit files unless the user separately asks for implementation.

## Establish the goal

- Restate the intended user outcome in the user's language.
- Identify the entry point, affected actors, and completion state.
- Inspect existing product behavior and code before describing the current flow.

## Map the flows

Show the current flow only when existing behavior is relevant. Always show the desired flow.

```text
User trigger
├─ System decision
│  ├─ User-visible response
│  └─ Side effect or persistence
└─ Recovery or alternate path
```

Include loading, empty, error, permission, cancellation, and recovery states only when they materially affect the feature.

## Decide boundaries

For each important transition, identify:

- where the condition is detected
- which layer owns the decision
- which layer performs side effects
- how UI status and feedback are updated
- where state is persisted or synchronized
- how failure or interruption is recovered

Separate existing coupling from intentional new coupling. Do not preserve a boundary merely because the current implementation happens to use it.

## Attach implementation anchors

Only after the desired flow is clear, map it to:

- existing functions, components, routes, commands, or domain services
- files and abstractions to reuse or change
- state and data contracts
- focused tests that prove the flow and boundary decisions

Treat these as anchors, not as the main narrative. Do not invent symbols or files that have not been verified.

## Finish with decisions

End with:

1. recommended architecture
2. alternatives rejected and why
3. assumptions that were verified
4. open decisions that require the user
5. the smallest coherent implementation sequence

If the behavioral flow is settled but the visual or interaction direction is not, offer the explicit `emil-prototype` workflow as a separate next step.
