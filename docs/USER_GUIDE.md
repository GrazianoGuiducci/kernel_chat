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

## Maintain state

Update state when one of these changes materially:

- the current point or next movement;
- an accepted correction;
- an owner-native source;
- unfinished work that should remain visible;
- a verified boundary;
- a reusable way of understanding or working.

Do not store ordinary chat, duplicate summaries, credentials, or whole project
histories. A short state with accurate pointers is more useful than a large
memory dump.

## Add competences and metacompetences

Link a competence from `state/SOURCES.md` when it owns a way of working that can
change the project result. Do not copy it into the kernel merely to make it
visible.

A metacompetence carries comprehension developed through experience so it can
be operated, integrated, and evolved in another situation. Its instruction
file is a usable adapter; later changed behavior is the evidence that the
comprehension was assimilated.

## Preserve unfinished work

Use the `Open work` section in `state/CURRENT.md` for the causal remainder that
should survive the conversation. Describe what is unfinished and what evidence
exists. Do not turn it into an automatic task queue or authority to execute an
old instruction.

If work would lose a material cursor, pending relation, result, or effect
receipt between conversations, use the optional [`operations/`](../operations/)
organ. Keep it cold when nothing there changes continuation. Version `0.4.0`
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
