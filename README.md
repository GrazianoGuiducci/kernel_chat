# kernel_chat

**An evolving way of working for conversational AI.**

`kernel_chat` is a user-owned semantic kernel: working knowledge that helps an
AI understand your situation, develop useful methods, connect skills and
sources, and learn from what happens. You keep that knowledge so it can grow
with your work and remain available across conversations and models.

A useful result can improve both what you are doing and how the AI approaches
what comes next. A discovery can become a method; methods can combine into a
new capability; experience can improve the way those capabilities are formed.
This capacity to develop its own working organization is the kernel's
autopoietic dimension.

## Choose your environment

| Where you work | Kernel to use |
| --- | --- |
| A conversational AI app, such as ChatGPT, Claude or another chat | **kernel_chat** — [set it up in your chat](docs/CHAT_SETUP.md). |
| An agent harness, agentic app or IDE, such as Codex, Claude Code or OpenCode | **[MAIOS Project Kernel](https://github.com/GrazianoGuiducci/maios-project-kernel)** — install it in the agent's workspace. |

Choose by how the application works, rather than by the model's name. Claude
chat and Claude Code, for example, use different forms of the kernel. A project
space inside a chat app can hold `kernel_chat` knowledge and instructions.

## What you gain

### Working knowledge that develops with you

A competence is knowledge the AI can use: what matters in a field, why a method
works, how to adapt it, and what experience has taught. The kernel helps the AI
find, combine, deepen and form competences as the situation develops. Research,
writing, planning, design and everyday work are possible starting points; the
methods and combinations can extend beyond these examples.

### More continuity, less reconstruction

Your decisions, their reasons, relevant sources and unfinished work can remain
available together. A later conversation can recover the part that matters and
continue from the situation as it is now. You retain the knowledge in sources
you can inspect, edit and carry into another setting.

### Learning that changes the next attempt

Imagine researching a topic with your AI. Together you discover that a familiar
way of comparing sources misses an important distinction. You preserve the
improved method and its reason. On a different question, the AI can reach that
method, adapt it and develop it further. The learning can also change how the
AI builds future research methods.

The same relation applies to a writing practice, a design method, a decision
process or a capability that emerges during work.

### Room for the unexpected

A new source, a useful result or a different perspective can change the question
and the methods that fit it. The kernel carries reasons and ways of learning,
rather than prescribing every future answer. It helps the AI notice when its
first interpretation has made the problem smaller than it really is.

## Start using it

Give this repository link to your AI and ask:

```text
Set up kernel_chat for this chat, using the instructions and knowledge storage
available here. Keep my existing work. Help me complete the setup and then
use it with me on [what I want to work on].
```

[**Chat setup**](docs/CHAT_SETUP.md) provides a shared route through project
instructions and knowledge files, a concrete Claude Projects example, and the
existing ChatGPT configuration helper. It also explains how to keep useful
changes when the app can read files but cannot save them directly.

The installation work follows the tools available in your app. The assistant
handles the steps it can perform and gives you the exact text or file for any
step that needs your action. Private work stays in a private destination you
choose.

After setup, bring your real work:

```text
Let's work on [topic]. Use the relevant sources and methods. When we learn
something reusable, help me preserve it where our next conversation can use it.
```

The [User guide](docs/USER_GUIDE.md) covers everyday use, continuing a topic,
forming competences and keeping what you learn. You can begin with an idea,
a question, an ongoing activity or a project.

## How it fits together

The [Core](kernel/KERNEL.md) carries the operating principles. The
[competence method](kernel/COMPETENCE.md) develops ways of working;
[evolution](kernel/EVOLUTION.md) returns useful experience to those methods;
[self-correction](kernel/FDLA.md) helps revise an interpretation when it
obscures the actual situation.

The model puts that knowledge to work with the sources, tools and instructions
available in its application. Saved files and the entry instructions make the
knowledge reachable again. The same core can therefore be used through
different conversational environments.

## Guides and source

[Chat setup](docs/CHAT_SETUP.md) ·
[Adoption model](docs/ADOPTION_GUIDE.md) ·
[User guide](docs/USER_GUIDE.md) ·
[ChatGPT helper](INSTALL.md) ·
[ChatGPT adapter guide](adapters/chatgpt/README.md) ·
[Architecture](docs/ARCHITECTURE.md)

For source work: [AGENTS.md](AGENTS.md), [Contributing](CONTRIBUTING.md),
[Changelog](CHANGELOG.md) and [Current source state](CURRENT_STATE.md).

[Source version](VERSION) · [Apache License 2.0](LICENSE)

Copyright 2026 Graziano Guiducci.
