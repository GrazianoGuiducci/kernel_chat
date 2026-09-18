# ChatGPT adapter

The ChatGPT adapter translates the portable kernel into a small host-native
Custom Instructions bridge and a repository reentry path.

It is designed for ChatGPT's turn-reactive conversational surface. It does not
simulate an agent runtime, filesystem, hook, background process, scheduler or
autonomous continuation.

## Bridge contract

The bridge should stay shorter and more stable than the package it reaches.
Its job is to preserve only the constitutive entry relation:

```text
work directly when the present is sufficient
user-owned instance identity
CURRENT for missing durable user/context relation
AGENTS for missing kernel/method/maintenance relation
source/evidence/inference/capability/effect boundaries
no simulated host mechanisms
package / configured bridge / installed instructions kept distinct
```

Competence composition, FDLA, source contact, Evolution Feedback and deeper
maintenance knowledge remain in their owner-native repository bodies and are
reached only when pertinent.

`adapters/chatgpt/VERSION` identifies the bridge-template contract separately
from the root package `VERSION`. A package update does not automatically require
a new bridge or ChatGPT UI update.

## Configure without a project

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY
```

## Configure with an initial project/context

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --project-name "YOUR PROJECT" \
  --project-source "https://github.com/YOU/YOUR_PROJECT"
```

The generated `CUSTOM_INSTRUCTIONS_CONFIGURED.md` is intentionally ignored by
Git. The configurator only prepares this local projection; it cannot install or
modify account-level ChatGPT instructions.

It also creates or preserves `state/INSTANCE.json`, which records package/bridge
identity and source-contact observations separately from CURRENT/SOURCES.

A standard bridge embeds the user-owned repository it reaches. During legacy
migration, if the preserved bridge names a repository different from the
instance identity being formed, configuration stops before writes rather than
creating an internally inconsistent receipt.

## Operator-owned host activation

For first adoption, the operator must manually copy the complete configured
text into ChatGPT Custom Instructions and save it. If a coder or agent is
performing setup, it must surface that required UI action immediately.

Until the operator confirms the UI step, the truthful state is:

```text
repository configured / host activation pending
```

After the operator actually copies/saves the current configured bridge, record
that operator-reported effect with:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --confirm-host-installation
```

The receipt stores the SHA-256 digest of the raw configured bridge bytes and
snapshots its repository target/template provenance when available. It does not
inspect ChatGPT settings directly. If local bytes differ from the configured
receipt, confirmation refuses to reconcile that drift implicitly. This lets
later validation distinguish local configured state from the last
operator-confirmed host incarnation.

Because the command changes only the local `state/INSTANCE.json`, publish the
receipt before a new remote chat is expected to observe it:

```bash
git add state/INSTANCE.json
git commit -m "Record ChatGPT host installation receipt"
git push
```

Read the pushed receipt back from the remote/upstream branch before treating the
confirmation as available to the ChatGPT-side consumer.

GitHub access and Custom Instructions availability depend on the current
account and host. The adapter cannot grant or prove those capabilities.

## Update behavior

Package template, configured local file, configured provenance and the last
operator-confirmed installed digest are distinct.

Use:

```text
--preview-adapter
  inspect a candidate; no writes

--replace-adapter
  replace the local configured bridge from the current template and establish
  its configured byte/target/provenance identity;
  an existing instance_repository is not rebound;
  installed ChatGPT instructions remain unchanged until the operator separately
  copies/saves them

--refresh-instance
  refresh package identity and the bridge template currently available while
  preserving configured-bridge identity/provenance and host observations;
  observed local drift is not accepted as configured state;
  missing CURRENT/SOURCES in an existing instance remain missing until an
  explicit state replacement/restoration is selected

--confirm-host-installation
  bind an operator-confirmed ChatGPT copy/save to the already-reconciled current
  configured bridge identity; INSTANCE only
```

Rerunning configuration preserves user-owned CURRENT/SOURCES and the configured
bridge by default.

After an adopted package update, check whether the bridge template itself
changed before asking the operator to touch ChatGPT settings. A package version
change alone is not sufficient reason for host resynchronization.

When the bridge is replaced locally, `INSTANCE` marks the local/host relation as
unconfirmed while preserving the digest/target/provenance/time of any previous
operator-confirmed installed bridge. The old host incarnation therefore remains
reconstructible until the operator confirms the replacement.

## Reachability and evidence

After operator-confirmed installation, a new conversation can verify repository
reachability when selected:

- `state/CURRENT.md` for missing durable user/context relation;
- `AGENTS.md` and the pertinent owner for kernel/method knowledge;
- `state/INSTANCE.json` when package/bridge/source-contact identity matters.

An operator-confirmed installed digest is evidence about **which configured
artifact the operator reported installing**. It is not direct host inspection.
Reachability and later behavioral assimilation remain separate observations.

See [installation](../../INSTALL.md) and the
[adoption guide](../../docs/ADOPTION_GUIDE.md).
