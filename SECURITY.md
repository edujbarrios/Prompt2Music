# Security Policy

## Supported versions

Prompt2Music is currently in active MVP development. Security fixes are applied to the latest code on the `main` branch.

## Reporting a vulnerability

Please do not open a public GitHub issue for a vulnerability that could put users, deployments, or maintainers at risk.

Use GitHub's private vulnerability reporting feature for this repository when available. If private reporting is not available, contact the repository owner privately through an appropriate GitHub contact channel.

Please include enough information to reproduce and assess the issue, such as:

- affected component or route
- expected and observed behavior
- reproduction steps or proof of concept
- impact assessment
- suggested remediation, if known

Avoid including unrelated personal data, credentials, tokens, or secrets in reports.

## Scope

Prompt2Music does not intentionally persist chat prompts and does not send them to third-party AI providers. The application delegates musical prompt structuring to the open-source `text-to-music-prompt-structurer` Python package created and maintained by Eduardo J. Barrios (@edujbarrios).

Security issues in that backend library should be reported to its own repository when the issue originates there:

https://github.com/edujbarrios/text-to-music-prompt-structurer
