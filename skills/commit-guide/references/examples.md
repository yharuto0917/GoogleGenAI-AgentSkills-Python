# Commit Message Examples

A comprehensive collection of good and bad commit message examples across various scenarios.

## Table of Contents

- [Features](#features)
- [Bug Fixes](#bug-fixes)
- [Documentation](#documentation)
- [Refactoring](#refactoring)
- [Performance](#performance)
- [Tests](#tests)
- [Breaking Changes](#breaking-changes)
- [Common Mistakes](#common-mistakes)

## Features

### Good Examples

```
feat: add user profile page

Create a new profile page where users can view and edit
their personal information, avatar, and preferences.
```

```
feat(auth): implement two-factor authentication

Add 2FA support using TOTP (Time-based One-Time Password).
Users can enable 2FA in their security settings.

Closes #789
```

```
feat: support dark mode

Add theme toggle with automatic OS preference detection.
Theme preference is persisted in localStorage.
```

### Bad Examples

```
❌ added new feature
   Missing type prefix, past tense, too vague

✅ feat: add email notification system
```

```
❌ Feature: Add login
   Wrong type format (should be lowercase)

✅ feat: add login functionality
```

```
❌ new stuff
   No type, too vague, unprofessional

✅ feat: add user activity dashboard
```

## Bug Fixes

### Good Examples

```
fix: prevent memory leak in event listeners

Remove event listeners in cleanup function to prevent
memory leaks when components unmount.

Fixes #234
```

```
fix(api): handle null response from external service

Add null check before accessing response data.
Return appropriate error message to client.
```

```
fix: resolve race condition in data fetching

Use Promise.all() instead of sequential awaits to
prevent state updates from racing.
```

### Bad Examples

```
❌ fix bug
   Too vague - what bug?

✅ fix: resolve null pointer exception in login
```

```
❌ Fixed the thing that was broken
   Past tense, unprofessional, no specifics

✅ fix: resolve date parsing error in Safari
```

```
❌ oops
   No context, unprofessional

✅ fix: correct typo in API endpoint URL
```

## Documentation

### Good Examples

```
docs: add API authentication guide

Document the OAuth2 flow and provide code examples
for common authentication scenarios.
```

```
docs(readme): update installation instructions

Add troubleshooting section for common npm install errors.
Update Node.js version requirement to 14+.
```

```
docs: add JSDoc comments to utility functions

Improve code documentation for better IDE support
and developer experience.
```

### Bad Examples

```
❌ update docs
   Too vague - which docs? What changed?

✅ docs: add contributing guidelines
```

```
❌ documentation
   Not a commit message, just a category

✅ docs: document API rate limiting behavior
```

## Refactoring

### Good Examples

```
refactor: extract validation logic to separate module

Move form validation functions from components to
shared utility module for better reusability.
```

```
refactor(auth): simplify token refresh logic

Replace complex nested callbacks with async/await
for better readability and maintainability.
```

```
refactor: use TypeScript enums for user roles

Replace string literals with type-safe enums.
This prevents typos and improves autocomplete.
```

### Bad Examples

```
❌ code cleanup
   Too vague - what was cleaned up?

✅ refactor: remove unused imports and dead code
```

```
❌ refactor: make things better
   No specifics about what improved

✅ refactor: improve error handling in API calls
```

## Performance

### Good Examples

```
perf: optimize image loading with lazy loading

Implement intersection observer for images below fold.
Reduces initial page load time by 40%.
```

```
perf(database): add index on user_id column

Reduces average query time from 500ms to 50ms
for user lookup operations.
```

```
perf: memoize expensive calculations

Use React.memo and useMemo to prevent unnecessary
recalculations in render-heavy components.
```

### Bad Examples

```
❌ make it faster
   No specifics about what or how

✅ perf: reduce bundle size by code splitting
```

```
❌ perf: optimization
   Redundant - all perf commits are optimizations

✅ perf: reduce API response size with field filtering
```

## Tests

### Good Examples

```
test: add unit tests for authentication service

Cover login, logout, and token refresh scenarios.
Achieve 90% code coverage for auth module.
```

```
test(api): add integration tests for user endpoints

Test CRUD operations and error handling for
/api/users endpoint.
```

```
test: fix flaky test in payment flow

Replace setTimeout with waitFor to eliminate
race condition in async test.
```

### Bad Examples

```
❌ add tests
   What tests? For what?

✅ test: add validation tests for user registration
```

```
❌ test: more tests
   Too vague, no context

✅ test: increase coverage for error handling
```

## Breaking Changes

### Good Examples

```
feat!: change API response format to camelCase

BREAKING CHANGE: All API responses now use camelCase
instead of snake_case for property names.

Migration guide:
- Update client code to use camelCase properties
- Use the provided migration script: npm run migrate

Closes #456
```

```
refactor!: remove deprecated authentication methods

BREAKING CHANGE: Remove legacy session-based auth.
All clients must migrate to JWT authentication.

See docs/migration/auth-v2.md for details.
```

### Bad Examples

```
❌ breaking change
   No context about what broke or why

✅ feat!: require API key for all endpoints
```

```
❌ BREAKING CHANGE: things changed
   Too vague - what things?

✅ feat!: replace Redux with Context API
```

## Common Mistakes

### Mistake 1: File names instead of changes

```
❌ update index.ts
❌ modify src/components/Header.tsx

✅ feat: add navigation menu to header
✅ fix: resolve PropTypes warning in header component
```

### Mistake 2: WIP or TODO commits

```
❌ WIP
❌ TODO: fix later
❌ checkpoint

✅ Use git stash for work in progress
✅ Or: feat: add basic structure for user profile (incomplete)
```

### Mistake 3: Combining unrelated changes

```
❌ fix: resolve login bug and update README and add tests

✅ Make 3 separate commits:
   fix: resolve login timeout issue
   docs: update README installation steps
   test: add integration tests for login flow
```

### Mistake 4: Too technical or too vague

```
❌ update variable x to use new algorithm
   Too technical without context

❌ improve stuff
   Too vague

✅ perf: optimize search algorithm using binary search
   Technical but with clear purpose
```

### Mistake 5: Capitalizing or adding periods

```
❌ feat: Add new feature.
❌ Fix: resolve bug

✅ feat: add new feature
✅ fix: resolve bug
```

### Mistake 6: Using past tense

```
❌ feat: added user dashboard
❌ fix: resolved memory leak
❌ docs: updated README

✅ feat: add user dashboard
✅ fix: resolve memory leak
✅ docs: update README
```

## Multi-line Commit Examples

### Example 1: Complex feature

```
feat(payment): integrate Stripe payment gateway

Implement complete payment flow with Stripe:
- Payment form with card validation
- Webhook handlers for payment events
- Receipt generation and email delivery
- Refund functionality in admin panel

Configuration:
- Add STRIPE_API_KEY to environment variables
- Set up webhook endpoint at /api/stripe/webhook

Testing:
- Use Stripe test keys for development
- Test cards provided in docs/testing.md

Closes #123, #124
```

### Example 2: Critical bug fix

```
fix: prevent data loss during concurrent edits

Race condition occurred when multiple users edited
the same document simultaneously. Last write would
overwrite all previous changes.

Solution:
- Implement optimistic locking with version numbers
- Show conflict resolution UI when version mismatch
- Allow users to merge changes manually

This fix prevents data loss but requires users to
resolve conflicts when detected.

Fixes #789
Related to #790, #791
```

### Example 3: Refactoring with migration

```
refactor: migrate from Moment.js to date-fns

Replace Moment.js with date-fns to reduce bundle size
(~67KB savings) and improve performance.

Changes:
- Update all date formatting calls
- Replace timezone handling logic
- Update tests to use new API

Migration notes:
- .format() → format()
- .add() → addDays(), addMonths(), etc.
- Timezone support now uses date-fns-tz

Breaking: Removes moment.js from dependencies.
Projects using moment directly will need to install it.

Closes #456
```

## Templates for Common Scenarios

### Adding a new page/component
```
feat: add [page/component name]

[Brief description of what it does]

Features:
- [Feature 1]
- [Feature 2]

[Optional: Technical details]
```

### Fixing a bug
```
fix: [brief description of bug]

[What was wrong]
[What caused it]
[How it's fixed]

Fixes #[issue number]
```

### Updating dependencies
```
build: update [dependency name] to [version]

[Reason for update]
[Any breaking changes or migration notes]
```

### Improving performance
```
perf: [what was optimized]

[Explanation of optimization]
[Performance metrics before/after if available]
```
