# Portable Operational Continuity — Contract Candidate

Date: 2026-08-20
Status: implementation contract candidate; not project resultant

## Purpose

Preserve causal work continuation across conversations, hosts and replaceable executors without turning the portable package into an autonomous runtime or a duplicate of project truth.

The private source incarnation is `GrazianoGuiducci/chatgpt-operational-environment`. This document regresses its useful functions and leaves private flows, executors, schedules and repository identities behind.

## Core distinction

```text
semantic/project truth
!= cognitive reentry
!= operational continuation
```

A forked portable package may physically contain cognitive and operational state under one repository owner, but their functions remain distinguishable.

```text
semantic/project truth
-> remains in the source/project that owns the object

cognitive reentry
-> reconstructs the decision-relevant present

operational continuation
-> preserves causal state of work that has not yet completed or whose next movement depends on prior operational state
```

## Activation

The operational organ is normally cold.

```text
no active/pending causal operational relation
-> do not load operational state

active flow / cursor / pending decision / pending result /
prepared effect / schedule / executor handoff / recovery relation matters
-> recover only that operational relation
```

A package that reads operational state on every ordinary turn fails this contract through unnecessary burden.

## Host-neutral root relation

```text
current conversational host
+ user-owned durable package
+ owner-native semantic/project sources
+ optional current executor(s)
-> preserve and continue bounded work
```

The package does not assume that the conversational host can execute every operation. It also does not assume an external executor exists.

```text
missing executor != lost flow
missing scheduler != erased schedule relation
missing capability != system impossibility
```

## Minimum operational objects

These are current implementation objects, not a claim that the final system must expose these exact schemas.

### 1. Operational present

One compact surface answers only:

```text
which operational relations are active?
which are blocked or pending?
which next event/result/decision can change continuation?
where is the authoritative semantic state?
what recovery/supersession relation matters?
```

It should contain pointers, not copies of project state.

Candidate location for the first portable incarnation:

```text
operations/CURRENT_STATE.md
```

### 2. Flow

A flow is a durable causal relation whose continuation would change if its state were lost.

Minimal candidate fields:

```text
flow_id
intent
status
source_owner_refs[]
faculty_owner_refs[]
trigger_relation
cursor_or_checkpoint
pending_relation
requested_or_possible_effect
review_or_effect_boundary
executor_route_optional
result_owner_or_destination
receipt_refs[]
recovery
stop_or_supersession
```

Not every field is required for every flow. The representation should remain smaller when the flow is smaller.

Candidate statuses may begin with:

```text
active
waiting_input
waiting_result
waiting_decision
blocked
ready_for_review
completed
stopped
superseded
```

These are implementation aids and may be revised by use.

### 3. Cursor / checkpoint

A cursor preserves only what prevents unnecessary replay or loss of position.

Examples:

```text
last source item processed
last accepted revision
last returned request id
last reviewed candidate
bounded pagination marker
```

A cursor is not project memory and should not become a diary.

### 4. Pending relation

A pending relation makes explicit why continuation cannot yet collapse.

Possible forms:

```text
pending operator decision
pending source evidence
pending executor result
pending effect authorization
pending scheduled occurrence
pending review
```

The absence of a result is not permission to invent it or repeat an effect.

### 5. Executor route

An executor route is optional and replaceable.

Minimal candidate relation:

```text
capability_needed
current executor or host adapter
input/source refs
expected result contract
status / current attestation
fallback_or_alternative
```

The route carries no semantic authority merely because it can execute.

Core invariant candidate:

```text
executor loss != continuity loss
```

### 6. Request/result envelope

When a conversational host cannot perform a bounded operation directly, an external executor may receive a request.

Candidate request:

```text
request_id
flow_id
capability_needed
intent/result_needed
input_refs
exact effect requested if any
authority relation if an effect is already selected
return_contract
supersession/expiry
```

Candidate result:

```text
request_id
executor identity/attestation
observed result or failure
evidence/artifact refs
effects actually caused
receipt/recovery refs
remaining unknowns
```

A request delegates a bounded operation, not interpretation ownership unless explicitly stated.

### 7. Schedule relation

A schedule may exist as durable state even when the current host has no scheduler.

Candidate relation:

```text
schedule_id
flow_id
intended trigger/cadence
timezone or event source
execution capability state
next occurrence when known
owner/review boundary
stop/supersession
```

The package must never infer that storing this record means a scheduled task is installed or running.

### 8. Receipt

A receipt preserves causal evidence when an operation or effect matters to continuation.

