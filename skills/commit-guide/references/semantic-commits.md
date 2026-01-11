# Semantic Commit Messages

Semantic commit messages are a formalized way of structuring commit messages to convey meaning about the changes. This guide covers the Angular commit message format and related semantic approaches.

## Angular Commit Message Format

This is the format used by Angular and many other projects.

### Structure

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

Similar to Conventional Commits, but may include additional types:

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation
- **style**: Formatting, missing semicolons, etc
- **refactor**: Code restructuring
- **perf**: Performance improvement
- **test**: Adding or updating tests
- **build**: Build system or dependencies
- **ci**: CI configuration
- **chore**: Maintenance tasks
- **revert**: Revert a previous commit

### Scope

The scope specifies the place of the commit change. For example:

- `feat(router): add navigation guards`
- `fix(compiler): resolve template parsing issue`
- `docs(api): update endpoint documentation`

### Subject

- Use imperative, present tense: "change" not "changed" nor "changes"
- Don't capitalize first letter
- No period (.) at the end
- Maximum 50 characters

### Body

- Use imperative, present tense
- Includes motivation for the change
- Contrasts with previous behavior
- Wrap at 72 characters

### Footer

- Reference issues: `Closes #123`, `Fixes #456`
- Breaking changes: `BREAKING CHANGE: description`

## Gitmoji

An alternative semantic approach using emojis to categorize commits.

### Common Gitmojis

- ✨ `:sparkles:` - New feature
- 🐛 `:bug:` - Bug fix
- 📝 `:memo:` - Documentation
- 🎨 `:art:` - Code structure/format
- ⚡ `:zap:` - Performance
- 🔥 `:fire:` - Remove code/files
- ✅ `:white_check_mark:` - Tests
- 🔒 `:lock:` - Security
- ⬆️ `:arrow_up:` - Upgrade dependencies
- ⬇️ `:arrow_down:` - Downgrade dependencies
- 🔧 `:wrench:` - Configuration
- 🚀 `:rocket:` - Deploy

### Example

```
✨ feat(auth): add social login

:sparkles: feat(auth): add social login (with emoji code)
```

## Semantic Release

Semantic commit messages enable automated versioning and changelog generation.

### Version Bumping Rules

- `feat:` → Minor version bump (0.1.0 → 0.2.0)
- `fix:` → Patch version bump (0.1.0 → 0.1.1)
- `BREAKING CHANGE:` → Major version bump (0.1.0 → 1.0.0)

## Examples

### Feature with scope
```
feat(api): add rate limiting middleware

Implement rate limiting to prevent API abuse.
Uses sliding window algorithm with Redis backend.

Closes #789
```

### Bug fix
```
fix(parser): handle escaped quotes in JSON strings

Previously, strings like "foo\"bar" would fail to parse.
Now correctly handles all valid JSON escape sequences.
```

### Performance improvement
```
perf(database): optimize user query with indexing

Add composite index on (user_id, created_at) to speed up
timeline queries. Reduces average query time from 250ms to 15ms.
```

### Breaking change
```
refactor(api)!: rename endpoints for consistency

BREAKING CHANGE: The following endpoints have been renamed:
- /api/users/get -> /api/users
- /api/posts/create -> /api/posts

Update all API calls to use the new endpoint names.
```

### Revert
```
revert: feat(auth): add social login

This reverts commit 1234567.

Reverting due to OAuth2 library compatibility issues.
```

## Best Practices

1. **Be consistent** - Choose one format and stick to it across the project
2. **Atomic commits** - One commit per logical change
3. **Clear scope** - Use scopes that match your project structure
4. **Meaningful subject** - Describe what changed, not which files
5. **Explain why** - Use the body to explain motivation, not what changed (code shows that)

## Tools

- **commitlint** - Lint commit messages
- **semantic-release** - Automate versioning and changelogs
- **commitizen** - Interactive commit message CLI
- **husky** - Git hooks for enforcing commit format
