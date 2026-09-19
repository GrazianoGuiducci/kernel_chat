# Conversational instructions

This directory owns the provider-neutral backend-instruction entry for
`kernel_chat`.

`INSTRUCTIONS.template.md` is the semantic source installed into a
conversational system's persistent/custom instruction surface. It does not
contain the whole kernel. It tells the receiver where the kernel lives, how to
enter it, which constitutive owners remain reachable, how competences
participate and how reusable learning returns.

```text
backend instructions
-> kernel source identity
-> AGENTS / CURRENT
-> pertinent kernel and competence owners
-> situated conversational movement
```

The placeholder is:

```text
{{KERNEL_SOURCE}}
```

A host adapter renders it with the source relation that host can actually
reach. The current ChatGPT helper renders a GitHub source such as:

```text
github:owner/repository
```

Another conversational receiver may use project knowledge, a filesystem,
another repository service, MCP or another persistent source. The receiving
mechanism changes; the kernel relation does not.

`VERSION` identifies this portable instruction contract. Host-adapter
mechanics have their own identity and must not redefine the kernel.
