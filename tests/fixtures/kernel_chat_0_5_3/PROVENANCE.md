# kernel_chat 0.5.3 migration fixture provenance

Source-bound historical fixture for migration regression.

```text
canonical_repository: GrazianoGuiducci/kernel_chat
canonical_revision: bb3f3fd7ef311d664832f2002f16872fed9723af
source_version: 0.5.3
rendered:
  adapters/chatgpt/CUSTOM_INSTRUCTIONS.template.md
  templates/state/CURRENT.md
  templates/state/SOURCES.md
replacements:
  GITHUB_USER: example-user
  REPOSITORY: my-kernel
  DATE: 2026-09-10
  PROJECT_NAME: Research
  PROJECT_SOURCE: https://example.org/project
```

These fixtures are static and network-independent. They exercise the historical
shape and embedded relations; they are not evidence of a live old installation.
Byte-level LF/CRLF discriminants are constructed directly in tests so Git
checkout normalization cannot change the bytes under test.
