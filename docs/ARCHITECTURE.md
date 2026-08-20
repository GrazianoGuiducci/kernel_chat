# Architecture

Status: `0.3.0` first integrated incarnation  
Scope: explain what the package contains, how its parts relate, and where ownership remains.

## 1. One package, distinct organs

`Meta_Semantic_Kernel` is delivered as one user-owned repository, but it does not collapse every function into one file or one mandatory workflow.

```text
host adapter
    |
    v
current conversation / present
    |
    +-- sufficient now ------------------------> direct work
    |
    +-- durable semantic relation matters ----> state/
    |
    +-- routing/competence matters -----------> kernel/
    |
    +-- unfinished causal work matters -------> operations/
    |
    +-- reusable change emerges --------------> evolution/
```

The repository is a durable reentry and continuity surface. It is not automatic authority over the host, connected projects, external services or effects.

## 2. Package map

### `adapters/`

Host-specific activation and capability binding.

The ChatGPT adapter is intentionally smaller than the kernel. It tells the host how to locate the user's repository and how to enter it selectively. Source presence, configured adapter text, installed host instructions, actual repository access and observed behavior remain separate states.

A future provider receives its own adapter rather than forcing provider-specific mechanics into the shared core.

### `kernel/`

The portable cognitive-semantic relation.

- `KERNEL.md` — present-first cognitive core and source/effect distinctions.
- `ROUTING.md` — expands the working set only when another relation can change the result.
- `COMPETENCE.md` — lets useful competence participate without treating the known catalogue as a ceiling.

The kernel does not assume a shell, daemon, scheduler, filesystem, connector or background runtime unless the active host actually exposes it.

### `state/`

Durable semantic/cognitive reentry owned by the user's fork.

- `CURRENT_PRESENT.md` — compact current material state.
- `ACTIVE.md` — only durable relations that have earned low-latency attention.

State is not a transcript archive. It should contain only what would materially change later recognition, routing or continuation.

### `operations/`

Durable causal continuity for unfinished work.

It can represent:

```text
active flow
cursor / checkpoint
pending decision / result / effect
stored schedule relation
replaceable executor route
bounded request/result identity
receipt
recovery / supersession
```

An operational record does not imply that a worker, scheduler or autonomous process is running.

The operational organ stores continuity, not copies of external project truth.

### `evolution/`

Admission and revision of durable change.

- `CRYSTALLIZATION.md` — decides what deserves persistence and at what attention level.
- `EVOLUTION.md` — preserves useful change at the smallest truthful surface and allows revision, cooling, supersession or de-kernelization.

A stored correction is not automatically an assimilated competence. Later changed behavior is stronger evidence.

### `evals/`

Behavioral discriminants. They describe failure and useful behavior but are not executed proof merely because they exist.

They are aids for observing real use, not a required ritual before work can begin.

### `scripts/`

Deterministic support tools.

- `configure_chatgpt_adapter.py` — configures the ChatGPT adapter offline for a user-owned repository.
- `validate.py` — verifies source structure and claim boundaries. It does not prove host behavior or portability.

## 3. Reentry model

Normal use starts from the present, not from repository traversal.

```text
conversation sufficient
-> work directly

missing durable semantic relation changes result
-> state/CURRENT_PRESENT.md
-> only the relevant owner/source pointer

unfinished causal work changes continuation
-> operations/CURRENT_STATE.md
-> only the relevant flow/request/receipt

competence materially changes result
-> kernel/COMPETENCE.md
-> owner-native competence or local extension only as needed
```

Stop expanding when another read would not change the result or next movement.

## 4. Ownership model

The fork owns its own kernel incarnation and continuity state. It does not become owner of every source it references.

```text
package/core implementation       -> this repository
user durable present              -> user's fork state/
user operational continuity       -> user's fork operations/
host installation/configuration   -> host/account + adapter
external project truth            -> external project's owner-native source
external effect authority         -> exact target/controller relation at the moment of effect
```

Use pointers to external owner-native sources rather than mirroring their current state into the kernel repository.

## 5. Capability and authority

Keep these distinct:

```text
relation is cognitively useful
!= capability exists on this host
!= capability is accessible now
!= an operational route exists
!= authority for the effect exists
```

A verified current host limit must be respected in the current movement, but it is not automatically a universal cognitive or future limit.

Authority is resolved for a concrete material effect when that effect exists. Ordinary cognitive work should not carry speculative permission workflows.

## 6. Operational continuity without an agent runtime

The package can preserve unfinished work even when the conversational host is turn-reactive.

```text
executor loss != continuity loss
```

A previous executor may disappear while the user's fork still preserves the flow, checkpoint, pending relation and evidence needed to continue later or through another executor.

Historical intent is not live authority. Recovery must inspect what actually happened before retrying or repeating an effect.

## 7. Evolution without self-approval

A material change may belong to state, an operational contract, an adapter, a local competence, routing, the cognitive core or an external owner. `kernel` is not the automatic destination.

Useful evolution should remain reversible and source-linked. A component may be simplified or removed when it becomes ritual, noise, redundant structure or host-specific residue.

## 8. What is intentionally not inside the core

The current integrated incarnation does not require:

```text
RepoKernel generation morphology
fixed capability-family taxonomy
MAIOS/D-ND private repository paths
private operator state
TM executor identity
background autonomy
product/publication workflow
one provider's mechanics as universal architecture
```

Those may exist elsewhere as lineage, implementation history or future product relations. They are not runtime dependencies of the portable core.

## 9. Current maturity boundary

`0.3.0` means that a coherent all-in-one implementation exists and can be configured and used. It does not by itself prove stable kernel maturity, later-use assimilation, second-host portability or public-release maturity.
