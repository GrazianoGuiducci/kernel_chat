# kernel_chat — current state

## Source 0.6.0 — 2026-09-18

```text
version: 0.6.0
status: canonical_kernel_chat_incarnation
review_state: external_rereview_complete_no_change
material_review_target: 2c111f2797a7ffe945067ac4b6eee8baace7c9c9
material_review_ci: 35390696891
release_promotion: published
release_promotion_commit: d2c94ca4e4523f1f7a343601d6beec1e84031fac
latest_tagged_distribution: v0.6.0
release_url: https://github.com/GrazianoGuiducci/kernel_chat/releases/tag/v0.6.0
release_readback_date: 2026-09-18
owner: Graziano Guiducci
```

This state describes the current canonical source in `GrazianoGuiducci/kernel_chat`.
Source publication is distinct from a numbered tag/release, user-instance
migration and ChatGPT host activation.

## Object now

`kernel_chat` is a **user-owned continuity kernel** for cloud chats and small
conversational systems that do not own a durable workspace.

The kernel instance can exist before any project is selected. A project can
later become one current context and source relation without becoming the
identity of the kernel itself.

ChatGPT is the first implemented host adapter. GitHub is the first implemented
persistence surface. Neither is the identity or future limit of the portable
core.

## Current package relation

Keep these surfaces distinct:

```text
canonical distribution
!= user-owned instance
!= configured host bridge
!= operator-confirmed installed bridge incarnation
!= repository reachability
!= situated conversation / exercised behavior
!= later behavioral assimilation
```

For non-public continuity, the documented default is a **private standalone
user repository** initialized from an identified public source/release. A
normal fork of a public GitHub repository remains public and is appropriate
only when public continuity is intended.

## User-owned state

The package separates three durable state owners:

```text
state/INSTANCE.json
  instance / package / bridge identity
  + operator-confirmed installed bridge observation
  + source-contact observation

state/CURRENT.md
  current user relation or context

state/SOURCES.md
  owner-native sources and why they may change the result
```

Operational cursors, requests/results, effect receipts and recovery remain in
the optional `operations/` organ when they are materially needed.

`INSTANCE` does not prove that ChatGPT Custom Instructions were installed,
that the repository is reachable from a host, or that later behavior assimilated
the kernel relation. An installed bridge digest is explicitly operator-confirmed
evidence, not direct host inspection.

## Temporal owner integrity

`state/INSTANCE.json` is a single semantic owner even when several cooperating
tools can reach the same filesystem. Mutating configurator commands therefore
acquire a transient exclusive writer lock **before reading INSTANCE** and hold it
through publication. The lock serializes cooperating local writers; it does not
pretend to make every external repository/API writer transactional.

```text
single-file atomic replacement
!= concurrent update preservation

visible writer lock
-> one cooperative INSTANCE writer at a time
-> conflict is surfaced instead of silently losing a later observation
```

If a process stops unexpectedly, the lock may remain. Recovery is deliberately
conservative: inspect the lock and current INSTANCE, establish that no writer
still owns it, then remove the stale lock and continue from actual state. The
kernel does not auto-delete evidence of uncertain ownership.

## Adoption and receiver fit

The product now distinguishes the **semantic adoption contract** from one
particular setup mechanic.

```text
user intent
+ receiver environment
+ available persistence
+ executable means
+ current authority
-> receiver-relative onboarding
```

The supported reference path remains Git + Python 3.11–3.14 and
`scripts/configure.py`. A capable model/coder may perform those effects for
the operator through an authorized local or remote execution surface; an
unavailable capability becomes an explicit operator step rather than a
simulated success.

`kernel_chat` remains aimed at cloud-chat continuity where the chat does not
own a durable workspace. A receiving AI/coder already operating inside a
persistent local or remote project filesystem is normally better matched by
MAIOS Project Kernel. This is product fit, not a restriction on what filesystem
can host the reference configurator.

Keep these capabilities distinct:

```text
GitHub read
!= GitHub repository creation / write
!= filesystem / terminal access
!= Python execution
!= ChatGPT account-setting authority
```

The irreducible operator boundary for the current ChatGPT adapter remains
saving the configured Custom Instructions and controlling account/credential
consent. Repository-side automation does not upgrade itself into host-setting
authority.

## Configuration and bridge

The configurator supports both:

