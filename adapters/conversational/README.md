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

Install it with the source relation that the receiving environment can
actually reach. A host-specific adapter may render this automatically; it is
not required when the host already exposes a usable persistent instruction
surface and persistent source.

The current ChatGPT helper renders a GitHub source such as:

```text
github:owner/repository
```

Another conversational receiver may use project knowledge, a filesystem,
another repository service, MCP or another persistent source. The receiving
mechanism changes; the kernel relation does not.

`VERSION` identifies this portable instruction contract. Host-adapter
mechanics have their own identity and must not redefine the kernel.

The owner references in the canonical template use the package layout. When a
receiver's knowledge surface does not preserve directories, either the
installation step or a host adapter may translate those references. Translation
must preserve the same owner mapping; it does not rewrite or duplicate the
kernel logic.
