# Package evolution guide

This guide carries accumulated reasons for package maintenance. Read it when
evolving this package or resuming that work; ordinary chats use the pertinent
owners reached from [AGENTS.md](../AGENTS.md). The living method is owned by
[Evolution](../kernel/EVOLUTION.md), not by a release receipt.

## Current reconciliation — 2026-09-17

Starting public baseline:

```text
canonical kernel_chat main:
  bb3f3fd7ef311d664832f2002f16872fed9723af

source version:
  0.5.3

latest tagged distribution:
  v0.5.0
```

The reconciliation reread source, package, bridge, state and
documentation relations as one system while preserving the canonical
repository as the publication owner.

Source selection followed causal relevance to the target. Current public owners
and accepted product determinations remained authoritative; later source work
contributed only when its relation could survive receiver change and become
owned coherently by `kernel_chat`.

Recency, naming or source sophistication did not confer authority by
themselves.

### First pass — what was actually missing

The target already carried much of the evolved kernel function:

```text
present-first work
selective reentry
situated competence composition
competence formation from intent/knowledge/memory/success/possibility/gap
downstream correction without a central controller
receiver-relative external learning
FDLA self-correction
owner-native evolution
no_change as a valid result
```

The material product debt was instead concentrated in two places.

First, the package still exposed a project-first adoption shape even though the
selected product identity had moved toward a user-owned continuity kernel.
`configure.py`, state templates and documentation still required an initial
project and treated a fork as the default user-owned form.

Second, later semantic work had deepened relations not yet explicit enough in
the portable core:

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

### Second pass — owner placement

The repeated pass exposed one important causal gap: source-contact state could
be represented in a new instance receipt but would remain ineffective unless
the maintenance entry actually reached it.

That changed the design from “add source-contact metadata” to:

```text
state/INSTANCE.json owns durable source-contact observation
AGENTS.md owns when that observation becomes pertinent
configured bridge stays small and does not carry the source-contact policy
```

This is a concrete example of the new Evolution relation: a function is not
complete merely because it was represented. Follow formation -> representation
-> delivery/entry -> consumer -> exercise far enough to find the first place
where the relation is lost or altered.

The same pass justified `INSTANCE` as a distinct owner rather than placing
installation/update metadata in CURRENT, SOURCES or operations:

```text
INSTANCE
  package / instance / bridge / source-contact observation

CURRENT
  user current relation/context

SOURCES
  owner-native domain/project/competence sources

operations
  unfinished causal/effect continuity
```

### Implemented development verticals

The development candidate provides:

- valid configuration with no initial project;
- project-first configuration as an optional paired input, not a requirement;
- `state/INSTANCE.json` with package, bridge, host-installation and source-contact
  observation responsibilities;
- separate root package version and ChatGPT bridge-template version;
- a smaller stable Custom Instructions bridge;
- source-contact/evolution policy removed from the always-hot bridge and kept
  in owner-native repository knowledge;
- bridge replacement that marks host installation unconfirmed instead of
  pretending the ChatGPT UI changed;
- `--refresh-instance` for package/bridge identity refresh without replacing
  user context;
- contract-oriented validator/tests rather than literal prose checks such as
  the presence of `seven days` in Custom Instructions;
- observation-frame / transformation-lineage continuity in KERNEL;
- semantic owner / persistent incarnation / effect / consequence distinction;
- first-losing-transformation diagnosis and owner/incarnation drift readback in
  EVOLUTION;
- documentation that distinguishes study, private standalone instance, public
  instance, optional project/context, package update and host-bridge update.

The implementation verticals are exercised by the repository's validator and
regression tests on both Ubuntu and Windows. Those checks establish
repository/package behavior only. They do not prove ChatGPT installation,
connector reachability, model behavior or later assimilation.

### Third pass — legacy migration exposed bridge provenance

Whole-result refinement then tested the situation the candidate would actually
meet in an existing installation rather than only fresh 0.6 configuration:

```text
pre-0.6 user instance
+ state/CURRENT.md
+ state/SOURCES.md
+ preserved CUSTOM_INSTRUCTIONS_CONFIGURED.md
+ no state/INSTANCE.json yet
```

The first 0.6 form could preserve that bridge and compute its digest while also
recording the current package's bridge-template version. Those two facts were
true individually, but using one template-version field would imply a relation
that had not been established: that the preserved bridge was generated from the
currently available template.

The candidate therefore split the relation:

