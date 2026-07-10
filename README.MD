# Git Workflow Standards

## 1. Branch Naming Convention

### Format

`<type>/<ticket-id>-<short-description>`

### Allowed Types

* `feature` – New functionality
* `bugfix` – Bug fixes
* `hotfix` – Critical production fixes
* `refactor` – Code restructuring without behavior changes
* `chore` – Maintenance, dependency updates, configuration changes
* `docs` – Documentation updates
* `test` – Test-related changes

### Rules

* Use lowercase letters for branch type and description.
* Separate words with hyphens (`-`).
* Include the ticket/story ID whenever available.
* Keep the description short and meaningful.
* One branch should address one feature, fix, or task.

### Examples

* `feature/abc-123-add-user-profile`
* `feature/abc-456-payment-status-api`
* `bugfix/abc-789-fix-login-validation`
* `refactor/abc-101-cleanup-auth-service`
* `chore/abc-102-update-dependencies`
* `docs/abc-103-update-api-guide`

---

## 2. Commit Message Convention

### Format

`<type>(<ticket-id>): <description>`

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
* Include the ticket/story ID whenever available.

### Examples

* `feat(ABC-123): add user profile page`
* `fix(ABC-456): handle null response from API`
* `refactor(ABC-789): simplify authentication service`
* `docs(ABC-101): update onboarding guide`
* `test(ABC-102): add payment service unit tests`
* `chore(ABC-103): upgrade spring boot version`

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
* Link the associated ticket/story.
* Keep PRs focused on a single objective.
* Ensure all tests and quality checks pass before requesting review.
* Obtain at least one approval before merging.

### Merging

* Prefer **Squash and Merge** to maintain a clean commit history.
* Delete merged branches after successful deployment.
