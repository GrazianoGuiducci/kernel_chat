# kernel_chat — current state

Updated: 2026-09-20

```text
source_version: 0.6.0
current_work: modality-neutral portable carrier and receiver-relative adoption convergence
current_change: public narrative reconciled around identity -> why -> offered transformation -> operation; carrier/setup descend after the object; portable entry 3.0.0 unchanged
latest_tagged_distribution: v0.6.0
release_promotion_commit: d2c94ca4e4523f1f7a343601d6beec1e84031fac
material_review_target: 2c111f2797a7ffe945067ac4b6eee8baace7c9c9
material_review_result: no_change
material_review_ci: 35390696891
current_proof_owner: GitHub Actions on validated PR tree + post-merge tree-identity verification
owner: Graziano Guiducci
```

## Object and adoption

`kernel_chat` is a user-owned semantic operating kernel for AI.
Working knowledge, competence formation, source-aware understanding and learning
participate together. Persistence makes that knowledge available across sessions and receiving environments;
it is one means of continuing the kernel rather than its full identity.

Use kernel_chat when the receiving AI environment can retain a persistent/custom
operating entry and reach a durable kernel source. A chat with Custom
Instructions plus GitHub, MCP, project knowledge, filesystem, connector or
equivalent source access is one concrete incarnation. Use MAIOS Project Kernel
when a durable workspace/filesystem is itself the AI's continuing operating
surface. The carrier follows those relations rather than a chat-vs-agent
category.

[Setup](docs/SETUP.md) now starts from the source route the
receiver actually exposes: use an already-reachable persistent source in place,
use project/knowledge storage as the persistent source when that is the native
mechanism, or treat attachments as session-only until persistence exists.

The provider-neutral portable entry is now version `3.0.0`. It
foregrounds **"Do not presume. Go deeper without narrowing the field."**, makes
experience-to-capability return explicit, and continues to activate the Core
competence trace. Host-specific configuration, provenance, receipt and recovery
mechanics are routed downward to their adapters instead of remaining
constitutive content in `AGENTS.md`.

The existing [ChatGPT helper](INSTALL.md) renders that same instruction source
with a GitHub instance and retains its configured-bridge and operator-report
receipts. Other receiving environments use their own persistent/custom
instruction and source mechanisms while preserving the same owners.

## Current product narrative

The public README now keeps four product functions independently recoverable:

```text
identity:
  user-owned semantic operating kernel for AI

why:
  useful operating context, reasons and ways of working otherwise require
  reconstruction or remain dependent on host-local persistence

what it offers:
  continuity from the present
  + reusable competences
  + learning from real work
  + user-owned operating knowledge
  + portable/selective reentry

what it does:
  present work
  -> selective source/state/competence participation
  -> authorized host effect when needed
  -> consequence/readback
  -> reusable learning returns to the owner that must behave differently later
```

Carrier, provider, setup and implementation mechanics now descend after these
relations are formed. The narrative functions are not mandatory README section
names for other products; the reusable editorial owner is
`Editoriali/skills/editorial-semantic-kernel/references/product-semantic-narrative.md`.

## Current communication correction

A fresh receiver readback exposed one remaining first-encounter compression:
after reaching deeper owners, a receiver could still reduce competence to a
structured note and continuity to rereading. The current surface therefore
makes the constitutive relation explicit:

```text
real experience
-> reusable difference
-> competence that understands / does differently
-> later non-identical work begins from the changed capability
```

The stored text is a carrier of that learning, not the competence itself. This
is a communication/entry correction; the architecture and portable adoption
contract are unchanged.

Receiver tests remain useful for locating ambiguity, but their doubts are not
treated as a standing content backlog. The README makes the product inspectable
through direct capability-to-source routes.

The public progression is:

```text
user result
-> observable before / after
-> capability + what it changes + source to inspect
-> minimal clarifications where a material ambiguity remains
-> direct verification path
-> setup / integrations
-> optional deep study
```

The capability map points directly to Core, Competence, Evolution, FDLA,
SOURCES, the provider-neutral portable entry, adoption/setup sources,
the ChatGPT adapter and current package evidence.

The public surface therefore answers uncertainty primarily by exposing the owner
that determines the relation. Clarification is added only when a source link
alone would leave a material ambiguity for correct use.

Complex architecture and research terminology remain available through the
kernel owners and SSK paper. They are depth, not prerequisite explanation.

The README remains a shared entry for people and AI assistants: humans can
inspect the capability map and start path; AI assistants can follow the same
owner links when deeper knowledge becomes relevant.

Portable adoption is defined by the receiver relation:

```text
persistent/custom instruction entry
+ persistent source reachable by the receiving environment
-> kernel_chat adoption
```

README, portable-entry guidance, SETUP, ADOPTION_GUIDE, AGENTS and
Architecture all preserve the same result. A host-specific adapter is optional;
when present, it packages receiver-specific setup, translation, receipt or
recovery mechanics.

