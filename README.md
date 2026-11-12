# /configure-it-out

**Research first. Inspect the machine. Explain the changes. Get it working. Prove it.**

An agent skill for installing, configuring, and repairing software without turning every setup into speculative commands, repeated privilege requests, or an unnecessary custom application.

Created by Josh LaRue with Hermes Agent. Originally built for Hermes; the workflow is reusable by agents that support `SKILL.md` instructions and appropriate local tools.

## What it does

1. Inspect the actual target: OS, architecture, relevant hardware/resources, drivers, existing installation, configuration, and active workloads.
2. Read current official installation, compatibility, upgrade, and security documentation.
3. Choose the smallest supported change and define observable success checks.
4. Explain packages, settings, services, network changes, interruptions, and recovery limits before execution.
5. Prepare reviewable, task-specific setup scripts when useful. Keep normal work unprivileged and batch the bounded privileged phase where feasible.
6. Execute within the user's scope, inspect partial failures, and verify the real application path as the intended user.

No universal installer. No dependency on the skills that inspired it. No guarantee of exactly one password prompt: changed scope and native security gates still apply.

## Install in Hermes

Install directly from the published skill file:

```sh
hermes skills install https://raw.githubusercontent.com/teknightstick/configure-it-out/main/SKILL.md
```

Review the installer preview and security scan. Do not override a blocked verdict just to install this skill. Hermes supports installing referenced supporting files; check the installed template and references are present.

Then invoke:

```text
/configure-it-out get this project running locally using its official installation docs
/configure-it-out repair the existing setup without reinstalling or overwriting my configuration
/configure-it-out research the right GPU build for this machine; don't change anything yet
```

If an already-open Hermes session has not refreshed its slash commands, use `/reload-skills` or start a new session.

## Other skill-compatible agents

Clone this repository and place the directory in your agent's documented skills location, preserving `SKILL.md`, `references/`, and `templates/`. Follow your agent's own installation documentation; skill discovery and slash-command behavior vary.

The skill names Hermes tools such as `terminal`, `read_file`, and `search_files`. Other agents must map these to their supported equivalents while preserving the same permission and verification boundaries. Loading the text does not grant tool access or administrative permission. Non-Hermes integrations have not been tested.

## Safety boundaries

- Research-only requests remain read-only.
- No unrelated upgrades, destructive migrations, firmware flashes, spending, account creation, reboots, or public exposure are authorized merely by loading this skill.
- No permanent passwordless sudo, disabled approval controls, or retained root shell to reduce prompts.
- Existing configuration and unrelated working services must be preserved.
- A failed setup is inspected before retrying; rollback is not promised when restoration is incomplete or unsafe.
- Secrets stay out of scripts, command arguments, logs, and chat.
- An installed package, listening port, or successful command is not enough to claim the user's task is complete.

This is a procedural guide, not a sandbox or enforced security boundary. The executing agent, tools, operating system, and human approvals remain responsible for enforcing permissions. Review generated scripts before authorizing elevated execution.

## Included files

- `SKILL.md`: the workflow and governing principles.
- `templates/change-plan.md`: a practical change plan and verification receipt.
- `references/evaluation-cases.md`: eight proposed behavioral scenarios, including partial failure, privilege scope changes, and false-positive success.
- `references/sources.md`: upstream design provenance.
- `tests/test_package.py`: standard-library packaging and instruction-contract checks.

## Validation status

The initial skill was loaded successfully by Hermes and listed as enabled. Repository checks validate metadata, linked files, packaging hygiene, and the presence of important instruction boundaries. They do not prove model behavior, installation success, or system safety.

The eight behavioral scenarios are specifications, not completed evaluations. Linux, macOS, and Windows are intended targets for the workflow; this is not a claim that real setups have been exercised on every platform.

Run repository checks with Python 3.9 or newer, without installing dependencies:

```sh
python3 -m unittest discover -s tests -v
```

## Contributing

Keep the main skill focused on observable behavior. Add tool- or product-specific details to the relevant product skill rather than building an installer framework here. Include an evaluation scenario for a meaningful new rule. Describe what you actually tested and distinguish structural checks from behavioral evidence.

Do not submit credentials, personal machine inventories, private logs, or confidential configuration. For sensitive security concerns, avoid public reproduction details containing secrets; use GitHub's private vulnerability reporting if the repository provides it, otherwise request a private contact without disclosing the sensitive details.

## Inspiration and license

Inspired by the evidence-first and systematic workflows in `obra/superpowers`, the evaluation approach in `anthropics/skills`, and defensive scripting guidance in `wshobson/agents`. See [design provenance](references/sources.md). This is an original adaptation, not a bundled copy of those projects.

MIT licensed. See [LICENSE](LICENSE).