```text
kernel instance / no active project
kernel instance + initial project/context
```

Supplying only one of `--project-name` / `--project-source` is rejected before
owned-file mutation.

The ChatGPT bridge has its own template version under
`adapters/chatgpt/VERSION`. It is intentionally smaller and more stable than
the package it reaches.

The package distinguishes these relations:

```text
available_bridge_template_version
  bridge template offered by the package currently present

configured_bridge_template_version
  template version known to have produced the preserved configured bridge

configured_bridge_sha256
  digest of the current local configured bridge recorded by INSTANCE

host_installation.installed_bridge_sha256
  digest of the bridge the operator last confirmed as copied/saved in ChatGPT
```

A legacy 0.5.x instance can already have a configured bridge before
`state/INSTANCE.json` exists. The 0.6 configurator preserves that bridge and can
record its digest, but it does not invent its template origin. When provenance
cannot be established, it records:

```text
configured_bridge_template_version = unknown
```

That state is valid and produces a reconciliation warning rather than a
structural failure.

A standard 0.5.x bridge also embeds the user-owned repository it reaches. If a
preserved bridge names a repository different from the instance being formed,
configuration now stops before writes. This prevents a truthful `INSTANCE`
identity from being paired with a bridge that would reenter another continuity
owner.

```text
package source update
!= bridge template currently available
!= configured bridge template provenance
!= configured bridge repository / bytes
!= operator-confirmed installed bridge incarnation
!= actual host behavior
```

`--refresh-instance` refreshes package identity and the available bridge-template
version while preserving configured-bridge provenance, source-contact and
operator-owned observations. `--replace-adapter` regenerates the local bridge
from the current template, can therefore establish its configured-template
provenance, and marks the local/host relation unconfirmed until the operator
separately updates ChatGPT through the UI.

When the configured bridge is delivered, the emitted
`confirmation_bridge_sha256` identifies that handoff. After the operator
copies/saves it, `--confirm-host-installation --expected-bridge-sha256 ...`
mutates `INSTANCE` only if that delivered incarnation is still current. A late
confirmation cannot promote a newer bridge. A later local replacement preserves
the previously confirmed installed digest/date but does not resurrect a
confirmation whose current host state was explicitly invalidated or unknown.

## Rereview consumer convergence

The rereview of the previous canonical resultant found four local seams rather
than a new architectural problem. The current source carries the already-known
relations through the consumers that had not yet inherited them:

```text
generated onboarding action
-> includes the exact delivered bridge digest required by the confirmation API

AGENTS adoption path
-> receipt publication + fresh remote readback owner
-> only then remote/new-chat reachability

active discovery route
-> active explicit anchor
-> intended rendered owner heading
  all observed on one consumer surface

local bridge drift
-> diagnostic local digest
!= delivery-authoritative confirmation digest
-> host copy/save remains blocked until reconciliation
```

The reference implementation therefore exposes unresolved local drift **before**
the host effect instead of offering an artifact that the same configurator
would later refuse to confirm. This adds no new state machine or controller;
it lets the present model/operator resolve the visible conflict at the seam
where it exists.

## Final rereview convergence

The latest rereview found no regression in the architecture or in the previously
reconciled mechanics. One remaining proof seam was local to the CommonMark
consumer oracle: its event projection could discard rendered content between a
constitutive anchor and the intended owner heading. The oracle now preserves
that intervening content as a material event, so only an anchor whose next
relevant rendered event is the intended heading satisfies the composed owner
relation.

Current onboarding shorthand also names the complete host-confirmation effect:
`--confirm-host-installation` is paired with the delivered bridge digest through
`--expected-bridge-sha256`. These changes refine proof and delivery wording;
they do not change INSTANCE, bridge, host or kernel architecture.

## Portable semantic deepening
The package preserves a deeper distinction across sources and incarnations:

```text
source observation
!= transformed representation
!= situated semantic relation

semantic relation
!= persistent operational incarnation
!= effect authority
!= actual effect
!= observed consequence
```

When losing observation frame changes meaning, preserve only the smallest
source/time/locality/medium/transformation/uncertainty/ownership relation needed
to avoid false co-reference.

A persistent bridge, state object or other operational form can become stale
relative to its living semantic owner. Evolution therefore follows the causal
path to the **first transformation that loses or alters a required relation**
instead of patching only the place where the loss becomes visible.