```text
available_bridge_template_version
  what the package currently offers

configured_bridge_template_version
  what template is known to have produced the local configured bridge

configured_bridge_template_version = unknown
  the bridge exists and is preserved, but available evidence does not establish
  its template provenance
```

This is not an error state. It is a truthful reconciliation state.

`--refresh-instance` can advance package identity and the available-template
identity without rewriting the provenance of a bridge it did not regenerate.
`--replace-adapter` is different: it generates the configured bridge from the
current template, so that exact effect can establish the configured-template
provenance while still leaving installed ChatGPT instructions unchanged until
an operator performs the UI update.

This pass sharpened a reusable maintenance rule:

```text
what an owner currently offers
!= what a persistent incarnation is known to embody
```

Do not infer lineage from adjacency, recency or availability. When an older
incarnation survives a package change, preserve `unknown` where necessary and
let validator/readback expose the reconciliation need rather than inventing a
history.

The regression suite at that point contained 16 cases, including legacy
migration and a validator case proving that unknown configured-bridge
provenance remained structurally valid while producing an explicit warning.

### Fourth pass — the capability existed, but the movement relation was implicit

A later review asked whether the kernel itself had inherited the way the work
recognized the appropriate movement rather than only the artifacts produced by
that reasoning.

The answer was partial: Core already preserved present-first work, valid
determinations, open possibility and effect authority; Competence already knew
how to use, compose and form capabilities; FDLA could remove an interpretation-
introduced closure; Evolution could reread consequences. What remained too
implicit was the relation connecting those functions **at the moment a
movement is formed**.

The candidate therefore made this relation explicit in the existing owners:

```text
present relation
+ still-valid determinations
+ materially pertinent possibilities
+ reachable competence / means
+ enough consequence awareness to distinguish alternatives
-> situated movement
```

Possible resultants include:

```text
use / preserve
compose
adapt / deepen
form the smallest continuing owner
preserve unknown / defer
no_change
```

This did **not** add a chooser, controller, score, ranking or mandatory decision
pipeline. `KERNEL.md` owns the general situated-movement relation;
`COMPETENCE.md` owns capability-specific responses; `AGENTS.md` reaches those
owners only when materially different movements remain open. FDLA and Evolution
retain their existing roles rather than being absorbed into a new selection
subsystem.

The word `smallest` was constrained deliberately: it means no more structure,
commitment or irreversible effect than the present relation requires while
preserving capability and relevant future possibility. It does not mean the
shortest text, fewest files or least ambitious outcome.

The same pass removed a stale `0.5.0` hardcode from the Core persistence
relation: the current ChatGPT adapter uses GitHub as the first implemented
persistence surface, but a historical source version does not belong as the
portable core's present identity.

### Fifth pass — receipt identity still stopped one relation too early

The final pre-canonical audit reread the candidate from its actual migration and
host-update transitions rather than from the intended model.

Two remaining gaps were found in the same causal chain.

First, a real 0.5.x configured bridge contains the user-owned repository it
reaches. The legacy test used a synthetic bridge without that identity, so the
candidate could form:

```text
INSTANCE.instance_repository = requested/current repository
```

while preserving a bridge that might still point to a different historical
repository. Both artifacts could be individually valid while the continuity
relation between them was false.

The configurator now recognizes the standard 0.5/0.6 bridge repository line.
During preservation, a known bridge target must agree with the instance identity
being preserved; a mismatch fails before writes. The validator can also surface
a mismatch introduced later by manual/customized state.

Second, `host_installation.state` could say that operator confirmation existed,
but the receipt did not identify **which configured bridge bytes** that report
referred to. There was also no normal configurator operation that persisted the
operator confirmation after the required ChatGPT UI step.

The candidate therefore added:

```text
host_installation.installed_bridge_sha256
```

and an exact effect:

```text
--confirm-host-installation
```

The command runs only after the operator says the current configured bridge was
copied/saved in ChatGPT. It mutates `INSTANCE` only and binds that report to the
current configured bridge digest. It does not inspect or perform the host UI
action.

When the local configured bridge is replaced later, the previous confirmed host
digest/date are preserved while the local/host relation becomes unconfirmed.
This keeps the old host incarnation reconstructible instead of erasing it when
the local projection advances.

The resulting relation is now:

```text
instance repository
-> configured bridge repository target
-> configured bridge bytes / provenance
-> operator-confirmed installed bridge digest
-> host reachability / behavior when later observed
```

