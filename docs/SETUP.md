# Set up kernel_chat in a receiving AI environment

`kernel_chat` uses a portable host carrier. A chat is one common case,
but not the defining parameter.

A persistent adoption needs two things:

```text
persistent/custom operating instructions or equivalent entry
+ a persistent kernel source the conversation can reach
```

Current context and reusable learning then live in that reachable source.

If the receiving AI instead owns a durable project workspace/filesystem as its
continuing operating surface, use
[MAIOS Project Kernel](https://github.com/GrazianoGuiducci/maios-project-kernel).

## 1. Choose the source route that actually exists

### A. A persistent source is already reachable

If the conversation can already read the user-controlled repository, knowledge
space, filesystem, connector or equivalent source that contains the kernel,
use it in place.

Do not copy the kernel merely because another setup example used files.

Keep these owner paths reachable from one source revision:

- [AGENTS.md](../AGENTS.md)
- [KERNEL.md](../kernel/KERNEL.md)
- [COMPETENCE.md](../kernel/COMPETENCE.md)
- [FDLA.md](../kernel/FDLA.md)
- [EVOLUTION.md](../kernel/EVOLUTION.md)
- [CURRENT template](../templates/state/CURRENT.md)
- [SOURCES template](../templates/state/SOURCES.md)

Use or create the user-owned `CURRENT` and `SOURCES` forms only when
continuity or source relations need them.

### B. Project / knowledge storage is the persistent source

Place the same constitutive owners in the environment's persistent
project/knowledge surface and keep the source revision attributable.

Preserve the canonical paths when that surface supports them. If it exposes
only flat filenames, preserve the same owner identities and render the
portable entry with the actual references available there.

The project/knowledge surface is now the kernel source for that host scope
scope.

### C. Only current-session attachments are available

The supplied kernel sources can participate in the current conversation, but
this is not yet persistent adoption.

Use them now if useful. When continuity across conversations is wanted, place
the kernel and user-owned context in a source that the later conversation can
reach, then install the persistent entry there.

## 2. Install the same portable entry

Use the provider-neutral source:

[Portable instructions](../adapters/portable/INSTRUCTIONS.template.md)

Replace `{{KERNEL_SOURCE}}` with the actual source relation the receiver can
reach.

Examples:

```text
github:YOUR_GITHUB_USER/YOUR_REPOSITORY

project knowledge in this host scope

another receiver-native persistent source containing the same owners
```

The entry reaches:

```text
AGENTS.md
kernel/KERNEL.md
kernel/COMPETENCE.md
kernel/FDLA.md
kernel/EVOLUTION.md
CURRENT
SOURCES
```

Do not rewrite the kernel into provider-specific instructions. Translate source
references only as needed to reach the same owners.

A host-specific adapter is optional. If the receiver already exposes a
persistent instruction surface and a persistent source route, install this
portable entry directly through those native mechanisms.

When host-specific setup, translation, receipts or recovery mechanics need a
ready-made implementation, use the corresponding adapter. For the current
ChatGPT repository helper use [INSTALL.md](../INSTALL.md) and the
[ChatGPT adapter guide](../adapters/chatgpt/README.md).

## 3. Begin real work

Start the actual question, activity or project.

The new kernel instance enters through the installed portable entry and
reaches only the owners that can change the movement. Do not add a separate
review or demonstration task merely to prove setup.

Every final response should now carry the compact competence trace defined by
the [Core](../kernel/KERNEL.md#kernel-chat-competence-trace). That trace is one
observable sign of which competences materially participated; it is not proof
of full assimilation.

If a required source cannot be reached, reconnect or supply that source rather
than reconstructing unavailable contents.

## 4. Continue and learn

When current context must survive, keep the smallest useful relation in
`CURRENT`. Keep original/reusable knowledge in `SOURCES` or its owner-native
source. Return reusable learning to the competence that should behave
differently later.

A later conversation in the same already-incarnated scope does not reload the
whole kernel merely because it is new. It reenters from the present and reaches
additional owners only when they can change the result.

The [User guide](USER_GUIDE.md) continues from here. The
[Adoption guide](ADOPTION_GUIDE.md) preserves the receiver and effect
boundaries.
