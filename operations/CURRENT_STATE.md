# Portable Operational Current State

Status: working candidate
Updated: 2026-08-20
Operational state owner: this fork/repository

This surface is read only when unfinished causal work can change continuation.

## Current operational present

```text
active_flows: none
waiting_results: none
waiting_decisions: none
pending_effects: none
active_executor_routes: none
installed_schedules: none_attested
recovery_required: false
```

No background runtime, scheduler, worker or external executor is implied by this state.

## Reentry

When operational continuity matters:

```text
read this file
-> identify only the relevant flow/request/receipt
-> follow semantic/project owner pointers only when they change continuation
-> attest current host/executor capability only when it becomes operative
-> resolve exact authority only for a concrete effect
-> continue from the current causal state
```

When nothing here can change the result, return to direct conversation without further operational loading.

## Storage boundary

This operational organ may preserve:

```text
active flow pointers
cursors/checkpoints
pending decisions/results/effects
schedule relations
bounded executor routes
request/result identities
receipts
recovery/supersession
```

It must not mirror external project truth or store a full conversation history.

## Executor relation

```text
executor loss != continuity loss
```

An executor may become unavailable while the flow remains durable and recoverable.

## Next update

The first operational object should be created only by a real or test case that would lose causal continuation without durable state.