A public-source hygiene pass also removed non-portable development-source topology from the
portable entry, Competence, FDLA, Lineage and package-evolution narrative.
Historical review evidence now states only the scope of what that review
observed: it neither establishes nor rules out capabilities outside its evidence
surface. Core and host-adapter documentation describe runtime means as
receiver-relative rather than as a permanent capability ceiling.

Exact current-effect boundaries remain explicit where they are evidence-bearing
(for example read != write, configured != installed, operator report != direct
host inspection).

## GitHub first-encounter metadata

The repository source now carries the modality-neutral product relation, but the
separate GitHub About metadata has not yet been mutated through the available
repository connector.

Target description:

```text
A user-owned semantic operating kernel for AI, where experience becomes situated competence and changes how later work is understood and carried out.
```

Target topics replace `conversational-ai` with `human-ai-interaction` while
preserving the other current product topics.

Observed GitHub About still carries the preceding conversational description and
topic. This is an external metadata reconciliation effect, not a source defect
or permission to rewrite the kernel around that stale label. The repository
homepage field remains empty.

## Post-resultant consumer convergence

A post-public audit found one live consumer still carrying the old modality
frame: `docs/USER_GUIDE.md` used "chat" and "new chat" as the default form of
ordinary use and continuation. The guide now uses receiving environment /
session where modality does not matter, while ChatGPT remains named only for
its actual helper/setup mechanics.

This is consumer convergence of the modality-neutral carrier resultant, not a
new kernel capability or adoption contract.

## Preserved mechanics and knowledge

For the ChatGPT helper, INSTANCE retains package/bridge identity and reported
host observations separately from CURRENT context and SOURCES knowledge.
Configured, delivered and operator-confirmed bridge identities remain distinct.
Cooperative writer locking, conservative legacy handling, raw-byte digests,
drift handling, exact-delivery confirmation, and fresh remote receipt readback
remain implemented by their existing owners and tests.

[Architecture](docs/ARCHITECTURE.md), [installation](INSTALL.md),
[adoption](docs/ADOPTION_GUIDE.md), the [portable entry](adapters/portable/README.md), the [ChatGPT adapter](adapters/chatgpt/README.md),
[Core](kernel/KERNEL.md), [Competence](kernel/COMPETENCE.md),
[Evolution](kernel/EVOLUTION.md) and [FDLA](kernel/FDLA.md) retain the deeper
operating and mechanical relations. Ordinary user context, reusable methods
and optional unfinished operations keep their distinct purposes.

## Current source proof after portable-carrier publication

```text
validated candidate:
  8d7ce3a1d8bfda73917841a560d398fddb268ab7

CI:
  run 35503746605
  validator valid=true / errors=[]
  62 tests
  8/8 Python 3.11–3.14 x Ubuntu/Windows

published main:
  4ff04dab5d87cd0ddfcdfe71dce9a2a4770ff032

validated tree = published tree:
  955f7bc469a04e3dc555e2ea87c6cc3118db615d
```

The squash commit has a different commit identity from the validated candidate;
tree identity establishes that the published source content is the tested
result. This does not make the two commits the same evidence object.

## Evidence and released identity

The portable carrier checkpoint at
`0742d6022c7cfa6e78917ae522d479747e2a8a1e` remains its own proof identity.

The object-first public-entry resultant at
`908732a560aef7896c2696fc7907a822c2583644` retains its own CI
`35436080650` evidence.

The current portability/setup resultant before this state readback is
`077e2a54c3ae14e34f3f0be97e66e17bd497610e`, CI
`35439455922`: validator clean, 61 tests, 8/8 Python 3.11–3.14 ×
Ubuntu/Windows. It adds conversational instructions `2.1.0`, the portable
competence trace, source-route setup branching and removal of ChatGPT receipt
mechanics from the constitutive AGENTS discovery contract.

The material review result belongs to `2c111f2797a7ffe945067ac4b6eee8baace7c9c9`.
Release `v0.6.0` remains on `d2c94ca4e4523f1f7a343601d6beec1e84031fac` with
promotion CI `35391971484` and 58 tests. Initial publication readback was
`159590474f46509296ba3fc3634f1e4bb3edf9d3`, CI `35392846944`.
Those historical identities do not move with subsequent source documentation.

Live adoption and fresh-receiver behavioral readback remain separate from
repository proof. The suite establishes the package, navigation, source-route
and configured-entry relations at the tested revision; it does not certify
behavior in every receiving environment.

## Continuity

Preceding state and review genealogy remain available through Git history, the
[review record](docs/EXTERNAL_REVIEW_0_6_0.md) and
[evolution guide](docs/EVOLUTION_GUIDE.md). They are historical evidence; the
current README and living owners define the present product relation. Product
releases, installed instances, account settings and downstream publications
remain separately selected work.
