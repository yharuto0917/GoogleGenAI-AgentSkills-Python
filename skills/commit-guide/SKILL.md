---
name: commit-guide
description: "Comprehensive guide for writing effective git commit messages with support for multiple conventions (Conventional Commits, Semantic Commits, Japanese practices). Use when: (1) Creating git commits - generate or validate commit messages, (2) Reviewing commit messages - suggest improvements based on best practices, (3) Setting up commit message guidelines for a project, (4) User explicitly asks about commit message conventions or best practices. Supports both English and Japanese commit messages."
---

# Commit Message Guide

A comprehensive toolkit for creating, validating, and reviewing git commit messages according to industry-standard conventions.

## Overview

This skill helps you write clear, consistent, and meaningful commit messages by providing:

- **Guidelines** for Conventional Commits, Semantic Commits, and Japanese best practices
- **Validation** scripts to check commit messages against conventions
- **Templates** for common commit scenarios
- **Examples** of good and bad commit messages

## Quick Start

### Generating a Commit Message

When creating a commit, analyze the changes (from `git diff` or `git status`) and generate an appropriate commit message following the project's convention.

**Process:**

1. Examine the changes to understand what was modified
2. Identify the type of change (feature, fix, docs, etc.)
3. Write a concise, descriptive message
4. Follow the chosen convention (default: Conventional Commits)

**Example:**

```
User changes: Added login form component with email validation

Generated message:
feat(auth): add login form with email validation

Implement login form component with:
- Email and password fields
- Client-side validation
- Error handling for invalid credentials
```

### Validating a Commit Message

Use the validation script to check if a commit message follows a specific convention:

```bash
python scripts/validate_commit.py "feat: add user profile" --convention conventional
```

Options:
- `--convention conventional` - Conventional Commits (default)
- `--convention semantic` - Semantic Commit Messages
- `--convention japanese` - Japanese best practices
- `--file FILEPATH` - Read message from file

### Reviewing and Improving Messages

When a user provides a commit message for review:

1. Identify which convention (if any) they're trying to follow
2. Check for common issues:
   - Missing or incorrect type prefix
   - Capitalization errors
   - Past tense instead of imperative mood
   - Too vague or too technical
   - Subject line too long (>72 characters)
3. Suggest specific improvements
4. Explain why the changes improve the message

## Commit Message Conventions

### Conventional Commits (Recommended)

Format: `<type>[optional scope]: <description>`

**Common types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation only
- `style` - Code style changes
- `refactor` - Code refactoring
- `perf` - Performance improvement
- `test` - Adding/updating tests
- `build` - Build system changes
- `ci` - CI configuration
- `chore` - Other changes

**Guidelines:**
- Use lowercase for type and description
- Use imperative mood ("add" not "added" or "adds")
- No period at end of subject line
- Subject line max 72 characters
- Separate body with blank line

**For detailed rules, examples, and best practices, see:**
- `references/conventional-commits.md` - Complete Conventional Commits guide
- `references/examples.md` - Extensive examples of good and bad messages

### Semantic Commit Messages

Similar to Conventional Commits but may include additional semantic types and Gitmoji support.

**See:** `references/semantic-commits.md` for complete guide including:
- Angular commit format
- Gitmoji conventions
- Semantic versioning integration
- Tools (commitlint, semantic-release)

### Japanese Best Practices

Guidelines for writing commit messages in Japanese.

**Format options:**
1. Simple: `動詞 + 対象 + 内容`
2. Prefixed: `[カテゴリ] 変更内容`
3. Hybrid: `feat: 日本語の説明`

**Key principles:**
- Use present tense (辞書形) not past tense
- Start with verb, omit subject
- Keep first line under 50 characters
- Be specific about what changed

**See:** `references/japanese-practices.md` for complete guide including:
- Format patterns
- Japanese translations of Conventional Commits types
- Common mistakes in Japanese
- When to use Japanese vs English

## Message Templates

Pre-written templates for common commit scenarios are available in `assets/templates/`:

- `feature.txt` - New feature commits
- `bugfix.txt` - Bug fix commits
- `refactor.txt` - Refactoring commits
- `breaking-change.txt` - Breaking changes with migration guide
- `docs.txt` - Documentation updates
- `performance.txt` - Performance improvements
- `japanese.txt` - Japanese language template

Use these as starting points and customize to your specific changes.

## Validation Script

The `scripts/validate_commit.py` script provides automated validation:

**Features:**
- Validates format compliance
- Checks type validity
- Verifies description quality
- Reports specific issues with helpful error messages

**Usage:**

```bash
# Validate a message
python scripts/validate_commit.py "feat: add new feature"

# Validate from file
python scripts/validate_commit.py --file COMMIT_EDITMSG

# Check against different conventions
python scripts/validate_commit.py "メッセージ" --convention japanese
```

**Exit codes:**
- 0 = Valid message
- 1 = Invalid message (errors printed to stderr)

## Best Practices

### When Creating Commits

1. **Make atomic commits** - One logical change per commit
2. **Write for readers** - Future developers (including you) will read this
3. **Be specific** - "fix login timeout" not "fix bug"
4. **Use present tense** - "add feature" not "added feature"
5. **Explain why, not what** - Code shows what changed, commit explains why

### Common Scenarios

**Adding a new feature:**
```
feat: add dark mode toggle

Implement theme switching with:
- Toggle button in settings
- Preference saved to localStorage
- Automatic OS preference detection
```

**Fixing a bug:**
```
fix: resolve memory leak in event listeners

Remove event listeners on component unmount
to prevent memory accumulation.

Fixes #234
```

**Updating documentation:**
```
docs: add API authentication guide

Document OAuth2 flow with code examples
for common authentication scenarios.
```

**Breaking changes:**
```
feat!: change API response format to camelCase

BREAKING CHANGE: All API responses now use camelCase.
Update client code accordingly.

Migration guide: docs/migration/v2.md
```

### Multi-line Messages

Use the body for:
- Explaining the "why" behind the change
- Describing implementation approach for complex changes
- Listing affected components or areas
- Referencing related issues or discussions

Keep the subject line concise and use the body for details.

## Reference Documentation

For comprehensive guides on each convention:

- **Conventional Commits**: `references/conventional-commits.md`
  - Full specification
  - All commit types explained
  - Rules and benefits
  - Common mistakes

- **Semantic Commits**: `references/semantic-commits.md`
  - Angular format
  - Gitmoji support
  - Semantic versioning integration
  - Tooling recommendations

- **Japanese Practices**: `references/japanese-practices.md`
  - Format patterns
  - Japanese type translations
  - When to use Japanese vs English
  - Hybrid approaches

- **Examples**: `references/examples.md`
  - Extensive good/bad examples
  - Real-world scenarios
  - Common mistakes
  - Multi-line commit examples

Load these references as needed based on the convention being used or when detailed guidance is required.

## Workflow Guide

### For Commit Creation

1. Analyze changes (from git diff or user description)
2. Identify the commit type (feat, fix, docs, etc.)
3. Determine if a scope is appropriate
4. Write subject line (max 72 chars, imperative mood, lowercase)
5. Add body if needed (explain why, not what)
6. Add footer for issue references or breaking changes
7. Validate against chosen convention

### For Commit Review

1. Identify which convention is being used
2. Check format compliance
3. Verify type is appropriate for the changes
4. Ensure description is clear and specific
5. Check for common mistakes (capitalization, tense, length)
6. Suggest improvements with explanations
7. Optionally run validation script

### For Project Setup

1. Ask which convention to use (or recommend Conventional Commits)
2. Decide on language (English, Japanese, or hybrid)
3. Set up commit message template in project
4. Configure validation tool (commitlint, husky)
5. Document the chosen convention in CONTRIBUTING.md
6. Provide examples for team reference

## Tips for Different Contexts

### Open Source Projects
- Use English for international collaboration
- Follow Conventional Commits for automation
- Enable semantic-release for automatic versioning
- Require conventional format in contribution guidelines

### Team Projects (Japanese)
- Consider hybrid approach: English types, Japanese descriptions
- Document your chosen convention clearly
- Use templates for consistency
- Review commit messages in code review

### Personal Projects
- Choose a simple, consistent format
- Don't over-engineer - simple messages are fine
- Focus on clarity for future you
- Consider Conventional Commits if you might open-source later

## Common Issues and Solutions

**Issue:** "My commits are always 'update' or 'fix'"
- **Solution:** Be more specific. What was updated? What was fixed?

**Issue:** "I don't know which type to use"
- **Solution:** See type descriptions in references/conventional-commits.md

**Issue:** "My team uses different conventions"
- **Solution:** Standardize on one convention and document it

**Issue:** "Japanese messages are too long"
- **Solution:** Use hybrid format (English type + Japanese description)

**Issue:** "I'm not sure if my message is good"
- **Solution:** Run validation script or ask for review
