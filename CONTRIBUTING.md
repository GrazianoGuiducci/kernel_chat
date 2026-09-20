# Contributing to kernel_chat

Real use is part of how `kernel_chat` evolves. Testers, operators, developers and
capable AI coders are welcome to report what helped, what confused them, what
failed, and what new possibility became visible.

First-use impressions are valuable even when nothing is broken. A friction that
is obvious to a new user can disappear from view once the system is familiar.

## Evolution Feedback

Use a GitHub Issue for observed experience, questions, friction, unexpected
success, missing context or a possible improvement. The repository includes an
`Evolution Feedback` Issue template under `.github/ISSUE_TEMPLATE/`.

Useful feedback keeps these relations visible:

```text
kernel version / revision
host and coder or model
what you were trying to do
first impression
what helped
what was confusing or missing
what failed or worked unexpectedly well
new possibility noticed
suggested improvement
observed evidence / uncertainty
```

A coder may prepare this feedback from real use, but must ask the operator for
permission before publishing it. Do not turn a private support or project
session into public evidence without consent.

Do not include credentials, private repository contents, client material,
personal data, private logs, hidden runtime state or anything the operator has
not approved for public disclosure.

Feedback is evidence, not authority. One report can expose a useful direction
without automatically changing the kernel.

Security vulnerabilities are a separate reporting path. Do not publish
exploitable details or sensitive material as Evolution Feedback; follow
[SECURITY.md](SECURITY.md) instead.

## Concrete changes

If you already have a concrete source change, fork the repository, create a
focused branch and open a Pull Request. Keep the change tied to the observed
condition or attainable result it is meant to improve. Do not write directly to
the upstream `main` branch unless you are an authorized maintainer acting in
that owner role.

A useful Pull Request states:

- the source version or revision it started from;
- the real condition or feedback that motivated the change;
- the smallest owner-native surface changed;
- the expected or observed difference;
- validation performed;
- what remains unverified.

## Source freshness while testing

The canonical upstream is [GrazianoGuiducci/kernel_chat](https://github.com/GrazianoGuiducci/kernel_chat).
It supplies source updates and receives approved feedback; the configured user
repository owns the user’s project continuity. Inspect upstream `main` as well
as version/release signals, since source changes may precede a tag. If access
or submission is unavailable, state that limitation and return prepared feedback
to the operator without claiming an external effect.

During active use, a coder should keep a light relation to upstream. When the
last known source check is about seven days old, or when a current problem may
already have been addressed upstream, inspect the repository in read-only mode.
Start with `VERSION`, `CHANGELOG.md` and the latest release or relevant current
source. Read deeper only when a material difference appears.

This is not a timer, scheduler or automatic updater. Do not pull, merge, replace
local instructions or change the host merely because a newer source exists.
Explain a relevant delta and let the operator select any adoption effect.

## The return loop

```text
real use
-> first impressions / friction / useful surprise / new possibility
-> operator-approved Evolution Feedback
-> upstream issue or focused pull request
-> maintainer reconciliation
-> later source evolution
-> future user/coder source check
-> situated adoption when useful
-> new real use
```

The purpose is not to maximize reports. Preserve only feedback that can improve
future understanding, behavior, safety, usability or attainable results.