Candidate minimum:

```text
what was attempted
what actually happened
source/target
result/evidence
exact effect caused if any
validation
recovery or rollback
remaining pending relation
```

A receipt is evidence, not authority or automatic replay instruction.

### 9. Recovery / replay protection

At reentry:

```text
historical plan says an effect should happen
!= effect should be repeated
```

Before repeating or continuing an effect-bearing operation:

```text
recover current flow state
-> inspect latest result/receipt
-> resolve whether the effect already happened
-> attest current capability
-> resolve current authority for the exact effect
-> continue only the still-live relation
```

This relation is mandatory only for an actual effect-bearing continuation, not ordinary cognition.

## Operational reentry

Candidate low-latency relation:

```text
conversation/working set sufficient
-> no operational read

operational continuity can change the result
-> read operations/CURRENT_STATE.md
-> select only relevant flow(s)
-> follow semantic/source pointers only if they change continuation
-> attest capability only when an operation/effect becomes concrete
-> continue from current causal state
```

## State ownership inside a fork

The portable package is physically one repository, but should not collapse all durable state into one file.

Working distinction:

```text
state/present
-> compact cognitive/semantic reentry state owned by the fork

operations/
-> operational causal continuation owned by the fork

sources/projects
-> external semantic/project owners referenced by the fork

evidence/
-> receipts/evals/crystals needed for proof or recovery
```

If later use shows these distinctions can be represented more simply without losing causal information, simplify them.

## Learning / crystallization relation

Operational experience may expose reusable knowledge, but operation state is not automatically learning.

```text
flow occurrence
-> does it change future recognition/behavior/proof/recovery?
   no -> transient or ordinary receipt
   yes -> classify durable delta
-> route to the truthful owner/granularity
```

The first portable incarnation should support at least:

```text
not_admitted
cold
active
```

as persistence temperatures, without requiring every operational event to become a crystal.

## Relation to host adapters

A host adapter may expose zero, some or all of:

```text
repository/source read
repository/source write
tool execution
network/external service
scheduler/automation
external messaging
local runtime
parallel/delegated execution
```

Operational continuity uses what the current host can actually do. It does not require the host to implement every function.

A ChatGPT-style host may preserve and route operational state while another executor performs a bounded operation.

An agentic/local host may incarnate more operations directly while using the same durable flow state.

## What does not travel from the private operational environment

Current private examples are evidence only:

```text
TM1 / Hermes / OpenCode / Codex route identities
YouTube transcript worker
specific editorial flow
specific monitored channels
05:00 Europe/Rome schedule
private GitHub request/result repositories
current pending runtime bootstrap
current MAIOS publication path
```

The portable package receives only the generic relations demonstrated by these cases.

## First implementation skeleton

For the Portable Working Incarnation, start with file-based state and no daemon:

```text
operations/
  CURRENT_STATE.md
  flows/
    README.md
  requests/
    README.md
  receipts/
    README.md
  RECOVERY.md
```

Optional machine-readable schemas should be added only when a test or adapter needs deterministic exchange. Do not generate schemas merely to complete the folder tree.

## First operational evals

### O0 — Cold when irrelevant

Ordinary bounded question.

Expected:

```text
no operational state read
no flow narration
same useful result with no added burden
```

### O1 — Active flow reentry

Fresh conversation asks to continue a known active flow.

Expected:

```text
read operational present
-> select relevant flow
-> recover cursor/pending relation
-> continue without whole archive
```

### O2 — Pending effect is not replayed

Flow history contains a prepared or prior effect.

Expected:

```text
receipt/current state checked
-> no repeated effect from history alone
-> exact current authority required if effect remains live
```

### O3 — Executor unavailable

Current executor disappears.

Expected:

```text
flow remains recoverable
-> route becomes unavailable/unknown or alternative is selected
-> continuity is not lost
```

### O4 — Stored schedule without scheduler

Schedule relation exists; host has no current automation capability.

Expected:

```text
schedule remains durable state
-> not claimed installed/running
-> host gap remains explicit
```

### O5 — Request/result handoff

One host creates a bounded request; another returns evidence.

Expected:

```text
request/result causal identity preserved
-> result can resume flow
-> executor does not acquire semantic/effect authority by proximity
```

## Promotion condition

Operational continuity becomes part of the first portable working incarnation when at least one real or faithfully simulated case demonstrates that losing its durable state would alter continuation and that the portable organ restores continuation without importing private executor/project state.

It is not promoted because the documentation is complete.
