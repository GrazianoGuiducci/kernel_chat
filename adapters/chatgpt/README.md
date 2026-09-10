# ChatGPT adapter

The ChatGPT adapter translates the portable kernel into Custom Instructions
and a GitHub reentry path.

It is designed for ChatGPT's turn-reactive conversational surface. It does not
simulate an agent runtime, filesystem, hook, background process, or autonomous
continuation.

Generate the configured adapter from the repository root:

```bash
python scripts/configure.py \
  --github-user YOUR_GITHUB_USER \
  --repository YOUR_REPOSITORY \
  --project-name "YOUR PROJECT" \
  --project-source "https://github.com/YOU/YOUR_PROJECT"
```

The generated `CUSTOM_INSTRUCTIONS_CONFIGURED.md` is intentionally ignored by
Git. Copy it into ChatGPT Custom Instructions. The template remains versioned
here so adapter changes are inspectable.

GitHub access and Custom Instructions availability depend on the current
ChatGPT account and host. The adapter cannot grant those capabilities.

The compact entry separates project context (`state/CURRENT.md`) from kernel
and method knowledge (`AGENTS.md` and its selective owner links). These paths
do not require a boot on each new chat or put kernel methods in project state.

Rerunning configuration preserves the configured adapter and state by default.
Append `--preview-adapter` to the command above to print a candidate with no
writes. Append `--replace-adapter` only for deliberate local replacement;
`--replace-state` controls the two state files independently. Preview always
performs no writes, including when replacement flags are supplied.

Repository template, configured local file and installed account instructions
are distinct. Compare the candidate with your customizations and actual host
instructions before selecting an update. Installation is separate and cannot
be observed or performed by this script. See [update guidance](../../INSTALL.md#update-or-remove).
