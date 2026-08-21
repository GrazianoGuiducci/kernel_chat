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
