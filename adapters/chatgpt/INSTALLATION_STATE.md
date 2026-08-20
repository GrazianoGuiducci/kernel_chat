# ChatGPT Adapter Installation State

Status: not_installed
Source adapter: `adapters/chatgpt/CUSTOM_INSTRUCTIONS.md`
Configuration command: `python scripts/configure_chatgpt_adapter.py --github-user USER --repository REPOSITORY`
Configured output: `adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md` when generated locally
Behavioral activation: unverified
Repository binding: unresolved until fork/user configuration

## Distinctions

```text
adapter source exists
!= adapter configured
!= adapter installed in ChatGPT
!= GitHub connector available
!= repository reentry observed
!= behavioral activation
```

## Installation receipt fields

When a real test installation occurs, preserve only what is needed:

```text
configured repository binding
source revision installed
operator-reported or directly observable installation evidence
first fresh-instance test reference
replacement/removal condition
```

Do not store account secrets or credentials here.

The configured output is fork-local state and is ignored by Git by default. Generating it does not update this installation state automatically and does not imply host installation.
