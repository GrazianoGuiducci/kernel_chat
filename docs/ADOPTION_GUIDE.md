# Adoption guide

`kernel_chat` can be studied without being installed, and it can be adopted as a
user-owned continuity instance with or without an active project.

Keep these distinct:

```text
study / evaluation
!= user-owned instance
!= configured ChatGPT bridge
!= operator-confirmed installed bridge incarnation receipt
!= repository reachability
!= exercised behavior
!= later assimilation
```

## Choose the relation you need

### Study only

Read the public package, architecture and kernel owners. No repository
configuration, Custom Instructions change, connector access or user state is
required merely to understand or review the package.

### Private continuity instance

A public GitHub repository cannot be made private by forking it. When the
continuity state should not be public, create a **private standalone
repository** under your control and initialize it from an identified
`kernel_chat` source revision or release.

Keep the canonical upstream relation visible so later source checks and updates
can be reconciled deliberately.

### Public continuity instance

When its state is intentionally public, a normal public fork is a valid
user-owned instance.

### Instance with an initial project

A project is optional. When one is selected during configuration, it becomes
the initial current context and owner-native source. It does not become the
identity of the kernel instance.

## What configuration creates

The configurator forms four distinct surfaces:

```text
state/INSTANCE.json
  instance/package/bridge identity and source-contact observation

state/CURRENT.md
  current user relation or context

state/SOURCES.md
  owner-native sources and why they may matter

adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md
  local generated host bridge, ignored by Git
```

`INSTANCE` is not user knowledge and does not prove installation. `CURRENT` is
not a task queue. `SOURCES` is not an activation registry. The configured
bridge is not the text currently installed in the account unless the operator
has copied and saved it there.

## ChatGPT activation

After configuration, the operator must manually copy the complete configured
bridge into ChatGPT Custom Instructions and save it. Repository-side success
cannot perform or independently verify this UI effect.

Use these evidence states when they matter:

```text
instance configured
-> host activation pending

operator copies/saves the current configured bridge
-> host action reported by operator

--confirm-host-installation
-> operator report persisted and bound to the already-reconciled configured
   bridge byte identity + target/provenance snapshot when known

new conversation reaches the instance and pertinent owners
-> host reachability observed

real use changes behavior as intended
-> host exercise evidence

later non-identical use retains the useful relation
-> stronger assimilation evidence
```

The confirmation receipt is still operator-reported evidence. It makes **which
bridge incarnation** was reported installed reconstructible through raw-byte
identity and the durable target/provenance relations available at confirmation;
it does not give the repository direct visibility into ChatGPT settings.

## Package update, available bridge and configured bridge are different

A newer package can change kernel owners, documentation, tests or package
mechanics without changing the stable host bridge.

```text
package update
!= bridge template currently available in the package
!= provenance of the preserved local configured bridge
!= repository targeted by that configured bridge
!= local configured bridge replacement
!= operator-confirmed installed bridge incarnation receipt
```

`state/INSTANCE.json` therefore keeps two bridge-template relations when they
matter:

```text
available_bridge_template_version
  what the current package offers

configured_bridge_template_version
  what template is known to have produced the preserved configured bridge
```

For a newly generated bridge both versions normally agree. During migration of
a pre-0.6 instance, however, a configured bridge may already exist before
`INSTANCE.json` exists. The configurator can preserve that bridge and its
digest, but it cannot truthfully infer which historical template produced it.
In that case it records:

```text
configured_bridge_template_version = unknown
```

`unknown` is a reconciliation signal, not automatic incompatibility. Preserve
the bridge until its fit is understood. Do not call it current merely because
the package now exposes a newer template.

A standard kernel_chat bridge also embeds the user-owned repository it reaches.
When a preserved legacy bridge names a repository different from the instance
being configured, the configurator stops before writes rather than creating a
receipt whose instance identity and bridge destination disagree.

After adopting a package change, `--refresh-instance` may update package identity
and the **available** bridge-template version while preserving configured-bridge
identity/provenance, source-contact observations and user state. If the local
bridge bytes changed independently, refresh leaves the persisted configured
identity untouched so validation can continue to expose the drift.

Preview a bridge candidate before replacement. `--replace-adapter` explicitly
regenerates the local configured bridge from the package's current template, so
that operation can establish its configured byte identity, template provenance
and repository target. For an already-existing INSTANCE it preserves
`instance_repository`; repository-identity migration is a separate effect. It
marks the local/host relation unconfirmed because replacing a local file does
not change ChatGPT.

After the operator copies/saves the replacement, run:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --confirm-host-installation
```

The receipt stores the raw-byte digest and target/provenance snapshot of the
bridge incarnation the operator says was installed. If a later local replacement
changes the configured incarnation, the previous installed receipt remains
recoverable so validation can expose the drift.

User-owned `CURRENT`, `SOURCES`, competences and local knowledge survive package
updates unless the operator explicitly replaces them.

The new configured/installed target/provenance fields are additive under
`kernel_chat.instance.v1`. Older valid v1 receipts that do not contain those
optional fields remain readable; absence means legacy/unrecorded identity, not
automatic invalidity. A refresh can backfill a target only when the observed
local bytes still match the persisted configured digest.


## Source contact

`state/INSTANCE.json` can retain the last observed upstream revision/time and
whether a material delta was seen. `AGENTS.md` owns the policy for when a light
source check is useful.

This creates reconstructible source contact without a timer, daemon or
background monitor. A newer upstream revision is a possibility to inspect, not
an automatic update.

## Continue normally

Once adopted, ordinary conversation remains direct. Reentry occurs only when a
missing durable relation can change the result:

```text
missing user/context relation
-> state/CURRENT.md + pertinent owner-native source

missing kernel/method/maintenance relation
-> AGENTS.md + pertinent owner

unfinished causal/effect relation
-> operations/ when material
```

A new chat alone does not require a boot.
