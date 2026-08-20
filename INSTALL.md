# Configure the ChatGPT Adapter

The current ChatGPT adapter uses a GitHub repository owned or forked by the user as its durable reentry surface. A GitHub account is therefore required for this adapter.

Repository source, configured adapter text, installed Custom Instructions, GitHub access and observed behavior are different states. Completing one does not imply the next.

## 1. Fork or own the repository

Create a fork or another user-owned copy of this repository on GitHub. The adapter will point to:

```text
<github-user>/<repository>/state/CURRENT_PRESENT.md
```

Do not place access tokens or account secrets in repository files or Custom Instructions.

## 2. Configure the adapter locally

From the repository root, run:

```bash
python scripts/configure_chatgpt_adapter.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY
```

The command reads the reusable template and creates:

```text
adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md
```

It performs no network request and changes no ChatGPT setting. The generated file is fork-local configuration and is ignored by Git by default.

## 3. Install the complete text

Open the generated file and copy only the complete text below `## Complete text to install` into ChatGPT Custom Instructions, replacing the existing instruction text as one complete adapter.

Installation is a user/account action. Repository source or configured output does not prove that installation occurred.

## 4. Connect GitHub when available

Enable the GitHub connection available to the selected ChatGPT account and make the fork accessible to that host. Actual repository access depends on the host, account, connector permissions and current turn.

The adapter does not simulate access when GitHub is unavailable.

## 5. Use the conversation normally

Ordinary requests should use the current message and conversation directly. The repository enters only when a durable relation of continuity, source, competence or unfinished causal work can materially change the result.

```text
conversation sufficient
-> no repository reentry

durable relation matters
-> read state/CURRENT_PRESENT.md selectively

unfinished operational relation matters
-> read operations/CURRENT_STATE.md selectively
```

## Other cloud conversational providers

The shared repository structure is not intended to be limited to ChatGPT. Another cloud conversational or agentic provider may use the same core through a host-native adapter and its real repository-access mechanism.

No compatibility is claimed from similarity alone. Each provider must keep source configuration, installation, actual capability and effect authority distinct.

## Remove or replace

Remove or replace the complete Custom Instructions text in the host. A repository commit cannot update or remove an adapter already installed in an account.