The bridge provenance and host-receipt cases are concrete exercises of this
relation: the package can know what it offers and what local bytes exist without
being entitled to rewrite which repository the preserved bridge reaches or
which exact bytes the operator last confirmed in the host.

This adds no daemon, semantic-hook runtime, global controller, fixed competence
taxonomy or automatic synchronization.

## Situated movement and capability selection

The package makes explicit a relation that was previously distributed across
Core, Competence, FDLA and Evolution:

```text
present relation
+ still-valid determinations
+ materially pertinent possibilities
+ reachable competence / means
+ enough consequence awareness to distinguish the alternatives
-> situated movement
```

The movement can resolve to:

```text
use / preserve
compose
adapt / deepen
form the smallest continuing owner
preserve unknown / defer
no_change
```

These are possible resultants, not an ordered decision pipeline or a central
chooser. The kernel does not invent an optimum when several materially
different movements remain genuinely open. It preserves the difference until
another source, consequence or operator determination changes the field.

The corresponding competence relation prevents both false novelty and false
conservatism: do not create a new capability merely because a new name or
possibility appears, and do not preserve an existing owner merely because it
already exists when the present relation shows that its capability is no longer
sufficient.

## Mobile observation and pre-closure claim/proof sensing

The package carries a further portable relation formed during its own
development. A point can remain determined while observation moves through a
different causal position when the current frame itself may be hiding a
material relation.

```text
point / object remains
+ current frame may be limiting what can be seen
-> move observation through a pertinent different relation
-> return to the same point from the changed field
-> changed resultant | no_change
```

This can involve source, scale, time, owner, representation, consumer,
transformation or consequence without becoming a required list of viewpoints.
Competences can exercise the same movement when their own method becomes the
limiting frame.

Evolution also distinguishes a stronger claim from stronger proof. A green
result is not sufficient when implementation, validator, tests or prose share
the same assumption. Material claims can be checked from an independent
owner-native surface: an external version label against its native tag/ref,
documented test counts against discovered execution, or a declared matrix
against jobs actually run.

The current workflow exercises this directly: `actions/checkout` v7.0.1 and
`actions/setup-python` v7.0.0 are pinned by immutable SHA and each declared
tag resolves owner-native to that exact commit; both action revisions use
Node 24.

This adds no standing reviewer, second model or mandatory audit phase. The
movement becomes pertinent only when another observation can materially change
the result.

The operating entry now also keeps explicit AGENTS discovery routes to Core mobile observation and Evolution closure convergence, so the bridge can select these capabilities from their material conditions rather than merely knowing that their owner files exist.

Evolution also carries **closure convergence**: after a material correction,
the corrected local line is not by itself the closed result. The new candidate
must reconcile the proof, consumer/reachability, current-state and descriptive
surfaces whose truth changed with it, then stop when another pertinent
observation with a real chance to disagree returns `no_change`.

## Competence and FDLA relation

The current target already carried substantial competence formation and
circulation, so no new competence subsystem was introduced. Competences can be
selected, composed, formed and evolved from intent, knowledge, memory,
successful work, possibility or a gap; downstream consequences can revise an
earlier owner without a central dependency graph.

FDLA remains the situated correction of closures introduced by the acting
interpretation. It is not a mandatory preliminary workflow and does not grant
authority over external effects.

## Source contact and evolution

Source-contact policy remains in `AGENTS.md`; durable observation can remain in
`state/INSTANCE.json`. The policy is reachable when useful rather than repeated
inside always-hot Custom Instructions.

A newer upstream source is a possibility to inspect, not an update command.
Package state, configured bridge, installed host instructions and user-owned
learning remain separately selected effects.

The validator exposes package/bridge/instance drift as warnings when structure
is still valid. It exposes unknown configured-template provenance, configured
bridge repository mismatch, configured-byte drift and configured-vs-last-
confirmed-host digest drift without silently reconciling them.

## Evidence boundary

Repository validation and tests can establish package mechanics only. They do
not establish:

- installation in a particular ChatGPT account independently of operator report;
- GitHub connector availability in a specific turn;
- real conversational behavior;
- later non-identical assimilation;
- autonomous self-evolution or AGI.

