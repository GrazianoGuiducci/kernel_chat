# User guide

## Use the chat normally

The kernel should be quiet when the conversation already contains what is
needed. Ask ordinary questions normally. You do not need to mention the
repository on every turn.

A new chat alone does not require a boot.

## Continue a relation in a new chat

When durable continuity matters and repository access is real, the bridge can
lead the host to `state/CURRENT.md`. That state should point toward only the
source or owner needed for the present question.

The current relation can be:

```text
no selected project yet
a project
a research object
a business/problem context
a recurring activity
another user-owned relation worth continuing
```

A project is therefore one possible context, not a prerequisite for the
kernel instance.

If the chat cannot reach the file, treat continuity as unavailable in that
turn. Do not invent repository contents or claim connector access.

For a missing way of understanding or working, the bridge instead reaches
`AGENTS.md` and the pertinent kernel owner. User state does not have to carry
the kernel's constitutive methods. These are selective paths, not boot stages.

## Know the three user-owned state surfaces

### `state/INSTANCE.json`

Carries instance/package/bridge identity and source-contact observation. Read it
when installation/update/source freshness can change the work.

It can distinguish:

```text
bridge template currently available
configured bridge provenance and bytes
repository targeted by a standard configured bridge
operator-confirmed installed bridge byte identity + target/provenance when known
```

The installed digest is an operator-reported receipt, not direct inspection of
ChatGPT. It does not own project/domain facts and does not prove connector
reachability or behavioral assimilation.

### `state/CURRENT.md`

Carries the smallest current relation/context that can change reentry:

- current point;
- why it matters;
- active relations;
- open causal work;
- accepted corrections;
- next movement when actually determined;
- relevant boundaries.

It is not an automatic task queue.

### `state/SOURCES.md`

Carries owner-native sources and the condition that makes each source useful.
Availability does not mean activation or authority.

## Maintain continuity

Update CURRENT/SOURCES when one of these changes materially:

- the current point or direction;
- an accepted correction;
- an owner-native source;
- unfinished work that should remain visible;
- a verified boundary;
- the pointer/reentry reason for a reusable way of understanding or working.

Do not store ordinary chat, duplicate summaries, credentials, or whole
histories. A short state with accurate pointers is more useful than a large
memory dump.

Keep reusable methods in the competence or kernel owner that uses them. State
may say what changed, why it matters now and where to recover that knowledge.
When resuming, check whether the reason is still valid instead of executing an
old next action automatically.

## Add a project or context later

Starting without a project does not lock the instance into an empty context.
When a project becomes material, update `state/CURRENT.md` and
`state/SOURCES.md` with the selected context and owner-native source.

This normally does **not** require changing the ChatGPT bridge, because context
and host entry are intentionally separate.

## Add competences and metacompetences

Link a competence from `state/SOURCES.md` when it owns a way of working that can
change the current result. Do not copy it into the kernel merely to make it
visible.

A metacompetence carries comprehension developed through experience so it can
be operated, integrated, and evolved in another situation. Its instruction
file can be an operating representation; later changed behavior is stronger
evidence that the comprehension was assimilated.

### Grow a competence in your instance

A useful continuing ability may emerge from intent, knowledge, memory,
successful work, a new possibility or a gap. Locate the owner that already
carries it; enrich that method or compose existing competences first when that
is the useful form. A distinct continuing function can have its own body.

For example, reusable source-comparison knowledge can live in
`knowledge/source-comparison.md`, or in an existing domain guide that already
owns it. The path is optional. Preserve what it makes possible, when it matters,
the sources/reasons behind it, how to adapt the method, what experience changed
it and what could invalidate it.

Add its real location to `state/SOURCES.md`, with its owner and the condition
that makes it useful. If current continuation depends on a correction, put a
short reason and pointer in CURRENT. Do not copy the whole method into state or
register every available competence as active.

On a later relevant task, the chat reaches the method, understands its reasons
and adapts it to the new object. Its result can call another competence or form
a temporary composition. If a later consequence changes an earlier method,
return that learning to the earlier owner. Preserve uncertainty when the
relationship is not established. No central orchestrator is required.

With real authorized repository writing, update that owner directly. With
read-only access, prepare the exact proposed change; do not claim it was saved.
A new file is availability, one use is exercise, and changed behavior on a
later non-identical task is stronger assimilation evidence.

## Preserve unfinished work

Use `Open work` in `state/CURRENT.md` for the causal remainder that should
survive the conversation. Describe what is unfinished and what evidence exists.
Do not turn it into automatic execution.

If work would lose a material cursor, pending relation, result or effect receipt
between conversations, use the optional [`operations/`](../operations/) organ.
Keep it cold when nothing there changes continuation. No scheduler, daemon or
executor is implied.

## Evolve the kernel

When a real situation is handled differently because of a reusable observation,
decide where the change belongs:

- user/domain truth goes to its owner-native source;
- current continuity goes to CURRENT/SOURCES;
- instance/package/bridge observation goes to INSTANCE;
- ChatGPT-specific friction goes to the ChatGPT adapter;
- reusable comprehension goes to a competence/metacompetence;
- a change to portable operating relations goes to `kernel/`.

Keep source, reason and an invalidating condition close to consequential
changes. Prefer small reversible edits over accumulated doctrine.

When a capability is present upstream in the reasoning but disappears later,
trace where it is first lost — representation, delivery, consumer, exercise —
instead of patching the nearest visible symptom.

## Update package and bridge separately

A package update may not require a bridge update.

```text
package source
!= bridge template currently available
!= configured bridge template provenance
!= configured bridge repository/bytes
!= operator-confirmed installed bridge incarnation
!= actual host behavior
```

Use `--refresh-instance` after adopting package changes when package/available-
template identity in INSTANCE should be refreshed. It does not rewrite the
configured bridge's historical template provenance.

A standard configured bridge contains the user-owned repository it reaches. If
a preserved legacy bridge names a different repository from the instance, do
not silently continue: use the matching instance identity or deliberately
replace the bridge.

Preview a bridge before replacement. `--replace-adapter` changes only the local
configured bridge and preserves the previous confirmed host digest as evidence
until the operator updates ChatGPT.

When the bridge is shown to the operator, retain the emitted
`confirmation_bridge_sha256`. After the operator copies/saves that delivered
bridge in ChatGPT, bind the report to that exact delivery digest:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --confirm-host-installation \
  --expected-bridge-sha256 DELIVERED_BRIDGE_SHA256
```

If the current configured bridge no longer matches the delivered digest, the
confirmation is rejected and the current bridge must be delivered again. This
receipt remains operator-confirmed evidence. Reachability and behavioral
assimilation still require their own observations.

## Source contact

During active use, `AGENTS.md` may make a light upstream check pertinent.
`state/INSTANCE.json` can preserve the last observed revision/time and material
delta so the next conversation need not reconstruct that observation.

This is not a background monitor. A newer upstream source does not automatically
replace local state, competences, bridge or installed instructions.

## Privacy and control

For non-public continuity, use a **private standalone repository** initialized
from the public source. Do not rely on the idea of a private fork of a public
GitHub repository.

A deliberately public fork is valid when public continuity is intended.

Never store tokens, passwords, private keys, secret logs or unapproved
sensitive material in the repository or Custom Instructions. Grant connectors
only the access you intend.
