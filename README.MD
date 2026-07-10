# Git Workflow Standards

## 1. Branch Naming Convention

### Format

`<type>/<short-description>`

### Allowed Types

* `feature` – New functionality
* `bugfix` – Bug fixes
* `hotfix` – Critical production fixes
* `refactor` – Code restructuring without behavior changes
* `chore` – Maintenance, dependency updates, configuration changes
* `docs` – Documentation updates
* `test` – Test-related changes

### Rules

* Use lowercase letters.
* Separate words with hyphens (`-`).
* Keep the description short and meaningful.
* One branch should address one feature, fix, or task.
* Avoid generic names such as `update`, `changes`, or `fixes`.

### Examples

* `feature/add-user-profile`
* `feature/payment-status-api`
* `bugfix/fix-login-validation`
* `hotfix/fix-production-auth-issue`
* `refactor/cleanup-auth-service`
* `chore/update-dependencies`
* `docs/update-api-guide`

---

## 2. Commit Message Convention

### Format

`<type>: <description>`

### Allowed Types

* `feat` – New feature
* `fix` – Bug fix
* `refactor` – Code refactoring
* `docs` – Documentation changes
* `test` – Test additions or updates
* `chore` – Maintenance tasks
* `style` – Formatting changes
* `perf` – Performance improvements
* `ci` – CI/CD changes

### Rules

* Use lowercase commit types.
* Write descriptions in the imperative mood.
* Keep commit messages concise and meaningful.
* One commit should represent one logical change.
* Avoid vague commit messages.

### Examples

* `feat: add user profile page`
* `fix: handle null response from api`
* `refactor: simplify authentication service`
* `docs: update onboarding guide`
* `test: add payment service unit tests`
* `chore: upgrade spring boot version`

### Avoid

* `updated code`
* `changes`
* `fixes`
* `misc updates`
* `wip`

---

## 3. Pull Request Guidelines

### Branch Creation

* Create a dedicated branch for every feature, bug fix, or task.
* Branches must follow the naming convention defined above.

### Commits

* Follow the commit message convention.
* Keep commits focused and logically grouped.
* Remove temporary or WIP commits before opening a PR.

### Pull Requests

* PR title should clearly describe the change.
* Keep PRs focused on a single objective.
* Ensure all tests and quality checks pass before requesting review.
* Obtain at least one approval before merging.

### Merging

* Prefer **Squash and Merge** to maintain a clean commit history.
* Multiple commits during development are allowed.
* The final merged commit should clearly describe the completed change.
* Delete merged branches after successful deployment.
