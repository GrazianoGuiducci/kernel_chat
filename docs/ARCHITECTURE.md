# Architecture

`kernel_chat` separates the portable semantic relation from user-owned
continuity, host delivery and actual host behavior.

```text
canonical package
  portable kernel owners + adapters + templates + configurator + validation

user-owned instance
  INSTANCE identity/bridge/source-contact observation
  CURRENT relation/context
  SOURCES owner-native pointers
  optional local competences and knowledge

portable entry
  provider-neutral instruction template
  -> kernel source identity + constitutive owner paths
  -> direct installation through receiver-native persistent mechanisms
  -> optional host adapter when packaged receiver-specific mechanics are useful

host adapter, when present
  receiver-specific rendering / delivery mechanics
  -> configured local projection with its own provenance / source target
  -> operator-confirmed installed incarnation receipt when that host supports it
  -> instructions actually installed in the host

actual host
  available connector/tool/capability reality
  -> situated work
  -> effects and consequences

operational continuity
  optional unfinished flows, requests/results, receipts and recovery
```

These layers are related but not interchangeable.

## Canonical package and user-owned instance

The public upstream owns the distributable package. A user-owned instance owns
its continuity state and local evolution.

A private instance can be a standalone private repository initialized from an
identified upstream revision/release. A public fork is valid when its state is
intentionally public. The package is not a living user node merely because its
source exists.

A project is optional. It can become one current context/source without becoming
the identity of the instance.

## State owners

### `state/INSTANCE.json`

Owns the smallest durable package/incarnation metadata that should not be mixed
with domain state:

```text
instance repository
canonical upstream
package source version
host adapter
bridge template currently available in the package
configured bridge template provenance, when known
configured bridge repository target, when known
configured bridge raw-byte digest
operator-reported host-installation state
operator-confirmed installed bridge raw-byte digest + target/provenance snapshot, when known
source-contact observation
```

Its bridge-template relations are intentionally split:

```text
available_bridge_template_version
  what the current package offers

configured_bridge_template_version
  what template is known to have produced the preserved configured bridge
```

A legacy configured bridge can predate the receipt that records this relation.
When its template origin cannot be established from evidence, the configured
provenance is `unknown`. That state is valid: it makes uncertainty visible
instead of assigning the current package template retroactively.

A standard configured bridge also carries the user-owned repository it reaches.
That bridge target and `INSTANCE.instance_repository` should describe the same
continuity owner. Ordinary migration refuses a known mismatch before writes;
validation can expose one created later by manual/customized drift.

`host_installation.installed_bridge_sha256` is different again. It records the
raw-byte digest of the configured bridge that the operator last confirmed as
copied and saved in ChatGPT; repository target and template provenance are
snapshotted alongside it when known. The repository cannot inspect the host
directly, so this remains an attributable operator report, not independent host
proof.

Its presence proves configured/persisted instance metadata only. It does not
prove connector reachability, host behavior or assimilation.

### `state/CURRENT.md`

Owns the user's current relation/context and the smallest causal margin needed
for reentry. It does not own reusable kernel methods or package-installation
metadata.

### `state/SOURCES.md`

Owns owner-native source pointers and why they may change the result. It is not
an activation registry.

## Selective reentry

The default relation is direct work. Reentry begins only when a missing durable
relation can change the result.

```text
current work
-> missing user/context relation:
   state/CURRENT.md + pertinent source pointer

-> missing kernel/method/maintenance relation:
   AGENTS.md + pertinent owner

-> unfinished causal/effect relation:
   operations/ when material

-> package/bridge/source-contact question:
   state/INSTANCE.json when material

-> current result
```

These are alternatives made pertinent by the work, not a required boot
sequence. Reading a representation first can frame interpretation without
making it authority.

## Portable entry and host adapter

The provider-neutral portable template is the constitutive host entry. It
carries kernel-source identity, the owner paths needed to enter the kernel,
competence participation and learning return without copying the whole kernel
into host instructions.

The entry does not classify the receiving AI by modality. A chat, voice or
multimodal interface, tool-using host or another future surface can carry the
same kernel relation when it can retain the operating entry and reach the
persistent kernel source. The modality is an incarnation of the carrier, not
its identity.

The kernel therefore does not need every evolving process relation to be
hard-coded as an external workflow. Competence formation/composition,
source-aware understanding, in-flow correction, learning return and parts of
process evolution can live in semantic owners and be re-formed in the present.
Actual execution facilities remain receiver-native means and preserve their own
authority and evidence boundaries.

The ChatGPT adapter renders that same source into a host-specific configured
artifact and owns only ChatGPT delivery/receipt mechanics.

The following are distinct incarnations/evidence states:

