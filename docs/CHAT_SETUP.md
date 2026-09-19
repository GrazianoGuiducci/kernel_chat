# Set up kernel_chat in a conversational app

Use this guide for a chat app. For an agent harness, agentic app or IDE, use
[MAIOS Project Kernel](https://github.com/GrazianoGuiducci/maios-project-kernel)
in the agent's workspace. A project area in a conversational app is still a
chat setting.

Setup connects the kernel's working knowledge, the app's instructions and a
place to keep your evolving context. The assistant uses the tools already
available; you complete account settings and file placement when those actions
belong to you.

## 1. Make the working knowledge available

Use a private project or knowledge area in your chat app, or a user-controlled
repository that the app can actually read. Place the following source files
from the same revision there, preserving their names:

- [KERNEL.md](../kernel/KERNEL.md)
- [COMPETENCE.md](../kernel/COMPETENCE.md)
- [EVOLUTION.md](../kernel/EVOLUTION.md)
- [FDLA.md](../kernel/FDLA.md)

These files carry the methods, not just the description on the public README.
For linked files, check access from the destination chat. When a link cannot
be read there, use the app's file-upload or knowledge feature.

Keep a `CURRENT.md` for the context you want to continue and a `SOURCES.md` for
original sources and reusable methods. The existing
[current-context template](../templates/state/CURRENT.md) and
[source template](../templates/state/SOURCES.md) provide starting forms; replace
placeholders with your own situation. An initial project is optional.

## 2. Install the conversational entry

Use the canonical provider-neutral instruction source:

[Conversational instructions](../adapters/conversational/INSTRUCTIONS.template.md)

Replace `{{KERNEL_SOURCE}}` with the source relation the receiving app can
actually reach.

Examples:

```text
github:YOUR_GITHUB_USER/YOUR_REPOSITORY

project knowledge in this project

a receiver-native persistent source that contains the same kernel paths
```

The installed entry points to the kernel owners:

```text
AGENTS.md
kernel/KERNEL.md
kernel/COMPETENCE.md
kernel/FDLA.md
kernel/EVOLUTION.md
state/CURRENT.md
state/SOURCES.md
```

Do not rewrite those methods into provider-specific instructions. The backend
instructions establish the entry; the repository or supplied knowledge carries
the kernel.

For ChatGPT, the existing configurator renders this source automatically with
the selected GitHub instance and records the configured/installed bridge
identity. Other conversational apps install the same semantic entry through
their own persistent/custom instruction surface.

## 3. Begin a real task

Ask an ordinary question or start the work you brought. During setup, have the
assistant read one supplied method and explain briefly how it applies to that
work. This confirms the source is usable in the current chat.

After a useful change, save the context or method that should continue. Start a
new chat in the same scope when you need to resume, and use the saved source.
The [User guide](USER_GUIDE.md) explains this continuing work.

## Claude Projects: file-based setup

In Claude's conversational app, create or open a project. Add the kernel files
and your context files to **project knowledge**. Render the same conversational
instruction template with `KERNEL_SOURCE` identifying that project knowledge,
save it under **project instructions**, then start a chat inside that project.

Project knowledge and project instructions are the shared sources for chats in
that project. When the assistant provides an improved method or updated context,
replace the saved file in project knowledge, or use a connected writing tool
when one is available. A discussion in one chat is not itself a saved update to
project knowledge.

This route uses project files and instructions; it does not require running the
ChatGPT configurator. Anthropic documents the two features in its
[project setup guide](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).
This is a documented setup route; an individual account's file access and
continuation are checked during its setup.

## ChatGPT: repository setup with the existing helper

Use [INSTALL.md](../INSTALL.md) for the Git/Python configuration path and the
[ChatGPT adapter guide](../adapters/chatgpt/README.md). It generates the entry
text and records that specific repository/ChatGPT setup.

Follow its complete host-confirmation and remote-readback procedure before
relying on the configured repository in a later chat. Those receipts describe
the ChatGPT helper's installation; they are not used to label a Claude project.

OpenAI documents the account instruction surface in
[Custom Instructions](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt).

## Other conversational apps

Use the same working files with the app's actual persistent instructions and
knowledge or connector features. The assistant identifies the relevant setting
and prepares the entry for that location. When a chat only accepts attachments,
the files can support that conversation; keep the updated files yourself for
later sessions. Persistent configuration is complete when the chosen app scope
can reach the saved entry and knowledge again.

## Keep the setup and learning yours

Choose a private destination for private work. Keep the source revision with
the copied kernel files, and distinguish it from changes made through your use.
A future upstream update is compared with those local methods so useful learning
survives. Existing source/update guidance is in the
[Adoption model](ADOPTION_GUIDE.md).
