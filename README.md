# kernel_chat

**A user-owned semantic operating kernel for conversational AI.**

`kernel_chat` lets a conversational AI continue as part of an evolving
relation with the user instead of treating every conversation as an isolated
surface.

It is not only a memory layer. The kernel can selectively recover the context,
sources, competences, reasons and consequences that matter to the present
movement; let new knowledge or a changed result alter what becomes pertinent
next; and revise a closure introduced by its own interpretation rather than
turning the current representation into the boundary of the object.

The current **0.6.0** incarnation uses GitHub as its first persistence surface
and ChatGPT as its first host adapter. Those mechanisms make the kernel usable
today; they are not its identity or its future limit.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Adapter](https://img.shields.io/badge/adapter-ChatGPT-10a37f.svg)](adapters/chatgpt/)

[Source version](VERSION) · [Install / adopt](INSTALL.md) ·
[Adoption model](docs/ADOPTION_GUIDE.md) · [User guide](docs/USER_GUIDE.md) ·
[Core](kernel/KERNEL.md) · [Architecture](docs/ARCHITECTURE.md)

## If an AI / LLM received this link

A GPT, Claude, Gemini, DeepSeek or another capable model does not need to be the
final host of `kernel_chat` in order to understand the repository.

When an operator gives an AI this link, the useful first task is **not**
installation. The model should first understand the object and report back in
plain language:

```text
what kernel_chat is
what changes compared with an ordinary isolated chat
what value it could have for this operator's actual way of working
which parts are available now
which parts are only a direction or possibility
whether kernel_chat is the right carrier for this environment
what the model can actually do itself
what still requires operator authority or another execution surface
```

The model should distinguish its ability to **study and explain** the source
from its ability to **adopt it in its own host**.

Any capable LLM can inspect the public source when it can reach it. The current
repository, however, implements a **ChatGPT host adapter**. Another model or
chat host should not claim that `kernel_chat` is installed or supported there
merely because it can understand the kernel. It can still explain the product,
assess fit, use the portable kernel as a source of operating knowledge, and
identify what receiver-native adapter or persistent surface would be needed.

If the operator then wants to adopt it, continue with
[Install / adopt](INSTALL.md) and the
[Adoption model](docs/ADOPTION_GUIDE.md). If the operator already works with an
AI/coder inside a durable project filesystem, also compare the fit with
[MAIOS Project Kernel](https://github.com/GrazianoGuiducci/maios-project-kernel)
before choosing a carrier.

## What the kernel is

The kernel is a portable operating relation through which a conversational
system can work from the present without being confined to the present
conversation.

```text
present relation
+ still-valid determinations
+ materially pertinent possibilities
+ owner-native knowledge and sources
+ competences that can participate
+ means that are actually available
+ enough consequence awareness to distinguish movements
-> situated movement
-> result / genuine non-collapse
-> causal readback
-> revisable continuation
```

These are causal relations, not mandatory stages.

If the current conversation is sufficient, the system should simply work. If a
durable relation can materially change the result, it can be recovered
selectively. If real use produces a reusable difference, that difference can be
preserved at the closest truthful owner so that later work can continue
differently.

A project is optional. The kernel can exist before any project is selected; a
project can later become one context and source relation without becoming the
identity of the kernel itself.

## What changes in practice

With `kernel_chat`, a conversational AI can:

- **continue without replaying the whole past** — recover only the durable
  relation that can change the work now;
- **stay source-aware** — reach owner-native sources instead of treating copied
  summaries as permanent truth;
- **work with situated competences** — use, compose, deepen or form capabilities
  when the present relation makes them pertinent;
- **preserve reasons and consequences** — not only what was decided, but enough
  of why and what changed for later work to re-enter coherently;
- **learn from success, failure, correction or new possibility** — a reusable
  difference does not require a defect first;
- **revisit its own framing** — when the acting interpretation has narrowed the
  object, that closure can become part of what is examined and revised;
- **continue unfinished operational relations** when losing a cursor, receipt or
  pending result would materially change continuation;
- **keep cognition and effect authority distinct** — the system can understand,
  compare and propose beyond the effects it is currently authorized to execute.

The result is not a fixed workflow or a closed capability catalogue. A movement
may preserve what already fits, compose existing capacities, deepen an owner,
form something genuinely missing, keep an unknown open, or return
`no_change`.

## Open by design

The kernel does not assume that what is currently represented is the whole
field of what can become relevant.

Its operating logic preserves two complementary relations:

```text
current representation
!= limit of the object

real invariant / observed limit
!= permission to invent or preserve an unnecessary closure
```

The first relation keeps possibility open rather than mistaking today's schema,
tooling, vocabulary or first interpretation for the horizon. The second lets the
system detect when its own interpretation has changed the object it is trying to
understand and correct that distortion while the work is still forming.

The current portable owners for these relations include
[Core](kernel/KERNEL.md), [Competence](kernel/COMPETENCE.md),
[Evolution](kernel/EVOLUTION.md) and [FDLA](kernel/FDLA.md). Their names and
current forms are implementations of a living relation, not a claim that the
kernel can only ever contain the capabilities already named today.

## The current 0.6.0 incarnation

The current package makes the portable relation usable through a small set of
separable surfaces:

```text
portable kernel
  kernel/

user-owned continuity
  state/CURRENT.md
  state/SOURCES.md
  state/INSTANCE.json

host entry
  adapters/chatgpt/

optional unfinished operational continuity
  operations/
```

GitHub is the first persistence adapter. ChatGPT is the first implemented host
adapter. The bridge is intentionally smaller and more stable than the kernel it
reaches.

The repository, the configured bridge, the instructions installed in a host,
repository reachability and later behavior are different facts. Keeping those
facts distinct protects the user's continuity without making implementation
mechanics the semantic owner of the kernel.

## Start using it

There are two natural starts.

### 1. Understand whether it is useful to you

Give the repository link to a capable AI/LLM and ask:

```text
Read kernel_chat as a product, not only as a code repository.
Explain what it is, what it could change in the way we work, which value is
relevant to my current environment, what is implemented today, and what is not.
Then tell me whether kernel_chat is the right carrier here before proposing any
installation.
```

A good answer should be specific to the operator's environment rather than
repeating the README as marketing copy.

### 2. Adopt it

If the fit is clear, ask the model/coder to adopt `kernel_chat` using the means
it actually has:

```text
Help me adopt kernel_chat in a user-owned repository and configure it for this
chat environment. Use the capabilities you actually have, preserve the
user-owned state, and ask me only for effects you cannot perform or authorize.
```

The receiving system should distinguish repository access, repository-write
authority, filesystem/terminal access, executable setup mechanics and
account-level host settings. It should perform authorized effects it can really
perform and surface only the missing operator action.

For the current ChatGPT adapter, saving Custom Instructions and controlling
account/repository consent remain operator-owned host effects unless the host
explicitly exposes that authority.

Detailed setup, receipt publication, recovery, legacy migration and update
mechanics live in [INSTALL.md](INSTALL.md), the
[Adoption guide](docs/ADOPTION_GUIDE.md) and the
[ChatGPT adapter guide](adapters/chatgpt/README.md). They are deliberately not
the definition of the kernel.

After adoption, ordinary use starts from the user's real work rather than from a
special boot phrase. See the [User guide](docs/USER_GUIDE.md) for the first
conversation, reentry, continuity and competence use.

### Which carrier?

`kernel_chat` is designed for turn-reactive conversational hosts that do not
own a durable project workspace.

If an AI/coder already operates inside a persistent local or remote project
filesystem, a project-local carrier such as
[MAIOS Project Kernel](https://github.com/GrazianoGuiducci/maios-project-kernel)
may be the more native form. This is a receiver-fit distinction, not a boundary
on the semantic kernel itself.

## What it is not

`kernel_chat` is not:

- a transcript archive that must be replayed before useful work;
- a closed taxonomy of skills or roles;
- GitHub itself, or a repository mistaken for the kernel;
- a background daemon, scheduler or autonomous agent runtime;
- a project identity;
- permission to perform external effects without the user's authority;
- proof that a host has assimilated a method merely because files are present;
- a claim of consciousness, AGI or autonomous self-evolution.

The package provides observable mechanisms for continuity, competence,
self-correction and evolution. What later behavior actually assimilates remains
an empirical question.

## Understand it more deeply

Start with the semantic owners, then move to implementation when needed:

- [Core — what remains portable](kernel/KERNEL.md)
- [Competence — how capabilities participate, form and evolve](kernel/COMPETENCE.md)
- [Evolution — how resultants can change future operation](kernel/EVOLUTION.md)
- [FDLA — correction of interpretation-introduced closure](kernel/FDLA.md)
- [Architecture — how the current incarnation separates semantic owners, state,
  bridge and host effects](docs/ARCHITECTURE.md)
- [User guide — ordinary use and reentry](docs/USER_GUIDE.md)

`AGENTS.md` is the repository entry for a model/coder that needs to discover
the pertinent owner while working. It is not a second copy of the kernel.

## Maintainers, evidence and contribution

The public README describes the product. Maintenance, verification and review
evidence remain available without occupying that first encounter:

- [Install / adoption mechanics](INSTALL.md)
- [Current source state](CURRENT_STATE.md)
- [External review evidence](docs/EXTERNAL_REVIEW_0_6_0.md)
- [Evolution / maintenance guide](docs/EVOLUTION_GUIDE.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Lineage](docs/LINEAGE.md)

The dependency-free structural validator and the full regression suite remain
available for repository maintenance. Their results establish package mechanics
and evidence boundaries; they do not by themselves establish host behavior or
later assimilation.

## Direction

The current implementation is one observable incarnation of a broader
direction: a conversational AI able to sustain a user-owned operating relation
across changing conversations, sources, competences, contexts and carriers,
while remaining able to revise the forms through which it understands and
continues.

No present repository structure, adapter, capability list or vocabulary is
intended to define the final horizon of that direction.

## License

Copyright 2026 Graziano Guiducci. Licensed under the
[Apache License 2.0](LICENSE).
