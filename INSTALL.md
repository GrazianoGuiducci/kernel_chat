# Install kernel_chat in ChatGPT

## Requirements

- Python 3.11–3.14;
- a GitHub account;
- a user-owned repository initialized from `kernel_chat`;
- a ChatGPT account where repository access and Custom Instructions are
  available.

Host features depend on the current account, plan, connector, and turn. Local
setup cannot grant or prove them.

> [!IMPORTANT]
> **Repository setup is not ChatGPT activation.** If a coder or agent is doing
> the installation for an operator, it must tell the operator immediately after
> the configured adapter is generated that one manual ChatGPT UI action is
> still required. Until the operator confirms that action, report
> `repository configured / host activation pending`, not “installed in
> ChatGPT”.

If you only want to study or evaluate the package, stop here: configuration is
not required. See [the adoption guide](docs/ADOPTION_GUIDE.md).

## 1. Create the user-owned instance

Choose the persistence relation that matches the information you intend to
store.

### Private continuity

A public GitHub repository cannot become a private fork. For non-public
continuity, create a **private standalone repository** and initialize it from an
identified upstream source/release.

One Git-based path that preserves history is:

```bash
git clone https://github.com/GrazianoGuiducci/kernel_chat.git YOUR_REPOSITORY
cd YOUR_REPOSITORY
git remote rename origin upstream
git remote add origin git@github.com:YOUR_GITHUB_USER/YOUR_REPOSITORY.git
git push -u origin main --tags
```

Create the destination repository as private before the push. The local
`upstream` remote keeps the canonical source relation explicit.

### Public continuity

If the state is intentionally public, fork `GrazianoGuiducci/kernel_chat`, then
clone the fork. You may rename the repository; pass its actual name to the
configurator.

The repository is now a persistence surface. It is not yet a configured or
installed ChatGPT kernel.

## 2. Configure the instance

### Start without a project

A project is not required:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY
```

### Start with an initial project/context

Provide both optional project arguments together:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --project-name "YOUR PROJECT" \
  --project-source "https://github.com/YOU/YOUR_PROJECT"
```

One project argument without the other is rejected rather than inventing
missing context.

The script writes or preserves:

```text
state/INSTANCE.json
  package / instance / bridge identity and source-contact observation

state/CURRENT.md
  current relation/context; project may be absent

state/SOURCES.md
  owner-native sources and their roles

adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md
  local configured bridge, ignored by Git
```

The script prints the host boundary explicitly: it cannot install or change
ChatGPT Custom Instructions.

Existing user state and the configured bridge are preserved by default. Use:

```text
--replace-state
  replace CURRENT and SOURCES only

--preview-adapter
  print a bridge candidate with no writes

--replace-adapter
  replace the local configured bridge from the current template,
  record its byte identity / repository target / template provenance,
  and mark the local/host relation as unconfirmed;
  for an existing INSTANCE this does not migrate instance_repository

--refresh-instance
  refresh package identity and the bridge template currently available
  while preserving configured-bridge identity/provenance and observations;
  local artifact drift remains visible rather than being accepted

--confirm-host-installation
  after the operator actually copied/saved the current configured bridge in
  ChatGPT, bind that operator confirmation to the already-reconciled configured
  bridge byte identity and semantic target/provenance; mutates INSTANCE only
```

`INSTANCE` has a different responsibility from `CURRENT` and `SOURCES`; package
or bridge identity can therefore change without replacing user context or
domain knowledge.

### Migrating an existing 0.5.x instance

An older instance can already contain:

```text
state/CURRENT.md
state/SOURCES.md
adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md
```

without having `state/INSTANCE.json`.

On the first 0.6 configuration, the existing configured bridge and user state
are preserved by default. The new receipt can know the current package version, the bridge template
currently available in that package, the raw-byte digest of the preserved
configured bridge and its repository target when observable. It cannot
necessarily know which historical template produced that bridge.

When provenance cannot be established truthfully, `INSTANCE` records:

```text
configured_bridge_template_version: "unknown"
```

This is not a failure and does not require immediate bridge replacement. It
means the local bridge should remain distinct from the currently available
template until its fit or origin is reconciled.

A standard 0.5.x bridge also contains the user-owned repository it reaches. If
that preserved bridge names a different repository from the instance being
configured, migration stops **before writes**. Use the repository identity that
matches the bridge, or deliberately select `--replace-adapter` to generate a
bridge for the intended instance. Do not preserve a bridge that silently points
to another continuity owner.

Keep these separate:

```text
available_bridge_template_version
!= configured_bridge_template_version
!= configured bridge repository target
!= Custom Instructions actually installed in ChatGPT
```