Each arrow can now fail or drift without the next representation silently
repairing the history.

This pass also changed the reusable maintenance lesson:

```text
operator-reported effect
+ exact persistent artifact identity
-> reconstructible effect receipt
```

A statement that “the host was updated” is weaker than a receipt that records
which local incarnation the operator says was installed. Conversely, even that
receipt remains operator-reported evidence and must not be upgraded to direct
host inspection or behavioral assimilation.

At that earlier checkpoint the regression suite contained **20 cases**: 14
configurator and 6 validator/drift/provenance cases. The later sixth pass above
supersedes that evidence closure with the deeper 35-case field.

### What remains deliberately separate

No package source change automatically:

- creates or publishes a release;
- changes the canonical public repository;
- performs or independently verifies Custom Instructions changes in an account;
- proves GitHub connector access;
- updates another user's instance;
- proves semantic/behavioral assimilation.

Whole-result refinement selected **0.6.0** as the source candidate because the
change adds materially new instance/adoption/bridge capabilities while keeping
the product lineage compatible. A `v0.6.0` tag/release remains a separate
effect.

## Sixth pass — technical closure reopened by a changed observation frame

A later reader returned to the same green candidate without reopening its core
architecture. The point remained `kernel_chat 0.6.0`; the observation moved
around migration evidence, artifact identity, support claims and command
transitions. That lateral/recursive movement exposed relations that the earlier
frame had treated as equivalent.

The first closure had 20 green tests, but:

```text
representative legacy fixture
!= source-bound historical 0.5.3 shape

text decode -> encode -> SHA-256
!= raw-byte artifact identity

artifact digest
!= durable repository target / provenance

technical Python floor
!= deliberate supported/tested floor
```

The exercise then exposed a second layer:

```text
implementation + validator sharing one normalization
!= independent falsification

observe local bridge drift
!= accept it as configured state

--refresh-instance
!= configured artifact reconciliation

--confirm-host-installation
!= local receipt repair

--replace-adapter
!= existing instance_repository migration

requested replacement
!= material change by assumption

missing local bridge
!= permission to regenerate it during unrelated state/package work
```

The candidate was changed accordingly. Historical 0.5.3 bridge/CURRENT/SOURCES
fixtures are now source-bound to the canonical baseline and remain static/offline.
Byte-level LF/CRLF tests construct the bytes directly so Git checkout policy
cannot normalize away the discriminant.

`configured_bridge_sha256` and installed bridge digests now identify raw bytes.
New optional v1 fields preserve configured/installed repository target and
template provenance when known; older valid v1 receipts without those fields
remain readable. Host confirmation uses an offset-aware timestamp and snapshots
the already-reconciled incarnation rather than advancing local configured state.

Configurator effects were separated. Refresh can advance package/available-
template identity while leaving local artifact drift visible. Replacement
regenerates the configured incarnation but cannot silently rebind an existing
instance repository. If replacement results in the exact already-confirmed host
incarnation, host synchronization remains confirmed instead of manufacturing
drift. A missing local bridge remains missing during independent state/package
work until explicit replacement is selected.

The public support contract is now Python 3.11–3.14, with CI on every declared
Python line (3.11, 3.12, 3.13, 3.14) across Ubuntu and Windows. Checkout/setup
actions are pinned to immutable Node-24-compatible revisions.

The resulting suite contains **35 cases** (25 configurator + 10 validator /
drift / provenance) and is green across all **8 Python/OS matrix jobs**. This remains
repository/package evidence; host reachability, actual ChatGPT settings,
conversation behavior and later assimilation remain separate observations.

This pass changed the maintenance method itself: a coherent result can be
re-read by keeping the object fixed while moving observation through another
causal relation. Common-mode agreement can make implementation and verifier
confirm the same wrong assumption. The useful stop condition is therefore not
"another pass happened", but another observation changes no material relation.

## Seventh pass — the observation itself became an evolvable faculty

After the migration/artifact/transition field was green, one more safety pass
kept the candidate fixed and moved observation to the provenance of the CI
tools themselves.

The workflow contained:

```text
actions/setup-python@f8cf4291c8b8e273ddd26e569454615c7315d932 # v7.0.0
```

The pinned commit was real, immutable, Node-24-compatible and had already run
the full matrix successfully. But the dependency owner's native
`refs/tags/v7.0.0` resolved to:

```text
5fda3b95a4ea91299a34e894583c3862153e4b97
```

So several individually true facts still formed a false relation:

