# ChatGPT adapter

The ChatGPT adapter installs the provider-neutral conversational entry in
ChatGPT and records the host-specific configured/installed relation.

The semantic instruction source is:

`../conversational/INSTRUCTIONS.template.md`

It is designed to remain usable by conversational receivers other than ChatGPT.
This adapter owns ChatGPT configuration, delivery and receipt mechanics.
Runtime facilities remain those actually exposed by the current host; when a
capability is available and authorized it can participate without becoming part
of the adapter's semantic contract.

## Bridge contract

The configured ChatGPT bridge is rendered from the conversational instruction
source with:

```text
KERNEL_SOURCE = github:<instance repository>
```

The installed instructions then enter the repository through `AGENTS.md`,
reach `CURRENT` when continuity matters, and let the pertinent kernel and
competence owners participate.

`adapters/conversational/VERSION` identifies the portable instruction contract.
`adapters/chatgpt/VERSION` identifies ChatGPT adapter mechanics. Neither is the
root package `VERSION`, and a package update does not automatically require a
new host-instruction update.

## Assisted host setup

The adapter does not require the human operator to perform repository mechanics
that the current model/coder can already perform. Before configuration, observe
the actual host relation:

```text
repository access / write authority
!= filesystem or terminal access
!= Python execution
!= ChatGPT account-setting authority
```

Use an authorized local or remote execution surface, including a reachable VPS
or remote workspace, when available. If a required capability is missing,
surface that boundary and the smallest operator action needed. Do not simulate
a terminal, repository write or host-setting effect that the current environment
does not expose.

The supported reference configuration remains `scripts/configure.py`; another
mechanism can claim equivalent configuration only when it preserves and
verifies the same instance, bridge, provenance and receipt relations.

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

Retain the `confirmation_bridge_sha256` emitted for the bridge shown to the
operator. After the operator actually copies/saves **that delivered bridge
incarnation**, record the operator-reported effect with:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --confirm-host-installation \
  --expected-bridge-sha256 DELIVERED_BRIDGE_SHA256
```

The receipt stores the SHA-256 digest of the raw configured bridge bytes and
snapshots its repository target/template provenance when available. It does not
inspect ChatGPT settings directly. If the current bridge no longer matches the
delivered digest, confirmation is rejected instead of being transferred to a
newer incarnation.

Because the command changes only the local `state/INSTANCE.json`, publish the
receipt and make a fresh observation of the selected remote branch before a new
chat relies on it:

```bash
git add state/INSTANCE.json
git commit -m "Record ChatGPT host installation receipt"
git rev-parse HEAD
git push
git branch --show-current
git fetch --no-tags origin <BRANCH>
git rev-parse FETCH_HEAD
git show FETCH_HEAD:state/INSTANCE.json
```

The fetched commit must equal the expected local commit recorded before push.
If the remote has advanced, reconcile that state first. Confirm
`installed_operator_confirmed` in the fetched receipt before starting a new
remote conversation.

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

--confirm-host-installation + --expected-bridge-sha256 DELIVERED_BRIDGE_SHA256
  bind an operator-confirmed ChatGPT copy/save to the delivered,
  already-reconciled current configured bridge identity; INSTANCE only
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
