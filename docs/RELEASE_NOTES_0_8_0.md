# kernel_chat 0.8.0

`kernel_chat 0.8.0` deepens FDLA with consequence-aware temporal recomposition
while preserving the existing in-flow correction relation.

## Main change

A later consequence or new evidence can make a relation understandable that was
not available in the earlier field. FDLA now preserves these as distinct when
material:

```text
what happened
!= what was understood then
!= what is understood now
```

The current understanding is not narrated backward as earlier knowledge, and an
earlier faithful interpretation is not frozen after a material consequence
changes what can now be understood.

AGENTS exposes the later-consequence condition to the FDLA owner. Structural
validation and the independent rendered Markdown consumer proof protect that
route, while README and Architecture expose the broadened current capability.

## Compatibility

- existing in-flow FDLA remains valid;
- portable entry remains 3.0.0;
- instance schema remains `kernel_chat.instance.v1`;
- configurator, ChatGPT adapter, state and operations contracts are unchanged;
- no configured bridge, installed host instruction or user-instance migration
  follows automatically from this release.

## Material review

Reviewed semantic candidate:
`ac74126f0cad31b6926e72b184df3ad0104bcf20`.

- CI `35533925195`: success;
- validator: `valid=true`, `errors=[]`, `warnings=[]`;
- tests: `64/64`;
- matrix: `8/8` Python 3.11–3.14 × Ubuntu/Windows;
- review result: `no_material_blocker`.

The 0.8.0 promotion commit must receive its own green CI before protected tag
and immutable release publication.