```text
valid immutable SHA
+ successful execution
+ Node-24-compatible action
!= correctly attributed v7.0.0 provenance
```

The workflow was corrected to the owner-native v7.0.0 commit and the full
Python 3.11–3.14 × Ubuntu/Windows matrix passed again. A following readback
then exposed another stale evidence surface: this guide still said `four`
matrix jobs although the actual matrix contains eight. That wording was
corrected and the resulting head was proved again.

This changed the portable kernel itself rather than only repository mechanics.
The useful relation is not a permanent final audit. It is the ability to keep
the object stable while moving observation to a different causal or identity
surface before the developing frame hardens around its own assumptions.

```text
point / object remains
+ current frame may hide a material relation
-> move observation through another pertinent relation
-> return to the same point
-> changed resultant | no_change
```

Core now owns that mobile-observation relation. Evolution owns pre-closure
incongruence sensing and common-mode proof limits. Competence can exercise the
movement inside its own method when that method becomes the limiting frame.
`AGENTS.md` carries the package-specific consequence: human version labels,
dependency tags, immutable revisions, discovered tests and actual matrix jobs
remain distinct proof surfaces.

No standing reviewer, smell detector, second model, score or mandatory
multi-angle checklist was added. The faculty becomes pertinent only when a
different observation can materially change comprehension, proof, method or
consequence.

## Eighth pass — closure convergence caught delivery drift

After mobile observation and pre-closure sensing had been integrated and the
candidate was green, another safety movement changed the observation from
semantic ownership to **delivery reachability**.

`AGENTS.md` contained the intended pointer to Evolution, but the Markdown had
been split as:

```text
[Evolution's pre-closure incongruence sensing]
(kernel/EVOLUTION.md#sense-incongruence-before-closure)
```

The owner existed and the anchor existed, yet standard inline-link parsing did
not treat that representation as a link. The package validator also missed the
error because its local-link check only observes already well-formed `](...)`
syntax.

This exposed another common-mode boundary:

```text
owner exists
+ target anchor exists
+ validator checks parsed local links
!= consumer can reach a malformed link representation
```

The link was corrected and the validator gained the smallest discriminant for
the observed malformed multiline inline-link shape, with a regression test.
The current-state date was also aligned from 2026-09-17 to 2026-09-18 because
the file claims to describe the current candidate rather than only its first
formation date.

The regression suite therefore advances to **36 cases**: 25 configurator and
11 validator/drift/provenance/reachability cases.

The broader lesson is **closure convergence**:

```text
material correction
-> new resultant / new candidate state
-> previous closure evidence is no longer sufficient by assumption
-> reconcile affected proof, consumer, state and descriptive surfaces
-> move observation through a position that can still disagree
-> material delta | no_change
```

Completion is not the first green local fix, nor an arbitrary number of
passes. It is the situated fixed point where materially dependent surfaces
describe and exercise the same resultant and another pertinent independent
observation adds no causal difference.

## Ninth pass — the discriminant had to match the consumer surface

The new malformed-link discriminant initially failed CI for the opposite
reason: it inspected code examples as though they were active Markdown links.
The Evolution Guide deliberately contains the broken form inside a fenced
historical example and also names the literal syntax `](...)` inline. Those
representations are not link consumers.

This exposed the inverse relation:

```text
more sensitive validation
!= more accurate validation

validation observation surface
must match
consumer surface relevant to the claim
```

The validator was refined to hide fenced code and inline code before link
reachability checks. The original malformed prose-link regression remains an
error, while a second regression proves that equivalent syntax inside code
examples remains valid.

The current suite therefore contains **37 cases**: 25 configurator and 12
validator/drift/provenance/reachability cases.

This also deepens closure convergence: a correction that introduces a new
discriminant must itself be observed for false positives and false negatives.
The fixed point is not maximal sensitivity; it is a discriminant whose
observation frame matches the consumer/effect whose integrity it claims to
protect.

## Tenth pass — capability presence was not yet capability discovery

After the consumer-surface validator converged, observation moved one step
earlier in the delivery path: the ChatGPT bridge reaches `AGENTS.md` and asks
it to select only the pertinent owner. Core and Evolution contained the new
faculties, but AGENTS still described their older perimeter.

```text
capability exists in owner
+ owner file is reachable
!= entry recognizes when that capability is the pertinent owner relation
```

The AGENTS owner map and operating relation were therefore deepened with two
explicit routes:

