---
name: zero-tech-debt
description: Review a current change from its intended end state and identify compatibility cruft, dead paths, and accidental complexity. Use only when explicitly invoked for a zero-tech-debt review. Review first and do not edit unless the user also asks for implementation.
disable-model-invocation: true
---

# Zero tech debt

Review the current change as if the intended product behavior and architecture had existed from day one. This is a deliberate, more aggressive lens than `proper-fix`, so it is read-only unless implementation is explicitly requested.

## Define the end state

- State the intended UX and architecture in one or two sentences.
- Limit the review to the current feature, branch, or explicitly named area.
- Identify what exists only because of the historical implementation path.

## Prove compatibility requirements

Search before preserving or deleting:

- repository callers and public exports
- API consumers and generated clients
- persisted data, migrations, and stored URLs
- feature flags, permissions, analytics, and operational tooling
- older deployed clients, plugins, integrations, or external consumers
- dynamic imports, reflection, configuration, and convention-based entry points

Absence of an in-repository caller does not prove that a public or persisted contract is unused. Mark uncertain contracts instead of deleting them.

## Classify the current shape

For each meaningful piece, choose one:

- **Keep:** belongs in the intended end state.
- **Reshape:** needed, but owned by the wrong layer or expressed through accidental structure.
- **Delete:** no verified caller or contract and no role in the end state.
- **Uncertain:** requires a product, compatibility, or operational decision.

Prefer one authoritative rule over mode flags, wrapper stacks, fallback chains, duplicated gating, and parallel meanings.

## Recommend the coherent result

- Describe the final product surface and ownership boundaries.
- Name compatibility paths that can be removed and the evidence supporting removal.
- Keep the proposal scoped; do not invent a generic framework for one feature.
- Distinguish cleanup required for coherence from optional adjacent improvement.

## Output

Lead with a verdict: `already coherent`, `targeted cleanup`, or `end-state refactor`.

Then report:

1. intended end state
2. keep, reshape, delete, and uncertain decisions
3. compatibility evidence
4. recommended final flow and ownership
5. verification required before and after implementation

## Implementation boundary

Do not edit during a review-only request. When implementation is explicitly authorized:

- preserve verified external and persisted contracts
- ask before deleting an uncertain compatibility path
- apply `proper-fix` for root-cause changes
- use `knip` only as supporting evidence for unused files, dependencies, or exports
- run focused tests for navigation, permissions, persistence, and migration behavior
- stop when the scoped end state is coherent
