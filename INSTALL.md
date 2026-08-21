# Install kernel_chat in ChatGPT

## Requirements

- Python 3;
- a GitHub account;
- a fork of this repository under your control;
- a ChatGPT account where GitHub repository access and Custom Instructions are
  available.

Host features depend on the current account, plan, connector, and turn. The
local setup cannot grant or prove them.

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

Existing state is kept by default. Use `--replace-state` only when you
deliberately want the initializer to replace both state files.

## 3. Commit the state

```bash
git add state/CURRENT.md state/SOURCES.md
git commit -m "Initialize kernel_chat state"
git push
```

Do not commit the configured Custom Instructions file. Do not store tokens,
passwords, private keys, or connector credentials in state.

## 4. Activate ChatGPT

1. Open `adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md`.
2. Copy the entire text into ChatGPT Custom Instructions.
3. Connect GitHub in the same ChatGPT account and grant only the repository
   access you intend.
4. Start a new chat and ask it to open `state/CURRENT.md` from your fork.

If the file is not accessible, the adapter is configured locally but the host
connection is not active. Fix the connection before relying on continuity.

## 5. Work normally

Ordinary questions should remain direct. When a missing durable relation can
change the result, the adapter points ChatGPT to the current state and then to
the relevant owner-native source.

When work changes the project's current point, ask ChatGPT to prepare the
smallest state update. A historical instruction or repository entry never
becomes automatic permission for an external effect.

## Update or remove

To update the package, merge or rebase upstream code without replacing your
`state/` files. Regenerate the local adapter when its template changes.

To remove the integration, delete the kernel text from Custom Instructions and
disconnect GitHub if you no longer want repository access. Your fork remains
ordinary user-owned data and can be archived or deleted separately.
