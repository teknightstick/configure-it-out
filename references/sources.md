# Design provenance

These published skills informed the process. This skill is an original adaptation, not a bundled copy or a dependency. Popularity is not proof of effectiveness; see evaluation-cases.md for proposed behavioral tests.

- obra/superpowers, verification-before-completion: require fresh execution evidence for completion claims. https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md
- obra/superpowers, systematic-debugging: investigate before fixing, test hypotheses minimally, and avoid stacking speculative changes. https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md
- obra/superpowers, writing-plans: specify exact changes, constraints and verification rather than vague tasks. https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
- anthropics/skills, skill-creator: evaluate realistic prompts and iterate from actual results, including comparisons without the skill. https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- wshobson/agents, bash-defensive-patterns: validate inputs, handle temporary files/failures safely, design reruns, and test error paths. https://github.com/wshobson/agents/blob/main/plugins/shell-scripting/skills/bash-defensive-patterns/SKILL.md

The hardware discovery, narrowly batched privilege, preservation, approval boundaries and honest recovery requirements reflect the user's requested workflow. They are not assertions that the source skills guarantee those behaviors.

Hermes skills/slash invocation reference: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
