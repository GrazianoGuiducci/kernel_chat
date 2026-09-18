# kernel_chat operating instructions

Work from the present. If the current request and working set are sufficient,
act directly.

Read root `CURRENT_STATE.md` only when package-maintenance state can materially
change the result. User continuity and operating knowledge use distinct
selective paths below; neither requires package state first.

Keep distinguishable:

- operator or owner source;
- evidence;
- inference;
- a representation introduced by the acting system;
- unknown or contradiction;
- host capability;
- authority over a material effect.

## Study and adoption are different

Reading or evaluating this repository does not install `kernel_chat`, create a
user instance, connect GitHub, or change ChatGPT settings.

When adoption is selected, the user-owned persistence surface may be a public
fork or a private standalone repository initialized from an identified
upstream source. A project is optional; the instance can exist before any
project is selected.

See [the adoption guide](docs/ADOPTION_GUIDE.md) for the supported distinctions.

## Adoption boundary

When the selected work is adopting or updating `kernel_chat` for an operator,
repository-side configuration is not ChatGPT host activation.

As soon as `scripts/configure.py` has produced
`adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md`, tell the operator
immediately that a manual ChatGPT UI action is required:

1. open the configured instructions file;
2. copy its complete text into ChatGPT Custom Instructions through the ChatGPT UI;
3. save the instructions and confirm that this host-owned step was completed.

The coder may continue repository-side setup, but until the operator confirms
that UI action, report the state as `repository configured / host activation
pending`. Do not report `kernel_chat` as installed or active in ChatGPT merely
because the repository, configurator, tests, or connector setup succeeded.

When the operator confirms the UI copy/save and repository writing is available,
record that exact observation with:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --confirm-host-installation
```

This receipt does **not** perform or independently verify the host action. It
binds the operator confirmation to the raw-byte SHA-256 identity of the
already-reconciled configured bridge and snapshots its repository
target/template provenance when known. If local bytes differ from the persisted
configured receipt, confirmation stops instead of accepting the drift. If the
receipt cannot be persisted, keep the host confirmation as an operator report
and do not claim that `INSTANCE` records it.

After operator confirmation, verify host reachability when that verification is
selected: a new chat should be able to reach the configured user state and,
when needed, the pertinent kernel owner. Reachability is evidence of access,
not proof of behavioral assimilation. Never simulate or claim a host UI action
the current tool surface cannot perform.

This boundary applies when adoption or host update is actually selected; it is
not a mandatory interruption of ordinary kernel work.

## Instance, state and sources

When the distinction matters, keep these user-owned surfaces separate:

```text
state/INSTANCE.json
  package/instance/bridge identity and source-contact observation

state/CURRENT.md
  current relation or context; a project can be one context but is not required

state/SOURCES.md
  owner-native sources and why they may change the result
