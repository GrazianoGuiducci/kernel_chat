# Install kernel_chat in ChatGPT

## Requirements

- Python 3;
- a GitHub account;
- a fork of this repository under your control;
- a ChatGPT account where GitHub repository access and Custom Instructions are
  available.

Host features depend on the current account, plan, connector, and turn. The
local setup cannot grant or prove them.

> [!IMPORTANT]
> **Repository setup is not ChatGPT activation.** If a coder or agent is doing
> the installation for an operator, it must tell the operator immediately after
> the configured adapter is generated that one manual ChatGPT UI action is
> still required. Until the operator confirms that action, report
> `repository configured / host activation pending`, not “installed in
> ChatGPT”.

## 1. Fork and clone

Fork `GrazianoGuiducci/kernel_chat`, then clone your fork:

```bash
git clone https://github.com/YOUR_GITHUB_USER/kernel_chat.git
cd kernel_chat
```

You may rename the fork. Pass the actual repository name to the configurator.

## 2. Initialize the adapter and first project

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --project-name "YOUR PROJECT" \
  --project-source "https://github.com/YOU/YOUR_PROJECT"
```

The script writes:

```text
adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md  local, ignored by Git
state/CURRENT.md                                    user-owned, commit it
state/SOURCES.md                                    user-owned, commit it
```

The script also prints the host boundary explicitly: it cannot install or
change ChatGPT Custom Instructions. For first adoption, the operator must still
copy the complete configured adapter into the ChatGPT UI and save it.

A coder or agent performing the setup must surface that required operator step
**now**, as soon as the configured adapter exists. Repository-side work can
continue, but host adoption remains pending until the UI action is confirmed.

Existing state and the local configured adapter are kept by default, even if
you rerun setup with different arguments. Use `--replace-state` to deliberately
replace both state files; use `--replace-adapter` independently to replace the
local adapter. Preview the candidate before choosing replacement as described
below. Configuration reports which files were kept or written.

## 3. Commit the state

```bash
git add state/CURRENT.md state/SOURCES.md
git commit -m "Initialize kernel_chat state"
git push
```

Do not commit the configured Custom Instructions file. Do not store tokens,
passwords, private keys, or connector credentials in state.

## 4. Operator action — activate ChatGPT

This step belongs to the operator through the ChatGPT UI.

1. Open `adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md`.
2. Copy the entire text into ChatGPT Custom Instructions from the ChatGPT UI.
3. Save the instructions.
4. Connect GitHub in the same ChatGPT account and grant only the repository
   access you intend.
5. Confirm to the coder or setup process that the UI step was completed.

The configurator and repository cannot perform or verify step 2 or step 3. A
coder must not claim those effects unless the operator has confirmed them.

## 5. Verify reachability

Start a new chat and ask it to open `state/CURRENT.md` from your fork. When a
kernel or method relation is needed, the host should be able to reach
`AGENTS.md` and only the pertinent owner.

If the file is not accessible, the adapter may be configured locally while the
host connection is not active. Fix the connection before relying on
continuity.

Keep the evidence levels distinct:

```text
repository configured
!= host instructions installed
!= repository reachability observed
!= behavioral assimilation
```

## 6. Work normally

Ordinary questions should remain direct. Project context is recovered through
`state/CURRENT.md` only when it matters; missing kernel or method knowledge uses
`AGENTS.md` and the pertinent owner instead. Neither route is a mandatory boot.

When work changes the project's current point, ask ChatGPT to prepare the
smallest state update. A historical instruction or repository entry never
becomes automatic permission for an external effect.

## Update or remove

To update the package, merge or rebase upstream code while preserving your
state, competences and local changes. A changed template does not update your
configured file or the instructions installed in ChatGPT.

Run the setup command with your actual configuration and `--preview-adapter`
to print the candidate without writing any files. Compare it with your local
configured adapter and the instructions actually installed in your account.
Preserve still-useful user changes. Preview takes precedence over replacement
flags and never initializes or replaces state.

When replacement is selected, rerun with `--replace-adapter`; state remains
preserved unless you also explicitly use `--replace-state`. Reconcile any
local customizations before separately copying the selected instructions into
the host settings. The configurator cannot read or change those settings and
does not infer which instructions are fresher from a repository version.

For a selected host update, the same operator boundary applies: the coder can
prepare or replace the local configured adapter, but must tell the operator
that the ChatGPT UI copy/save step remains separate and must not report the
host as updated until that action is confirmed.

The generated character count helps check the actual instruction field's
capacity. If it does not fit alongside your instructions, keep the entry and
essential behavior compact and leave deeper methods at their linked owners.
Do not assume a successful configuration means the host accepted the text.

In a new conversation, verify that the host can reach the project state and,
when a method is needed, the pertinent owner through `AGENTS.md`. Actual access
and use are separate from local configuration or structural validation.

To remove the integration, delete the kernel text from Custom Instructions and
disconnect GitHub if you no longer want repository access. Your fork remains
ordinary user-owned data and can be archived or deleted separately.
