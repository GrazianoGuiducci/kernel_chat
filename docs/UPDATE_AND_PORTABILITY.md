# Update and Portability

Status: update/portability discipline for the `0.3.0` first integrated incarnation.

This document separates upstream package evolution from user-owned durable state. `0.3.0` does not yet provide an automated updater; the rules below define what an updater must preserve if one is added.

## 1. Two kinds of evolution live in one fork

A fork contains both distributable implementation and user-owned continuity.

```text
upstream package evolution
+ user/fork evolution
-> one working incarnation
```

These must not be treated as interchangeable.

## 2. Upstream-owned distribution surfaces

These normally evolve from the `Meta_Semantic_Kernel` upstream project:

```text
kernel/
evolution/
evals/
scripts/
adapters/<host>/ reusable templates and contracts
docs/
README.md
INSTALL.md
validation workflow
```

A fork may intentionally modify them, but then an upstream update may require a real merge decision rather than blind replacement.

## 3. Fork-owned mutable surfaces

These normally contain the user's durable incarnation and should not be overwritten by an upstream update:

```text
state/CURRENT_PRESENT.md
state/ACTIVE.md
operations/CURRENT_STATE.md
operations/flows/ user flow instances
operations/requests/ user request/result instances
operations/receipts/ user receipts
configured host-adapter output
host/account installation state that is specific to the fork
```

The repository currently ships seed/template forms for some of these paths. Once the fork has real user state, that state is part of the fork and is not distribution boilerplate.

External project truth remains outside both layers in its owner-native source.

## 4. Generated local configuration

For ChatGPT:

```text
adapters/chatgpt/CUSTOM_INSTRUCTIONS.md
-> upstream reusable template

adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md
-> generated fork-local configuration
```

The configured file is ignored by Git by default. Regenerate it after an upstream adapter change rather than copying another user's configured output.

An upstream repository change cannot update Custom Instructions already installed in a host. Source update and host installation remain separate effects.

## 5. Current manual update discipline

Until an automated updater exists, prefer normal Git history rather than copying folders over a fork.

A typical fork can keep an `upstream` remote pointing to the canonical repository and periodically fetch it.

Before integrating a newer upstream version:

```text
1. preserve/commit current fork state where appropriate
2. fetch the new upstream state
3. inspect changes to shared implementation surfaces
4. merge/rebase according to the fork's chosen Git workflow
5. resolve conflicts by ownership and meaning, not by newest-file-wins
6. preserve user state and operational evidence
7. regenerate configured adapters if the template changed
8. run structural validation
9. continue normal use
```

Do not overwrite `state/` or operational instances merely because upstream ships a newer seed copy.

## 6. Conflict rule

When an update conflicts, first determine what kind of relation is in conflict.

### Shared implementation conflict

Example: the fork modified `kernel/ROUTING.md` and upstream changed the same relation.

Treat this as an actual semantic/code merge. Preserve the fork difference when it is still useful; adopt upstream when it supersedes it; integrate both when they express compatible material relations.

### User-state conflict

Example: upstream seed `state/CURRENT_PRESENT.md` differs from the fork's lived present.

The fork's lived state wins by ownership. Upstream may change the **shape or contract** expected of the state, but migration should transform the user's state rather than replace its content.

### Operational-history conflict

Receipts, checkpoints and actual observed effects are evidence. Do not delete or rewrite them merely to match upstream layout. Migrate or archive them if a schema/structure later changes.

### Adapter conflict

Keep the reusable upstream adapter contract distinct from fork-local coordinates and host installation. Regenerate local configuration after integrating the template.

## 7. What an automated updater must eventually do

If a deterministic updater is introduced, it should at minimum:

```text
identify current package version/revision
identify upstream target revision
classify changed paths as shared implementation vs fork-owned state/configuration
never overwrite fork-owned state silently
surface semantic conflicts for review
apply deterministic migrations when a versioned migration exists
regenerate configured adapter only when explicitly requested
validate the resulting source tree
produce an update receipt
never change host settings or external project sources
```

The updater must not treat Git synchronization as semantic authority.

## 8. Migration rather than reset

A future version may change the shape of state or operations. The correct relation is:

```text
old user-owned state
+ explicit migration relation
-> new compatible state preserving material continuity
```

not:

```text
new package seed
-> overwrite old state
```

When no safe deterministic migration exists, preserve the old material and require a bounded review rather than guessing.

## 9. Moving to another repository

To move the same incarnation to another repository/account:

1. create or clone the destination repository under the intended owner;
2. preserve the shared implementation and the user-owned state/operations that should continue;
3. configure the host adapter with the new repository coordinates;
4. install/replace the configured adapter in the host separately;
5. update only external source pointers that actually changed location;
6. keep receipts and causal history needed for continuation.

Changing repository coordinates does not require changing the meaning of the kernel or resetting the user's continuity.

## 10. Moving to another conversational host

Portability does not mean copying ChatGPT instructions into another provider.

The desired relation is:

```text
same shared core/state/operations
+ host-native adapter
+ host-local capability attestation
-> another incarnation
```

A new adapter belongs under:

```text
adapters/<host>/
```

It should define only what is needed to connect that host to the shared repository and its actual capabilities.

Do not move into the shared core:

```text
ChatGPT Custom Instructions mechanics
provider-specific tool names
assumed scheduler/background behavior
host-specific permission model
private account identity
```

If the new host exposes a materially different relation that improves the shared core, route the host-independent invariant back to the package rather than universalizing the adapter itself.

## 11. Moving operational work across executors

An unfinished flow may outlive the executor that previously acted on it.

Preserve:

```text
flow identity
checkpoint/cursor
pending relation
request/result identity
receipts
known effects
recovery/stop state
```

Then attest the replacement executor or host when it becomes operative.

Do not infer that the replacement owns the project's semantic truth or inherits historical effect authority.

## 12. Backup and recoverability

The Git repository is already a versioned durability surface for committed state. The user decides how much personal/operational state should be committed and what repository visibility is appropriate.

Before destructive migration or major update, ensure the current material state is recoverable through Git history or another user-controlled backup.

Do not store secrets in the repository as a backup mechanism.

## 13. Version and release boundary

The project version describes the integrated upstream incarnation. A fork may additionally preserve its own revision/history.

A future distribution should make these distinguishable:

```text
upstream package version
fork revision/state
host adapter source version
configured adapter identity
installed host state
```

`0.3.0` currently has project-state versioning through `CURRENT_STATE.md` and Git history. A dedicated `VERSION`, release/tag and changelog lifecycle can be added when the distribution/release owner selects that form.

## 14. Current practical rule

Until tooling automates this safely:

> Update shared implementation through an explicit Git merge, preserve lived fork state by ownership, regenerate host configuration when its template changes, and never make an upstream update a reason to erase continuity.
