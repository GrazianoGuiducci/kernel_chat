# kernel_chat — current state

Updated: 2026-09-19

```text
source_version: 0.6.0
current_work: conversational adoption and public communication
current_change: shared chat setup, reader-facing explanation and source-route tests
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

[Chat setup](docs/CHAT_SETUP.md) now supplies a shared instructions-and-knowledge
route, including a concrete Claude Projects configuration. Other chat apps use
their actual instruction, file or connector facilities. The existing
[ChatGPT helper](INSTALL.md) remains the Git/Python implementation with its own
configured-bridge and operator-report receipts.

The shared file route does not fabricate a ChatGPT `INSTANCE` receipt. It keeps
source identity, saved knowledge and the chosen app scope explicit. When the
assistant cannot save an updated method, the user receives the complete file
to place in that scope.

## Current communication correction

The operator supplied a Claude readback in which the prior README was reduced
to memory/context, its unsolicited denials became prominent, and its commands
to an evaluating LLM were treated as hidden instructions. The response is one
reported encounter, not a benchmark across models.

The public entry now explains the kernel's practical and generative value,
uses a concrete example and leads directly to setup. Generalized denials,
review genealogy and model-directed evaluation instructions no longer shape
the README. AGENTS and the adoption/user guides carry the corresponding route.

This source change adds a documented chat setup path. It does not change the
portable kernel bodies, configurator, runtime validator, state schema or
existing ChatGPT bridge. The documentation test observes active navigation
rather than freezing an editorial heading or requiring a duplicated procedure.

## Preserved mechanics and knowledge

For the ChatGPT helper, INSTANCE retains package/bridge identity and reported
host observations separately from CURRENT context and SOURCES knowledge.
Configured, delivered and operator-confirmed bridge identities remain distinct.
Cooperative writer locking, conservative legacy handling, raw-byte digests,
drift handling, exact-delivery confirmation, and fresh remote receipt readback
remain implemented by their existing owners and tests.

[Architecture](docs/ARCHITECTURE.md), [installation](INSTALL.md),
[adoption](docs/ADOPTION_GUIDE.md), the [adapter](adapters/chatgpt/README.md),
[Core](kernel/KERNEL.md), [Competence](kernel/COMPETENCE.md),
[Evolution](kernel/EVOLUTION.md) and [FDLA](kernel/FDLA.md) retain the deeper
operating and mechanical relations. Ordinary user context, reusable methods
and optional unfinished operations keep their distinct purposes.

## Evidence and released identity

The current source suite contains 59 tests: 38 configurator, 18 validation and
public-route cases, and 3 CommonMark consumer cases. CI is configured for
Python 3.11–3.14 on Ubuntu and Windows. Read the actual run for the exact
commit before attributing a result to this source.

The material review result belongs to `2c111f2797a7ffe945067ac4b6eee8baace7c9c9`.
Release `v0.6.0` remains on `d2c94ca4e4523f1f7a343601d6beec1e84031fac` with
promotion CI `35391971484` and 58 tests. Initial publication readback was
`159590474f46509296ba3fc3634f1e4bb3edf9d3`, CI `35392846944`.
Those historical identities do not move with subsequent source documentation.

The shared Claude route is documented from the app's project features. Live
adoption and a new reader test on this revised source have not been performed
in this maintenance turn. Repository tests establish their tested mechanics
and routes, not a result from a different model or account.

## Continuity

The complete preceding state and review genealogy remain available at
[the pre-correction source checkpoint](https://github.com/GrazianoGuiducci/kernel_chat/blob/6bbfa868ecfaa8e5806d703fe68f81efa3f9a044/CURRENT_STATE.md),
in the [review record](docs/EXTERNAL_REVIEW_0_6_0.md) and
[evolution guide](docs/EVOLUTION_GUIDE.md). They are historical evidence, not a
second current onboarding instruction. Product releases, installed instances,
account settings and downstream publications remain separately selected work.