```text
portable semantic owner
!= portable instruction template currently available
!= host adapter mechanics
!= configured local bridge + known/unknown template provenance + source target
!= operator-confirmed installed bridge incarnation receipt
!= instructions actually present in the host
!= observed host behavior
```

The package exposes a bridge-template version because package evolution does not
always change the host entry contract. The configured bridge has a separate
provenance relation because preserving an existing local bridge does not prove
that it was generated from the currently available template.

A package/instance refresh may advance the available template identity while
leaving configured-bridge byte identity and provenance untouched. It can observe
drift without accepting it. An explicit bridge replacement uses the current
template and can therefore establish configured byte identity, target and
provenance; for an existing instance it does not migrate the instance repository.
It still does not change the installed ChatGPT instructions.

When a configured bridge is delivered, its raw-byte digest becomes the
correlation identity for that operator handoff. A later
`--confirm-host-installation --expected-bridge-sha256 ...` snapshots the
operator report only when that delivered incarnation is still the current
configured bridge. A late confirmation cannot be transferred from A to B. The
command does not repair drift or inspect ChatGPT; the last confirmed host
incarnation remains distinct until another attributable confirmation.

## Semantic relation and operational incarnation

A semantic relation can be made persistent through a bridge, state object,
guard or another receiver-native mechanism. The mechanism is not the semantic
owner and does not inherit authority over effects.

```text
semantic relation
-> receiver-native representation/incarnation
-> actual authorized effect when selected
-> observed consequence
-> readback can preserve / revise / retire the incarnation
```

Enough source identity, transformation lineage and consequence should remain
reachable to notice when a persistent projection has become stale relative to
its living owner.

## Situated observation

Source observation, transformed representation and situated semantic relation
are not interchangeable. When the distinction can change meaning, preserve the
minimum observation frame needed to avoid false co-reference: relevant source
or observer, time/locality, medium/representation, transformation, uncertainty
and ownership.

This is a semantic relation, not a required universal metadata schema.

## Mobile observation and proof relation

The kernel can preserve the point being understood while moving observation
through another material relation when the current frame may itself be the
limit. The alternative observation can be source-, scale-, owner-,
representation-, consumer-, transformation- or consequence-relative; no
fixed set is required.

```text
stable point
+ materially different observation
-> return to the same point
-> changed relation | no_change
```

Evolution applies the same principle to proof. A claim and the evidence used
to support it remain distinct; implementation, validator and tests can agree
because they inherited the same assumption. When that difference matters,
owner-native identity or execution surfaces supply a falsifiable observation.

This is a distributed semantic faculty, not an additional runtime component or
review controller.

## Competence field

The kernel does not ship a closed capability taxonomy. A user-owned instance
may point to competences, metacompetences, guides or context-specific methods.
They participate when the present relation makes them useful and the host can
actually reach them.

Results can make another competence pertinent, form a temporary composition or
expose a consequence that revises an earlier method. Reusable learning lives in
the affected owner; CURRENT/SOURCES preserve the current reentry implication
and pointer when needed.

## Situated movement, choice and self-observation

The Core can recognize a situated movement from the present relation, still-
valid determinations, materially pertinent possibilities, reachable means and
enough consequence awareness to distinguish alternatives. Competence supplies
capability-specific resultants such as use/preserve, compose, adapt/deepen,
form, defer/unknown and `no_change` without a central chooser or fixed ranking.

FDLA lets the system notice when its own interpretation is acting as an
unjustified limit and also when a later consequence changes what the present
can now understand about an earlier relation. It preserves real invariants and
present limits while revising interpretation-introduced closures; in the
consequence-aware case it preserves the event, the understanding actually
available then and the understanding available now without retroactive
narration or historical freezing. It is not a second workflow before ordinary
work.

## Operational continuity

When losing a cursor, pending relation, result or effect receipt would change
continuation, the optional [`operations/`](../operations/) organ preserves the
smallest causal state needed to resume. Execution facilities remain those
actually exposed and authorized by the receiving environment.

## Effects

The following facts remain orthogonal:

```text
useful action
host capability
source access
target ownership
current authorization
```

An adapter can represent these distinctions; actual capability, access,
ownership and authorization come from the receiving environment and operator
relation.

## Extension

A receiving environment can adopt the portable entry directly through its
native persistent-instruction and source mechanisms.

When a host-specific adapter is useful, it should define:

- the host's real persistent-instruction surface;
- how the host reaches user-owned state;
- what it can read or write in the current interaction;
- how a user verifies reentry;
- which receiver-specific mechanics it packages.

The core remains open to evolution when another host exposes a relation that
the current form cannot yet represent without loss.
