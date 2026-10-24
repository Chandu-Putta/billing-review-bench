# pr6-A run2 (PR #11)

## Review
<!-- ccr-overview-v2 -->

### 🔵 Needs a closer look

The support authorization check lacks a lower bound, allowing arbitrarily large negative waiver amounts to reach the ledger.

<details open>
<summary><strong>2 open issues</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Reject negative and non-finite SUPPORT waiver amounts](https://github.com/Chandu-Putta/billing-review-bench/pull/11#discussion_r4365762834)
- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.png" alt="Medium severity" width="62" height="18" align="texttop"></picture> [Add boundary and unauthorized waiver regression tests](https://github.com/Chandu-Putta/billing-review-bench/pull/11#discussion_r4365762852)
</details>

<sub>Review effort: Balanced</sub>

## Inline comments