Use `--preview-adapter` to inspect the current candidate. Use
`--replace-adapter` only when a bridge replacement is actually selected; that
operation generates the bridge from the current template and can therefore
record its byte identity, repository target and provenance. If INSTANCE already
exists, supply its existing repository identity: bridge replacement does not
silently migrate the instance to another repository. Updating the local bridge
still does not update the ChatGPT UI.

## 3. Commit the durable state

```bash
git add state/INSTANCE.json state/CURRENT.md state/SOURCES.md
git commit -m "Initialize kernel_chat continuity"
git push
```

Do not commit `CUSTOM_INSTRUCTIONS_CONFIGURED.md`. Do not store tokens,
passwords, private keys, connector credentials, or raw sensitive logs in state.

## 4. Operator action — activate ChatGPT

This step belongs to the operator through the ChatGPT UI.

1. Open `adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md`.
2. Copy the entire text into ChatGPT Custom Instructions.
3. Save the instructions.
4. Connect GitHub in the same ChatGPT account and grant only the repository
   access you intend.
5. Confirm to the coder/setup process that the UI step was completed.

The configurator and repository cannot perform or independently verify step 2
or step 3.

After the operator has actually copied and saved the **current configured
bridge**, persist the operator-reported receipt:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --confirm-host-installation
```

This snapshots the SHA-256 digest of the raw configured bridge bytes, the
configured bridge repository target when observable and its template provenance
when known. If the local configured bridge differs from the persisted configured
receipt, confirmation stops rather than reconciling that drift. The command does
not inspect the ChatGPT UI and therefore remains operator-confirmed evidence,
not direct host proof.

The confirmation receipt is still only local until it is committed and pushed:

```bash
git add state/INSTANCE.json
git commit -m "Record ChatGPT host installation receipt"
git push
```

Before starting the new chat in step 5, read the remote receipt back — for
example with `git show @{upstream}:state/INSTANCE.json` — and verify that the
published state records `installed_operator_confirmed`.

Keep the states separate:

```text
repository / instance configured
!= operator-confirmed installed bridge incarnation receipt
!= repository reachability observed
!= behavior exercised
!= later behavioral assimilation
```

If the local configured bridge later changes, the last confirmed installed
digest remains recoverable. Validation can then expose that local/host drift
instead of silently treating the newer local file as already installed.

## 5. Verify reachability

Start a new chat. When continuity matters, ask it to reach the user-owned
instance and inspect `state/CURRENT.md`; when kernel or method knowledge matters,
it should be able to reach `AGENTS.md` and only the pertinent owner.

`state/INSTANCE.json` is useful when package/bridge/source-contact state itself
matters. It is not a mandatory read for ordinary work.

If files are not accessible, local configuration may be valid while host access
is unavailable. Fix that boundary before relying on continuity.

A successful reachability check is still not evidence of later assimilation.

## 6. Work normally

Ordinary questions should remain direct. Durable context is recovered only when
it can change the result. A project can be selected later by updating CURRENT
and SOURCES; no reinstall is required merely because the current context
changes.

When work changes the current relation, preserve the smallest useful state
update. Reusable methods belong in the competence/kernel owner that must use
them; state carries current reasons and pointers, not a duplicate method.

## Update the package

Package source, bridge template available in the package, configured bridge
provenance/repository/bytes and the last operator-confirmed installed bridge
have separate update states.

After integrating a selected upstream package change:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --refresh-instance
```

This refreshes package identity and the available bridge-template version in
`INSTANCE` without replacing user CURRENT/SOURCES or the local configured
bridge. It preserves the configured bridge's known provenance; it does not
relabel an old bridge as current merely because a new template is available.

If the bridge contract itself changed or you intentionally want a new local
bridge, preview first:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --preview-adapter
```

Then, only when selected:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --replace-adapter
```

A local bridge replacement does **not** update ChatGPT. The previous
operator-confirmed installed digest is preserved, while the local/host state is
marked unconfirmed. After the operator copies/saves the replacement in ChatGPT,
run `--confirm-host-installation` again to bind the new host confirmation to the
new configured digest.

A package update that leaves the bridge contract unchanged does not require a
host UI update merely because the package version changed.

Preserve user-owned state, competences and local knowledge across upstream
updates. A newer upstream source is a possibility to inspect, not permission to
overwrite local evolution.

## Source contact

`state/INSTANCE.json` can retain the last observed upstream revision/time and
whether a material delta was found. `AGENTS.md` defines the light source-contact
relation. There is no background timer or automatic update process.

## Remove the integration

Delete the kernel text from ChatGPT Custom Instructions and disconnect the
repository if you no longer want host access. The user-owned repository remains
ordinary data under your control and can be archived or deleted separately.
