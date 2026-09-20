# Portable kernel entry

This directory owns the provider-neutral operating entry for
`kernel_chat`.

`INSTRUCTIONS.template.md` is the semantic source installed into a receiving AI environment's persistent/custom instruction surface. It does not
contain the whole kernel. It tells the receiver where the kernel lives, how to
enter it, which constitutive owners remain reachable, how competences
participate and how reusable learning returns.

```text
host instructions
-> kernel source identity
-> AGENTS / CURRENT
-> pertinent kernel and competence owners
-> situated work
```

The constitutive operating owners named by the entry live in the selected
kernel source. User/domain sources can become pertinent during real work, and
optional research sources can deepen study; neither relation supplies missing
constitutive kernel definitions.

A chat is one possible receiving environment, not the definition of this carrier.
A chat that can retain persistent/custom operating instructions and reach a
durable source through GitHub, MCP, project knowledge, a filesystem, a
connector or equivalent means can host this kernel relation. The same semantic
entry can inhabit other receiving surfaces exposing equivalent capabilities.

This carrier can move part of what an agentic harness often externalizes as
fixed orchestration into the semantic operating layer: competence formation and
composition, source/owner relations, in-flow correction, continuity and
evolution through consequences can be represented and exercised as living
semantic capabilities. This does not turn semantic description into executable
runtime. Tools, scheduling, filesystem access, network access and material
effects remain the capabilities and authorities actually exposed by the host.

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

Another receiving environment may use project knowledge, a filesystem,
another repository service, MCP or another persistent source. The receiving
mechanism changes; the kernel relation does not.

`VERSION` identifies this portable-entry contract. Host-adapter
mechanics have their own identity and must not redefine the kernel.

The owner references in the canonical template use the package layout. When a
receiver's knowledge surface does not preserve directories, either the
installation step or a host adapter may translate those references. Translation
must preserve the same owner mapping; it does not rewrite or duplicate the
kernel logic.
