# kernel_chat — current state

Updated: 2026-09-19

```text
source_version: 0.6.0
current_work: public product and receiver-relative adoption convergence
current_change: portable adoption clarified: host-specific adapter is optional when persistent instruction + persistent source already exist
latest_tagged_distribution: v0.6.0
release_promotion_commit: d2c94ca4e4523f1f7a343601d6beec1e84031fac
material_review_target: 2c111f2797a7ffe945067ac4b6eee8baace7c9c9
material_review_result: no_change
material_review_ci: 35390696891
current_proof_owner: GitHub Actions on the exact current source commit
owner: Graziano Guiducci
```

## Object and adoption

`kernel_chat` is a user-owned semantic operating kernel for conversational AI.
Working knowledge, competence formation, source-aware understanding and learning
participate together. Persistence makes that knowledge available across chats;
it is one means of continuing the kernel rather than its full identity.

Use kernel_chat for a conversational app. Use MAIOS Project Kernel for an
agent harness, agentic application or IDE. The destination's working mode, not
the model name, determines this product choice.

[Chat setup](docs/CHAT_SETUP.md) now starts from the source route the
receiver actually exposes: use an already-reachable persistent source in place,
use project/knowledge storage as the persistent source when that is the native
mechanism, or treat attachments as session-only until persistence exists.

The provider-neutral conversational entry is now version `2.1.0`. It also
activates the Core competence trace. Host-specific configuration, provenance,
receipt and recovery mechanics are routed downward to their adapters instead of
remaining constitutive content in `AGENTS.md`.

The existing [ChatGPT helper](INSTALL.md) renders that same instruction source
with a GitHub instance and retains its configured-bridge and operator-report
receipts. Other conversational receivers use their own persistent/custom
instruction and source mechanisms while preserving the same owners.

## Current communication correction

Receiver tests were useful for locating ambiguity, but their doubts are no
longer treated as a content backlog. The README now makes the product inspectable
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
SOURCES, the provider-neutral conversational entry, adoption/setup sources,
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
+ persistent source reachable by the conversation
-> kernel_chat adoption
```

README, conversational-entry guidance, CHAT_SETUP, ADOPTION_GUIDE, AGENTS and
Architecture all preserve the same result. A host-specific adapter is optional;
when present, it packages receiver-specific setup, translation, receipt or
recovery mechanics.

## GitHub first-encounter metadata

The repository-level GitHub About surface has been reconciled and re-read after
the README rewrite.

Current public description:

```text
A user-owned semantic operating kernel for conversational AI, where situated competences learn from use and change how later work is carried out.
```

Current public topics:

```text
ai-architecture
causal-learning
competence-evolution
context-engineering
context-management
conversational-ai
human-ai-collaboration
llm
semantic-kernel
situated-competence
```

The GitHub About surface is reconciled to the current product relation. The
repository homepage field is currently empty, so no separate homepage
representation participates in this first-encounter path.

## Preserved mechanics and knowledge

For the ChatGPT helper, INSTANCE retains package/bridge identity and reported
host observations separately from CURRENT context and SOURCES knowledge.
Configured, delivered and operator-confirmed bridge identities remain distinct.
Cooperative writer locking, conservative legacy handling, raw-byte digests,
drift handling, exact-delivery confirmation, and fresh remote receipt readback
remain implemented by their existing owners and tests.

[Architecture](docs/ARCHITECTURE.md), [installation](INSTALL.md),
[adoption](docs/ADOPTION_GUIDE.md), the [conversational entry](adapters/conversational/README.md), the [ChatGPT adapter](adapters/chatgpt/README.md),
[Core](kernel/KERNEL.md), [Competence](kernel/COMPETENCE.md),
[Evolution](kernel/EVOLUTION.md) and [FDLA](kernel/FDLA.md) retain the deeper
operating and mechanical relations. Ordinary user context, reusable methods
and optional unfinished operations keep their distinct purposes.

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
behavior in every conversational host.

## Continuity

Preceding state and review genealogy remain available through Git history, the
[review record](docs/EXTERNAL_REVIEW_0_6_0.md) and
[evolution guide](docs/EVOLUTION_GUIDE.md). They are historical evidence; the
current README and living owners define the present product relation. Product
releases, installed instances, account settings and downstream publications
remain separately selected work.
