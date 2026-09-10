# User guide

## Use the chat normally

The kernel should be quiet when the conversation already contains what is
needed. Ask ordinary questions normally. You do not need to mention the
repository on every turn.

## Continue a project in a new chat

Ask the chat where the project is or tell it to continue the configured
project. When continuity matters and GitHub is accessible, the adapter points
it to `state/CURRENT.md`. That state should lead to the specific source needed
for the present question.

If the chat cannot access the file, treat continuity as unavailable in that
turn. Do not let it invent repository contents or claim that the connector is
active.

For a missing way of understanding or working, the adapter instead reaches
`AGENTS.md` and the pertinent kernel owner. Project state does not have to
carry the kernel's constitutive competences. These are two selective paths,
not two boot stages; neither runs merely because a chat is new.

## Maintain state

Update state when one of these changes materially:

- the current point or next movement;
- an accepted correction;
- an owner-native source;
- unfinished work that should remain visible;
- a verified boundary;
- the pointer or reentry reason for a reusable way of understanding or working.

Do not store ordinary chat, duplicate summaries, credentials, or whole project
histories. A short state with accurate pointers is more useful than a large
memory dump.

Keep the reusable method in the competence or kernel owner that uses it.
State may say what changed, why it matters now and where to recover that
knowledge. When resuming, check whether the reason is still valid instead of
executing the old next action automatically.

## Add competences and metacompetences

Link a competence from `state/SOURCES.md` when it owns a way of working that can
change the project result. Do not copy it into the kernel merely to make it
visible.

A metacompetence carries comprehension developed through experience so it can
be operated, integrated, and evolved in another situation. Its instruction
file is a usable adapter; later changed behavior is the evidence that the
comprehension was assimilated.

### Grow a competence in your fork

A useful continuing ability may emerge from intent, knowledge, memory,
successful work, a new possibility or a gap. Locate the owner that already
carries it; enrich that method or compose existing competences first when
that is the useful form. A distinct function can have its own body.

For example, if work has produced a reusable source-comparison method, you
can keep it in `knowledge/source-comparison.md` in your fork, or in an existing
project guide that already owns it. That example path is optional. Explain
what it makes possible, when to use it, the sources and reasons behind it,
how to adapt its method, what experience changed it and what could invalidate
it. Keep deeper knowledge there when a short reminder would lose meaning.

Add its real location to `state/SOURCES.md`, with its owner and the condition
that makes it useful. If current project continuation depends on a correction,
put a short reason and pointer in CURRENT. Do not copy the whole method into
state or register every available competence as active.

On a later relevant task, the chat reaches the method, understands its reasons
and adapts it to the new object. Its result can call another competence or
form a temporary composition. If a later consequence changes an earlier
method, return that learning to the earlier owner. Preserve uncertainty when
the relationship is not established. No central orchestrator is needed.

With real authorized repository writing, update that owner directly. With
read-only access, prepare the exact proposed change for the user or an
available writer; do not claim it has been saved. A new file is availability,
one use is exercise, and changed behavior on a later non-identical task is
stronger assimilation evidence. This is a cultivation path, not a test you
must perform before ordinary work.

## Preserve unfinished work

Use the `Open work` section in `state/CURRENT.md` for the causal remainder that
should survive the conversation. Describe what is unfinished and what evidence
exists. Do not turn it into an automatic task queue or authority to execute an
old instruction.

If work would lose a material cursor, pending relation, result, or effect
receipt between conversations, use the optional [`operations/`](../operations/)
organ. Keep it cold when nothing there changes continuation. Version `0.5.0`
does not imply that a scheduler, daemon, or executor is running.

## Evolve the kernel

When a real situation is handled differently because of a reusable
observation, decide where the change belongs:

- project-specific truth goes to the project;
- ChatGPT-specific friction goes to the ChatGPT adapter;
- reusable comprehension goes to a competence or metacompetence;
- a change to the portable operating relation goes to `kernel/`.

Keep source, reason, and an invalidating condition close to consequential
changes. Prefer small reversible edits over accumulated doctrine.

## Privacy and control

The visibility of your fork determines who can see its state. Use a private
fork or repository when the continuity is not public, provided your ChatGPT
connection can access it.

Never store tokens, passwords, private keys, or secret logs in the repository
or Custom Instructions. Grant the connector only the access you intend.
