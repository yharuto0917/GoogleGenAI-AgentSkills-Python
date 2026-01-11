# Conventional Commits

Conventional Commits is a specification for adding human and machine-readable meaning to commit messages.

## Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Type

Must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes that affect the build system or external dependencies
- **ci**: Changes to CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

### Scope

Optional. A noun describing a section of the codebase, enclosed in parentheses.

Examples: `feat(parser):`, `fix(api):`, `docs(readme):`

### Description

- Short summary in present tense
- Not capitalized
- No period at the end
- Maximum 72 characters for the entire subject line

### Body

Optional. Provides additional contextual information.

- Separated from subject by a blank line
- Can be multiple paragraphs
- Explains **what** and **why**, not how

### Footer

Optional. References issues, breaking changes, etc.

- `BREAKING CHANGE:` followed by description
- `Closes #123` or `Fixes #456`

## Examples

### Simple feature
```
feat: add user authentication
```

### Feature with scope
```
feat(auth): implement OAuth2 login flow
```

### Bug fix with issue reference
```
fix: resolve memory leak in data processor

The processor was not releasing references to cached objects,
causing memory to grow unbounded over time.

Fixes #234
```

### Breaking change
```
feat!: drop support for Node 12

BREAKING CHANGE: Node 12 is no longer supported.
Minimum version is now Node 14.
```

### Multiple paragraphs in body
```
refactor: restructure authentication module

This refactor improves maintainability by separating concerns
between authentication and authorization.

The new structure makes it easier to add new authentication
providers in the future.
```

## Rules and Best Practices

1. **Type is required** - Every commit must start with a type
2. **Use lowercase** - Type and description should be lowercase
3. **Use imperative mood** - "add feature" not "added feature" or "adds feature"
4. **Be specific** - "fix: resolve null pointer in login" not "fix: bug fix"
5. **One logical change** - Each commit should contain one logical change
6. **No period at end** - The description should not end with a period
7. **50/72 rule** - Subject max 50 chars (soft limit), 72 chars (hard limit); body wrap at 72

## Benefits

- **Automated changelogs** - Generate changelogs from commit history
- **Semantic versioning** - Automatically determine version bumps
- **Better navigation** - Quickly find specific types of changes
- **Clear communication** - Team understands changes at a glance

## Common Mistakes

❌ `Fix bug` - Too vague, not following format
✅ `fix: resolve date parsing error in Safari`

❌ `feat: Added new feature for users` - "Added" instead of "add", capitalized
✅ `feat: add password reset functionality`

❌ `fixed login problem.` - Wrong type format, has period
✅ `fix: resolve login timeout issue`

❌ `Update README.md` - Missing type
✅ `docs: update installation instructions`