```

`INSTANCE` is not project/user knowledge and is not proof of host installation.
Its configured receipt can preserve raw-byte identity plus repository
target/provenance; its `host_installation` object can preserve an
**operator-confirmed** installed incarnation snapshot. Those remain reported
evidence, not direct inspection of the ChatGPT UI. Older valid v1 receipts may
lack the newer optional semantic-identity fields. `CURRENT` is not an automatic
task queue. `SOURCES` is not a catalogue of active competences.

For a missing user/context relation, use `state/CURRENT.md` and its pertinent
source pointers. For a missing kernel or method relation, use only the owner
needed:

- [Core](kernel/KERNEL.md): understanding sources, representations and context,
  situated movement, and mobile observation when the point remains but the
  current frame may hide a material relation;
- [Competence](kernel/COMPETENCE.md): use, formation, circulation and cultivation;
- [Evolution](kernel/EVOLUTION.md): learning ownership, reentry, source return,
  pre-closure incongruence sensing, and closure convergence after a material
  correction;
- [FDLA](kernel/FDLA.md): correction of an interpretation that closes the field;
- [Operations](operations/CURRENT.md): unfinished effects and recovery, when material.

These are selective reachability paths, not a loading order. A new conversation
alone does not require a boot. A state, instruction or prior solution read
first can frame interpretation without becoming authority: understand its
function in the present before letting its form prescribe the method.

## Source contact and evolution feedback

The canonical upstream is
[GrazianoGuiducci/kernel_chat](https://github.com/GrazianoGuiducci/kernel_chat).
It supplies source updates and receives approved feedback; the user-owned
instance owns the user's continuity state.

When source freshness can change the work, inspect `state/INSTANCE.json` first
when available. Its `source_contact` fields can retain the last observed
revision/time and whether a material delta was seen. That state is an
observation aid, not a scheduler or automatic update command.

During active use, if the last known upstream check is about seven days old, or
if the current problem could plausibly have been corrected upstream, inspect
canonical upstream `main` and the smallest relevant version/release/source
surface. The seven-day relation is a light suggested cadence during active use,
not an ontological rule or background timer.

A newer source is a possibility, not an update command. Do not automatically
pull, merge, replace configured instructions or change the host. Surface only a
material delta and let the operator select any adoption effect.

Package source version, bridge template currently available, configured bridge
provenance/target/raw bytes, operator-confirmed installed incarnation and actual
host behavior are different relations. A package refresh may observe local
drift but does not accept it. Bridge replacement does not migrate an existing
instance repository identity. A package update does not require a host UI update
when the bridge contract did not change.

A command that mutates or refreshes an existing INSTANCE must use that
INSTANCE's repository identity. Supplying another repository is not an implicit
migration. A no-write `--preview-adapter` may inspect another target without
rebinding the instance.


Real testers are part of the evolution field. After a first meaningful use, or
when later use exposes informative friction, failure, unexpected success,
missing context or a new possibility, prepare a compact Evolution Feedback when
that evidence could improve upstream. Ask the operator before public
submission. With consent, use a GitHub Issue for observed feedback; use a
focused fork and Pull Request for a concrete public-source change. Do not grant
an external tester direct write authority over upstream `main` by implication.

Do not emit feedback merely to satisfy a cadence. Preserve an observation only
when it changes future understanding, behavior, safety, usability or attainable
results.

## Operating relation

Let relevant competences and metacompetences participate because the present
relation calls for them. Do not treat the current catalogue, schema, adapter,
host, or first plausible answer as the limit of what can emerge.

When more than one materially different movement remains open and the
difference can change the result, reach the [Core situated-movement
relation](kernel/KERNEL.md#situated-movement) and the [competence
field](kernel/COMPETENCE.md#movement-through-the-competence-field) only as far
as needed. Possible resultants include use/preserve, compose, adapt/deepen,
form, preserve unknown/defer, and `no_change`. They are not a checklist or a
central ranking system. If the present field already determines the movement,
do not reopen it merely to enumerate alternatives.

If the acting interpretation is narrowing the field on behalf of the sources,
use `kernel/FDLA.md` to inspect and revise that closure. This is not a mandatory
workflow and does not delay direct work when the field is already sufficient.

If the point or object remains stable but the current frame may itself hide a
material relation, use [Core mobile observation](kernel/KERNEL.md#mobile-observation-without-losing-the-point) only as far as another causal or identity
position can change the result.

If a material correction creates a new resultant, use [Evolution closure convergence](kernel/EVOLUTION.md#converge-the-changed-resultant) to reconcile only the
proof, consumer/reachability, state and descriptive surfaces whose truth changed
with it. The previous green result remains evidence for its own revision.

Constitutive discovery routes are also stated as stable owner paths so runtime
validation does not need to emulate a full Markdown renderer:

- `kernel/KERNEL.md#mobile-observation-without-losing-the-point`
- `kernel/EVOLUTION.md#converge-the-changed-resultant`

When repository/package work forms a stronger claim, keep claim identity and
proof identity joined before calling the result closed. Human labels and
comments are representations, not authority.

```text
local version/comment
!= owner-native tag/ref

immutable revision
!= correctly attributed version provenance

green CI
!= proof that a dependency label names the executed revision

documented test count
!= discovered / executed tests

declared matrix
!= jobs actually created and completed
```

For an external dependency pinned by SHA and annotated with a version/tag,
resolve the dependency owner's native ref and verify that it reaches the
pinned revision. Follow an annotated tag to its commit when necessary. Inspect
the artifact/action at that exact revision when runtime compatibility is part
of the claim. For current package counts or status, prefer native execution
evidence over copied prose.

This is an instance of [Evolution's pre-closure incongruence sensing](kernel/EVOLUTION.md#sense-incongruence-before-closure), not a mandatory
preflight for unrelated work.

Never simulate a filesystem, hook, background process, scheduler, connector,
or authority that the current host does not expose. Resolve authority only for
an exact material effect, when that effect appears.

Preserve a change only when it improves future behavior, proof, recovery, or
reentry. Prefer the smallest truthful owner. Storage alone is not evidence of
assimilation.

Do not manufacture test environments or fixed taxonomies before real use
exposes a discriminant that matters. Structural validation supports the
package; it does not certify host behavior.
