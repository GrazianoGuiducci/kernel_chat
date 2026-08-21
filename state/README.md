# User-owned state

The configurator creates `CURRENT.md` and `SOURCES.md` in this directory.

`CURRENT.md` is the compact reentry surface: where the work is, why it matters,
what is active, and what should happen next. `SOURCES.md` identifies the
owner-native sources that can change the result.

Keep state small. Point to project sources instead of copying their histories.
Do not store credentials, tokens, passwords, private keys, or raw sensitive
logs here.

The upstream package does not ship a configured user state. Your fork owns it.
