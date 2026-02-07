#!/bin/bash
# Release Script for Flash USDT
# Usage: ./scripts/release.sh [patch|minor|major]

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Check if we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    print_error "You must be on the main branch to create a release."
    print_info "Current branch: $CURRENT_BRANCH"
    exit 1
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    print_error "You have uncommitted changes. Please commit or stash them first."
    git status --short
    exit 1
fi

# Pull latest changes
print_info "Pulling latest changes from origin..."
git pull origin main

# Get version bump type
BUMP_TYPE=$1
if [ -z "$BUMP_TYPE" ]; then
    echo "Usage: ./scripts/release.sh [patch|minor|major]"
    echo ""
    echo "Version bump types:"
    echo "  patch - Bug fixes (1.0.0 → 1.0.1)"
    echo "  minor - New features (1.0.0 → 1.1.0)"
    echo "  major - Breaking changes (1.0.0 → 2.0.0)"
    exit 1
fi

if [[ ! "$BUMP_TYPE" =~ ^(patch|minor|major)$ ]]; then
    print_error "Invalid bump type: $BUMP_TYPE"
    print_info "Must be one of: patch, minor, major"
    exit 1
fi

# Get current version
CURRENT_VERSION=$(node -p "require('./package.json').version")
print_info "Current version: v$CURRENT_VERSION"

# Bump version
print_info "Bumping $BUMP_TYPE version..."
npm version $BUMP_TYPE --no-git-tag-version

# Get new version
NEW_VERSION=$(node -p "require('./package.json').version")
print_success "New version: v$NEW_VERSION"

# Update CHANGELOG.md
print_info "Please update CHANGELOG.md with changes for v$NEW_VERSION"
print_warning "Opening CHANGELOG.md in your default editor..."
${EDITOR:-nano} CHANGELOG.md

# Confirm changelog update
read -p "Have you updated CHANGELOG.md? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_error "Release cancelled. Please update CHANGELOG.md and try again."
    # Revert version bump
    git checkout package.json package-lock.json
    exit 1
fi

# Commit version bump and changelog
print_info "Committing version bump and changelog..."
git add package.json package-lock.json CHANGELOG.md
git commit -m "chore: release v$NEW_VERSION"

# Create git tag
print_info "Creating git tag v$NEW_VERSION..."
git tag -a "v$NEW_VERSION" -m "Release version $NEW_VERSION

See CHANGELOG.md for details."

# Show what will be done
echo ""
print_warning "About to:"
echo "  1. Push commits to origin/main"
echo "  2. Push tag v$NEW_VERSION"
echo "  3. Trigger automated build (GitHub Actions)"
echo ""

# Confirm push
read -p "Continue with release? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_error "Release cancelled."
    print_info "To undo changes:"
    echo "  git reset --hard HEAD~1"
    echo "  git tag -d v$NEW_VERSION"
    exit 1
fi

# Push to remote
print_info "Pushing to origin..."
git push origin main
git push origin "v$NEW_VERSION"

print_success "Release v$NEW_VERSION created successfully!"
echo ""
print_info "Next steps:"
echo "  1. GitHub Actions will automatically build desktop apps"
echo "  2. Check release at: https://github.com/PierPaolo19/llo/releases"
echo "  3. Add release notes if needed"
echo "  4. Test the release builds"
echo ""
print_success "Done! 🎉"