The current regression suite contains **58 cases**: 38 configurator cases, 17
structural/receipt/drift/provenance/delivery validator cases, and 3 independent
CommonMark consumer-oracle cases. It includes a source-bound real 0.5.3
migration shape, custom/unknown legacy identity, repository-target match and
mismatch, raw-byte LF/CRLF discrimination, additive v1 receipt compatibility,
refresh/replace/confirm effect separation, missing-local-bridge preservation,
operator-confirmed digest/target/provenance snapshots, and configured-vs-
installed drift reporting. CI runs the validator and full suite on every declared supported Python line
(3.11, 3.12, 3.13, 3.14) across Ubuntu and Windows. Repository proof belongs to the exact canonical source revision being evaluated.

## Source relation and lineage

The package continues the public Meta Semantic Kernel lineage and retains
portable relations developed through the ChatGPT kernel, KA, Meta_Skill and
FDLA. Later MPK/SSK work contributed causal and semantic distinctions through
the evolved ChatGPT source; those systems remain separate owners and are not
runtime dependencies of `kernel_chat`.

See `docs/LINEAGE.md` and `docs/EVOLUTION_GUIDE.md`.

## External review before release

The first external review of `2c816975...` produced ten findings. The rereview
of `1a0720fa...` confirmed nine previous material defects closed, kept F06 open
at the semantic Markdown-consumer boundary, and added N1 (preview/schema
composition) plus N2 (delivery-proof quality).

The current canonical source reconciles those three remaining relations:

```text
R1 / F06
  runtime validator stops claiming arbitrary Markdown parsing
  + explicit structural discovery routes remain dependency-free
  + independent CommonMark test oracle owns consumer-surface link semantics

N1
  --preview-adapter renders/returns before INSTANCE interpretation

N2
  documentation regression proves ordered
  confirm -> add -> commit -> push -> remote readback -> reentry
```

A further rereview of `82078ed2...` found no reopened runtime/product defect,
but exposed three proof gaps in that oracle: raw-HTML anchors were outside the
token-only link observation, discovery evidence could be individually true
without proving that the fragment reached a real owner heading, and the
transitive parser dependency was not pinned exactly. The current resultant
therefore strengthens proof without widening the runtime validator:

```text
rendered consumer HTML
-> Markdown links + raw-HTML anchors observed on one surface

constitutive discovery
-> active AGENTS link
+ destination
+ one explicit prefixed custom anchor adjacent to the intended owner heading

test oracle identity
-> markdown-it-py 4.2.0
+ mdurl 0.1.2
```

The current source carries 58 tests across all 8 supported Python/OS jobs.
Five new configurator regressions cover writer-lock conflict/recovery,
confirmation validity, delayed bridge confirmation, literal template-like user
data and conservative custom-bridge attribution. Canonical proof must belong to the exact revision being rereviewed;
branch proof and prior reviewed SHAs remain genealogy/evidence for their own
identities.

## Review closure and release promotion

The external rereview reached `no_change` on the exact material resultant:

```text
reviewed material SHA:
  2c111f2797a7ffe945067ac4b6eee8baace7c9c9

canonical CI:
  35390696891
  validator valid=true / errors=[] / warnings=[]
  58/58 tests
  8/8 Python 3.11–3.14 × Ubuntu/Windows
```

That review result belongs to the reviewed material SHA. The present
promotion-only source transition records the closure; it does not retroactively
claim that administrative metadata was part of the material rereview.

Release promotion was published and read back through the GitHub UI on
2026-09-18. `kernel_chat v0.6.0` is the latest release, not a prerelease; its
tag resolves exactly to `d2c94ca4e4523f1f7a343601d6beec1e84031fac`.
The release notes preserve the material-review and promotion identities.
This post-release state update is administrative evidence of publication,
not a transfer of review or CI proof to a later source revision.

```text
promotion-only canonical revision:
  d2c94ca4e4523f1f7a343601d6beec1e84031fac
-> v0.6.0 tag / GitHub Release published
-> fresh GitHub UI readback confirms exact tag target and Latest label

canonical source / release
!= automatic user-instance migration
!= configured bridge replacement
!= ChatGPT Custom Instructions update
!= repository reachability
!= exercised behavior
!= later assimilation
```

Existing user-owned instances retain their own state, local evolution,
configured bridge provenance and last operator-confirmed installed incarnation
until their owners select a migration or host-update effect.
