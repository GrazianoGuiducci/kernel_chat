# User guide

## Your first conversation after adoption

Start with your real work. The kernel's working knowledge participates through
the instructions and sources saved in your chat environment. You can ask a
normal question, continue a topic or begin a new activity.

For example:

```text
Let's work on [topic]. Use the relevant sources and methods. When we learn
something reusable, help me preserve it where our next conversation can use it.
```

During initial setup, have the assistant reach one supplied method and connect
it to the work you are starting. The [chat setup guide](CHAT_SETUP.md) explains
file-based project setup and the existing ChatGPT repository route.

## Use the chat normally

You do not need to repeat a boot phrase or request a full repository load on
every turn. Use the principles already available and reach additional knowledge
when it can change the question, method or result. The conversation stays direct.

## Continue a relation in a new chat

Use the same project or connected source where you saved the kernel and current
context. Ask to continue the topic. The assistant uses `CURRENT.md` and the
relevant sources to recover the still-valid reasons and what has changed.

The topic may be research, a project, a recurring activity, a business question
or another context worth continuing. A project is optional.

In a repository-backed setup, these files live under `state/`. In a file-based
chat setup, they live in the selected knowledge area. Use the location that
actually exists. When a source is unavailable, supply or reconnect that source
rather than reconstructing its contents from a guess.

## Know the user-owned state surfaces

### `state/CURRENT.md` or the saved `CURRENT.md`

Keep the current point, why it matters, relevant changes, unfinished work and
any next action that has actually been decided. It is a reentry margin, not the
whole history or an instruction to execute an old plan automatically.

### `state/SOURCES.md` or the saved `SOURCES.md`

Point to original information and reusable methods with a reason to reach each
one. Availability does not mean every source must be loaded for every task.

### `state/INSTANCE.json` in the ChatGPT helper route

The Git/Python helper records package, repository, bridge and reported
installation identity here. It is setup metadata rather than project knowledge.
A file-based project in another chat app does not need this ChatGPT receipt.
The [adoption guide](ADOPTION_GUIDE.md) explains the distinction.

## Maintain continuity

When the work changes, preserve the knowledge that lets it continue: an accepted
correction, an important source, a changed direction, an unfinished relation or
the reason a method should now work differently.

With authorized writing access, the assistant updates the selected source and
reports what was saved. Otherwise it provides the complete updated file for you
to save in project knowledge or your repository. A response in one chat is not
by itself a saved update to the source used by the next chat.

Keep original facts in their own sources, reusable methods in their competence
and the current reentry margin in CURRENT. Avoid duplicate histories and never
put credentials in these files.

## Add a project or context later

Add the new context and its sources to CURRENT and SOURCES. The app's entry
usually stays the same: it connects the kernel to the knowledge location,
rather than hard-coding the first project as the kernel's identity.

## Add competences and metacompetences

A competence carries a usable way of understanding and working. It can combine
with others, adapt to a different situation or improve through experience.
A metacompetence helps form, combine or evolve those capabilities.

### Grow a competence in your instance

Begin with knowledge useful to your work. It may come from a successful result,
a source, an intention, a new possibility or a correction. Improve an existing
method when it owns that knowledge; give a distinct continuing capability its
own body when that is the useful form.

For example, a research method can live in `knowledge/source-comparison.md`
or a saved `source-comparison.md` in project knowledge. Preserve what it makes
possible, when it matters, the sources and reasons behind it, how to adapt it,
and what experience could change it. A short entry can reach a deeper guide.

Point to its actual location from SOURCES. Put a short pointer in CURRENT when
the current continuation depends on a correction. Keep the method itself in its
own file rather than replacing it with a summary in current state.

On a different task, use the method through its reasons and adapt it to the new
case. A result can make another competence useful or improve how future methods
are formed. Save that reusable difference in the competence that will use it.
The [competence source](../kernel/COMPETENCE.md) explains the deeper relation.

## Preserve unfinished work

Keep what remains to be done and the evidence already available. When a pending
request, result or receipt needs deeper continuity, use the optional
[operations knowledge](../operations/CURRENT.md) and its relevant files.
Retrieve or add those files to your knowledge area when that work needs them.
A saved next action is reconsidered from the present, not replayed automatically.

## Evolve the kernel

Work can improve a domain method and also the way the kernel understands,
forms or connects methods. Return reusable learning to the knowledge that will
participate next, preserving source, reason and what could change the conclusion.

When a useful relation is lost in a later result, trace where it was first lost:
source interpretation, saved method, entry, delivery or use. Correct that point
rather than adding another explanation downstream. The
[evolution source](../kernel/EVOLUTION.md) carries this method.

## Update package and bridge separately

A new upstream source is compared with your saved methods so local learning
survives. A source update does not require replacing app instructions when the
entry relation still fits.

For the ChatGPT repository helper, use the complete
[installation and update procedure](../INSTALL.md) and
[adapter guide](../adapters/chatgpt/README.md). Preview a selected bridge change,
keep its delivery digest, obtain the operator's copy/save report for that exact
text, publish the receipt and freshly read it before remote reentry.

For project knowledge, replace the selected files in the app and preserve their
source revision and useful local changes. Keep account settings and saved file
updates explicit so the next chat reaches the intended form.

## Source contact

Check upstream when a relevant change can improve the work. Preserve useful
observations without making every conversation a maintenance session. Updates
and public feedback are deliberate actions; the current source-contact method
is in [AGENTS.md](../AGENTS.md).

## Privacy and control

Use a private knowledge space or private standalone repository for private work.
A public fork is suitable for deliberately public contents. Keep passwords,
tokens and private keys out of knowledge files and account instructions. Grant
only the access intended for the work.
