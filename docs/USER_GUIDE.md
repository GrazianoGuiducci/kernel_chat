# User Guide

Status: practical guide for the `0.3.0` first integrated incarnation.

This guide explains normal use after configuration. It is not a test protocol and does not require the user to narrate kernel operations.

## 1. Start once

For ChatGPT, follow `INSTALL.md`:

```text
fork or own the repository
-> configure the adapter for your repository coordinates
-> install the complete configured text in Custom Instructions
-> make the repository accessible through the host's GitHub connection when available
```

After that, use the chat normally.

The repository should not be opened for every question. The installed adapter exists so the host can recover durable context only when it changes the result.

## 2. Ordinary conversation

Ask normal questions normally.

If the current message and conversation are sufficient, the expected behavior is simply:

```text
request
-> answer / work
```

No boot narration, repository tour, operational-state loading or explicit competence selection is needed.

## 3. Continuing work across conversations

Use the repository when the current conversation is missing a durable relation that changes continuation.

The main semantic entry is:

```text
state/CURRENT_PRESENT.md
```

It should carry a compact present, not the entire history.

A useful current present may contain:

```text
what is currently being worked on
accepted current relation or direction
compact pointers to owner-native project/source material
material unresolved relations
whether operational continuity is active
```

Do not copy a project's full state into this repository when a pointer to the real owner is sufficient.

## 4. Connecting a project

When a project repeatedly matters across conversations, add the smallest useful binding to `state/CURRENT_PRESENT.md`.

Example form:

```text
project/source binding:
  owner: <repository or other durable source>
  relation: <why it can change current work>
  entry: <specific current-state or source path when useful>
```

The exact representation may remain smaller when less information is needed.

The external project remains the owner of its truth. This repository stores the relation needed to find and use it.

## 5. When operational continuity is needed

Operational state becomes useful only when unfinished causal work would otherwise be lost.

Examples:

```text
a process stopped at a checkpoint
an external result is still expected
a decision is pending
an effect was prepared but its actual outcome matters before continuing
a scheduled intention exists but execution may or may not be installed
a prior executor is unavailable and another route may be needed
```

The entry point is:

```text
operations/CURRENT_STATE.md
```

Create a flow under `operations/flows/` only when durable flow state is actually useful.

A flow may preserve:

```text
intent
status
cursor/checkpoint
pending relation
possible effect and its boundary
optional executor route
receipt references
recovery or stop condition
```

Do not create flows for ordinary one-turn tasks.

## 6. Requests to another executor

If the current host cannot close a bounded operational need, `operations/requests/` defines the request/result relation.

A delegated operation should remain bounded:

```text
request id
flow id when relevant
capability/result needed
input references
exact effect requested, if any
return contract
```

The executor's result is evidence, not automatic semantic authority. The receiving conversation decides what it changes using current sources and owners.

## 7. Receipts and recovery

Preserve a receipt only when losing evidence of an operation or effect would change later continuation, proof or recovery.

Typical reasons:

```text
an external effect happened
an attempted operation failed materially
a result must not be recomputed or repeated blindly
a later conversation needs evidence of what actually occurred
```

Before repeating an effect, check current state and relevant receipts. A historical instruction does not authorize replay.

`operations/RECOVERY.md` defines recovery when a flow is interrupted or an executor disappears.

## 8. Corrections, learning and persistent knowledge

Not every useful conversation becomes durable state.

Preserve a relation when losing it would materially reduce future understanding, continuity, capability, recovery or quality of action.

Use:

```text
state/CURRENT_PRESENT.md
-> current durable semantic relation

state/ACTIVE.md
-> small set of relations that have earned low-latency attention

evolution/CRYSTALLIZATION.md
-> decide whether and where something deserves persistence

evolution/EVOLUTION.md
-> decide whether a reusable change belongs to state, operations, adapter, competence, core or another owner
```

A note stored once is not automatically an assimilated competence. Later changed recognition or behavior is stronger evidence.

## 9. Host capability and effects

The package does not pretend the host has capabilities it does not expose.

For any concrete external effect, keep distinct:

```text
what would be useful
what this host can actually do now
what source/target is involved
who controls the target
whether the current interaction authorizes that exact effect
```

A current host limitation is real for the current movement when verified. It should not be generalized into a permanent or universal system limitation.

## 10. What you normally do not need to manage

A normal user should not routinely:

```text
read every kernel file
run eval cases before working
create operational flows for simple tasks
classify every message as a competence
precompute effect authority
load full project histories into CURRENT_PRESENT
edit the adapter for every conversation
```

The package should reduce reconstruction and drift, not add a new administrative ritual.

## 11. When to change the kernel itself

Change the core only when real use exposes a material reusable difference, such as:

```text
repeated routing friction
missing relation that affects results
unnecessary reentry or latency
operational state repeatedly losing causal information
host adapter repeatedly requiring the same correction
simpler representation preserving the same useful function
```

Prefer the smallest truthful surface. The correct outcome can be a state update, an operational change, a host-adapter change, a competence change, a core change, an external-owner update or no change.

## 12. Troubleshooting

### The chat never reads the repository

Check separately:

1. the adapter was configured with the correct GitHub coordinates;
2. the complete configured adapter was installed in the intended host/account;
3. GitHub access is actually available to that host/account;
4. the current request genuinely needs durable context.

Repository source alone does not install or activate anything.

### The chat reads too much

Reduce `state/CURRENT_PRESENT.md` to the material present and source pointers. Do not use it as an archive. The routing rule is to stop reading when another source would not change the result.

### The chat treats an old action as still pending

Inspect `operations/CURRENT_STATE.md` and relevant receipts. Record the actual observed result, then update or close the flow. Historical plans are not current effect authority.

### A project source conflicts with fork memory

Prefer the current owner-native project source for project truth. Preserve the contradiction only when its lineage or correction changes future work.

### The host cannot perform an operation

Preserve the bounded need or flow state. Do not call it a universal impossibility. Another route or host may later close the gap.

## 13. Privacy and secrets

Do not store access tokens, passwords, secret keys or credentials in kernel state, Custom Instructions or repository files.

A fork may contain personal or operational state. Choose repository visibility and connected-service permissions accordingly. Give a host only the access required for the work you intend it to perform.

## 14. Updating or moving the package

Read `docs/UPDATE_AND_PORTABILITY.md` before syncing a fork with a newer upstream version or moving the same durable state to another host/repository.
