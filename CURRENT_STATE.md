# kernel_chat — current state

Updated: 2026-09-19

```text
source_version: 0.6.0
current_work: public first-encounter and receiver-relative adoption convergence
current_change: public README reorganized for normal users: value -> observable example -> evidence-derived Q&A -> setup -> deep study
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

Fresh receiver tests showed a stable distinction between what ordinary users
need first and what belongs to the study surface. The public README now starts
from the result available to the user, then gives one observable before/after
case, answers recurrent adoption questions, exposes setup, and only afterward
routes into the internal kernel sources.

The public progression is now:

```text
user result
-> observable later-work difference
-> recurrent questions answered in place
-> source/setup path
-> ready-made integrations
-> deep kernel / research surface
```

The Q&A is evidence-derived rather than objection-generating. It answers
questions repeatedly produced by first encounters: what learning means, how the
kernel differs from memory/instruction carriers, portability beyond ChatGPT,
source and write requirements, selective context use, revision of stale
competences, the competence trace, and how to observe whether later work has
actually changed.

Answers state the operating relation positively and then give the action or
source path that matters. Conceptual terms and deeper architecture remain
reachable in Core, Competence, Evolution, FDLA, Architecture and the SSK paper;
normal adoption does not require reading them first.

The public surface therefore no longer uses internal conceptual depth as the
entry cost for understanding the product. It also avoids a defensive "what this
is not" perimeter: receiver-added categories are answered only when an observed
question makes that distinction useful.

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

The previous AGI/autopoiesis/provider/persistent-awareness framing is no longer
present in the GitHub About topics. The repository homepage field is currently
empty, so the unreconciled historical `maios.it/conversation-kernel.html`
surface does not participate in this first-encounter path.

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

The complete preceding state and review genealogy remain available at
[the pre-correction source checkpoint](https://github.com/GrazianoGuiducci/kernel_chat/blob/6bbfa868ecfaa8e5806d703fe68f81efa3f9a044/CURRENT_STATE.md),
in the [review record](docs/EXTERNAL_REVIEW_0_6_0.md) and
[evolution guide](docs/EVOLUTION_GUIDE.md). They are historical evidence, not a
second current onboarding instruction. Product releases, installed instances,
account settings and downstream publications remain separately selected work.
