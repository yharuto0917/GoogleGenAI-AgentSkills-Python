#!/usr/bin/env python3
"""
Commit message validator for various conventions.

Supports:
- Conventional Commits
- Semantic Commit Messages
- Japanese best practices
"""

import re
import sys
from typing import Tuple, List


# Conventional Commits types
CONVENTIONAL_TYPES = [
    'feat', 'fix', 'docs', 'style', 'refactor',
    'perf', 'test', 'build', 'ci', 'chore', 'revert'
]


def validate_conventional_commits(message: str) -> Tuple[bool, List[str]]:
    """
    Validate against Conventional Commits specification.

    Format: <type>[optional scope]: <description>

    Example: feat(auth): add login functionality
    """
    errors = []

    # Check basic format
    pattern = r'^([\w-]+)(\([a-z0-9-]+\))?: .+$'
    if not re.match(pattern, message.split('\n')[0]):
        errors.append("Format should be: <type>[optional scope]: <description>")
        return False, errors

    # Extract type
    type_match = re.match(r'^([\w-]+)', message)
    if type_match:
        commit_type = type_match.group(1)
        if commit_type not in CONVENTIONAL_TYPES:
            errors.append(f"Type '{commit_type}' is not a valid Conventional Commit type")
            errors.append(f"Valid types: {', '.join(CONVENTIONAL_TYPES)}")

    # Check description length
    first_line = message.split('\n')[0]
    desc_start = first_line.find(':')
    if desc_start != -1:
        description = first_line[desc_start + 1:].strip()
        if len(description) < 3:
            errors.append("Description is too short (minimum 3 characters)")
        if description[0].isupper():
            errors.append("Description should start with lowercase letter")
        if description.endswith('.'):
            errors.append("Description should not end with a period")

    # Check subject line length
    if len(first_line) > 72:
        errors.append(f"Subject line is too long ({len(first_line)} chars, max 72)")

    return len(errors) == 0, errors


def validate_semantic_commits(message: str) -> Tuple[bool, List[str]]:
    """
    Validate semantic commit messages (Angular style).

    Similar to Conventional Commits but may include additional types.
    """
    # For now, use Conventional Commits validation as base
    # Can be extended with additional semantic rules
    return validate_conventional_commits(message)


def validate_japanese_practices(message: str) -> Tuple[bool, List[str]]:
    """
    Validate Japanese commit message best practices.

    Checks:
    - Appropriate use of Japanese characters
    - Message clarity
    - Common Japanese patterns
    """
    errors = []

    first_line = message.split('\n')[0]

    # Check if message is empty or too short
    if len(first_line.strip()) < 5:
        errors.append("メッセージが短すぎます（最低5文字）")

    # Check for period at end (common in Japanese)
    # In Japanese, ending with 。 is acceptable

    # Check for common issues
    if re.search(r'^[a-z]', first_line):
        # If starts with lowercase English, might want Conventional Commits
        errors.append("英語で書く場合はConventional Commitsの形式を検討してください")

    # Check length
    if len(first_line) > 50:
        errors.append(f"1行目が長すぎます（{len(first_line)}文字、推奨50文字以内）")

    return len(errors) == 0, errors


def validate_message(message: str, convention: str = 'conventional') -> Tuple[bool, List[str]]:
    """
    Validate a commit message against specified convention.

    Args:
        message: The commit message to validate
        convention: One of 'conventional', 'semantic', 'japanese'

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    if not message or not message.strip():
        return False, ["Commit message is empty"]

    if convention == 'conventional':
        return validate_conventional_commits(message)
    elif convention == 'semantic':
        return validate_semantic_commits(message)
    elif convention == 'japanese':
        return validate_japanese_practices(message)
    else:
        return False, [f"Unknown convention: {convention}"]


def main():
    """CLI interface for commit message validation."""
    import argparse

    parser = argparse.ArgumentParser(description='Validate commit messages')
    parser.add_argument('message', nargs='?', help='Commit message to validate')
    parser.add_argument('--file', '-f', help='Read commit message from file')
    parser.add_argument('--convention', '-c',
                       choices=['conventional', 'semantic', 'japanese'],
                       default='conventional',
                       help='Convention to validate against')

    args = parser.parse_args()

    # Get message from file or argument
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                message = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
    elif args.message:
        message = args.message
    else:
        print("Error: Provide message as argument or use --file", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    # Validate
    is_valid, errors = validate_message(message, args.convention)

    if is_valid:
        print("✅ Commit message is valid!")
        sys.exit(0)
    else:
        print("❌ Commit message has issues:\n")
        for error in errors:
            print(f"  • {error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