```text
stable point + limiting frame
-> kernel/KERNEL.md#mobile-observation-without-losing-the-point

material correction -> new resultant
-> kernel/EVOLUTION.md#converge-the-changed-resultant
```

The package validator now preserves these route targets as structural discovery
contracts while leaving explanatory prose free to evolve. A regression removes
the mobile-observation anchor and proves that the package becomes invalid when
the entry can no longer discover that owner relation.

The current suite therefore advances to **38 cases**: 25 configurator and 13
validator/drift/provenance/reachability cases.

This refines the earlier delivery relation:

```text
represented
!= reachable
!= discoverable from the condition that makes the capability pertinent
!= exercised
!= assimilated
```

## Previous movement — 2026-09-10

Starting source: `edf036187e90ca71cb5c579eec9f85280b911210`, version `0.4.0`.
The owner selected implementation and source publication of the conversational
kernel transfer. Account installation, a tagged release and website updates
were separate effects. The transfer was implemented as source version `0.5.0`.

The 0.5.0 transfer incorporated portable relations already developed through
earlier kernel work, including source-aware relational comprehension,
competence circulation and owner-local learning. Those relations are now owned
by the public kernel sources in this repository. Development-source genealogy
is historical evidence, not an operating dependency or a source that a receiver
must reach to understand or use kernel_chat.

### Decisions and their reasons

- Preserve present-first work. The old source adapter's automatic reentry on a
  greeting would regress selective continuation.
- Keep user/context reentry and kernel-method retrieval separate. User state
  owns current continuity; `AGENTS.md` reaches kernel owners without turning
  constitutive methods into state.
- Understand representations through function, source and current consequences.
  Regenerate a method in a changed situation while preserving still-valid
  determinations.
- Preserve competence circulation: a result can call another competence,
  produce a temporary composition, or expose a consequence that changes an
  earlier contributing method.
- Let formation arise from intent, acquired knowledge, memory, successful
  composition, possibility or a gap.
- Put reusable learning in the owner that must act differently. State keeps the
  reason and pointer needed for reentry.
- An unchanged source identity ends only inspection for new source changes.
  Pending integration, validation and return remain open until actually done.
- Preserve the configured local adapter by default. Template, configured file
  and instructions installed in an account are different surfaces.
- Add competence templates/directories only when actual use lacks a useful
  owner after existing knowledge is considered.

### Established baseline and discriminants

The initial checkout was clean and matched GitHub main. A temporary copy had
reproduced a second configuration overwriting a customized adapter while
preserving state. Structural validation alone missed that behavior; this is why
configuration regression tests became part of CI rather than relying only on a
file/schema check.

The configured adapter initially linked only project CURRENT; the default
source table contained only the project source. That was a reachability gap,
not evidence of an observed ChatGPT failure.

### Implemented owner disposition

| Owner | Difference and reason |
| --- | --- |
| AGENTS and ChatGPT adapter | Selective user/context and kernel-method entry; no automatic greeting boot. |
| KERNEL | Understand representations by function and still-valid reasons, including entry-order framing. |
| COMPETENCE | Regenerate methods, circulate results, learn externally and cultivate user-owned competence from more than failures. |
| EVOLUTION | Keep learning with its causal owner; preserve pending integration across unchanged-source scans; reread actual results. |
| USER_GUIDE and state templates | Show creation, location, retrieval and learning while state keeps current implication/pointer. |
| Configurator, INSTALL and adapter guide | Preserve configured bytes by default; preview no-write; adapter/state replacement independent; host sync separate. |
| Validator, tests and CI | Check package links and configuration effects on Windows/Linux without certifying model behavior. |
| README, architecture, state, version and changelog | Describe the same package and evidence boundaries. |

FDLA and operations retained their existing bodies: self-closure correction,
unfinished flows, request/result ownership and replay-aware recovery were
already present. No new runtime, registry, provider or fixed competence
directory was needed.

## Completion and reentry

Implement a selected owner-native result, then reread the resulting package for
lost capabilities, disconnected entry, duplicate owners, host residue and
update behavior. Refine the coherent form without losing the portable delta.
These are cognitive passes; do not repeat material effects to count passes.

For source reentry, compare actual repository identity and the specific CI
result rather than assuming this guide proves publication. New operator
direction, a changed destination source or a material contradiction supersedes
the relevant decision. Preserve unrelated concurrent work.

No repository test establishes account installation, connector access, actual
model use or behavioral assimilation. Return those states separately.
