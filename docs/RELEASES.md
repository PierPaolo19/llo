# GitHub Releases Guide

Complete guide for creating and managing releases for the Flash USDT project.

## Table of Contents

- [What are GitHub Releases?](#what-are-github-releases)
- [Quick Start](#quick-start)
- [Manual Release Process](#manual-release-process)
- [Automated Release Process](#automated-release-process)
- [Version Numbering](#version-numbering)
- [Release Notes Best Practices](#release-notes-best-practices)
- [Desktop App Releases](#desktop-app-releases)
- [Troubleshooting](#troubleshooting)

## What are GitHub Releases?

GitHub Releases are a way to package and distribute software versions to users. Each release includes:

- **Version tag** (e.g., v1.0.0, v2.1.3)
- **Release notes** describing changes
- **Binary files** (desktop apps, executables)
- **Source code** snapshot

### Why Create Releases?

✅ **For Users**: Easy download of stable versions  
✅ **For Developers**: Track project milestones  
✅ **For Documentation**: Record what changed and when  
✅ **For Distribution**: Provide pre-built binaries  

## Quick Start

### Creating Your First Release

```bash
# 1. Ensure you're on the main branch with latest code
git checkout main
git pull origin main

# 2. Update version in package.json
npm version patch  # or minor, or major

# 3. Update CHANGELOG.md with changes
# Edit CHANGELOG.md manually

# 4. Commit version bump
git add package.json CHANGELOG.md
git commit -m "chore: bump version to v1.0.1"

# 5. Create and push tag
git tag -a v1.0.1 -m "Release v1.0.1"
git push origin main --tags

# 6. Build desktop applications
npm run desktop:build-all

# 7. Go to GitHub and create release from tag
# Upload built desktop apps from dist/ folder
```

## Manual Release Process

### Step 1: Prepare the Release

**Update Version Number:**

```bash
# For bug fixes (1.0.0 → 1.0.1)
npm version patch

# For new features (1.0.0 → 1.1.0)
npm version minor

# For breaking changes (1.0.0 → 2.0.0)
npm version major
```

**Update CHANGELOG.md:**

```markdown
## [1.0.1] - 2024-01-15

### Added
- New feature X
- Support for Y

### Fixed
- Bug in Z
- Issue with W

### Changed
- Updated dependency A
- Improved performance of B
```

**Commit Changes:**

```bash
git add package.json package-lock.json CHANGELOG.md
git commit -m "chore: release v1.0.1"
git push origin main
```

### Step 2: Create Git Tag

```bash
# Create annotated tag (recommended)
git tag -a v1.0.1 -m "Release version 1.0.1

- Added feature X
- Fixed bug Y
- Updated dependencies"

# Push tag to GitHub
git push origin v1.0.1

# Or push all tags
git push origin --tags
```

### Step 3: Build Desktop Applications

```bash
# Build for all platforms (Windows, macOS, Linux)
npm run desktop:build-all

# Or build for specific platforms:
npm run desktop:build -- --win     # Windows only
npm run desktop:build -- --mac     # macOS only
npm run desktop:build -- --linux   # Linux only
```

**Build artifacts location:**
- Windows: `dist/Flash USDT Setup 1.0.1.exe`, `dist/FlashUSDT-1.0.1-portable.exe`
- macOS: `dist/Flash USDT-1.0.1.dmg`, `dist/Flash USDT-1.0.1-mac.zip`
- Linux: `dist/Flash USDT-1.0.1.AppImage`, `dist/flash-usdt_1.0.1_amd64.deb`

### Step 4: Create GitHub Release

**Via GitHub Web Interface:**

1. Go to your repository on GitHub
2. Click on "Releases" in the right sidebar
3. Click "Draft a new release"
4. Choose your tag (v1.0.1)
5. Set release title: "Flash USDT v1.0.1"
6. Write release notes (see template below)
7. Upload build artifacts from `dist/` folder
8. If it's a pre-release, check "This is a pre-release"
9. Click "Publish release"

**Via GitHub CLI:**

```bash
# Install GitHub CLI if needed
# https://cli.github.com/

# Create release
gh release create v1.0.1 \
  --title "Flash USDT v1.0.1" \
  --notes-file RELEASE_NOTES.md \
  dist/*.exe \
  dist/*.dmg \
  dist/*.AppImage \
  dist/*.deb
```

### Step 5: Announce the Release

- Update README.md with latest version badge
- Post on discussions/forums
- Notify users via social media
- Update documentation if needed

## Automated Release Process

We provide a GitHub Actions workflow for automated releases.

### Using the Release Workflow

**Trigger automated release:**

```bash
# 1. Create and push a version tag
git tag v1.0.1
git push origin v1.0.1

# 2. GitHub Actions will automatically:
#    - Build desktop apps for Windows, macOS, Linux
#    - Create GitHub release
#    - Upload all build artifacts
#    - Generate release notes
```

**What the workflow does:**

✅ Builds desktop apps for all platforms  
✅ Uploads builds to GitHub Releases  
✅ Creates release notes from commits  
✅ Marks release as pre-release if tag contains `-alpha`, `-beta`, or `-rc`  

### Workflow File Location

`.github/workflows/release.yml`

## Version Numbering

We follow [Semantic Versioning](https://semver.org/) (SemVer):

### Format: MAJOR.MINOR.PATCH

**MAJOR** (1.0.0 → 2.0.0):
- Breaking changes
- Incompatible API changes
- Major rewrites

**MINOR** (1.0.0 → 1.1.0):
- New features
- Backward-compatible additions
- New functionality

**PATCH** (1.0.0 → 1.0.1):
- Bug fixes
- Security patches
- Minor improvements

### Examples

- `1.0.0` - First stable release
- `1.0.1` - Bug fix release
- `1.1.0` - New feature release
- `2.0.0` - Major update with breaking changes
- `1.0.0-alpha.1` - Pre-release alpha version
- `1.0.0-beta.1` - Pre-release beta version
- `1.0.0-rc.1` - Release candidate

### Pre-release Versions

```bash
# Alpha (early testing)
npm version prerelease --preid=alpha
# → 1.0.0-alpha.0

# Beta (feature complete, testing)
npm version prerelease --preid=beta
# → 1.0.0-beta.0

# Release Candidate (final testing)
npm version prerelease --preid=rc
# → 1.0.0-rc.0
```

## Release Notes Best Practices

### Template

```markdown
## Flash USDT v1.0.1

Released: January 15, 2024

### 🎉 Highlights

Brief summary of the most important changes in this release.

### ✨ New Features

- Feature 1 description (#123)
- Feature 2 description (#124)

### 🐛 Bug Fixes

- Fixed issue with X (#125)
- Resolved problem with Y (#126)

### 🔧 Improvements

- Improved performance of Z
- Updated UI for better UX

### 📚 Documentation

- Added guide for ABC
- Updated tutorial for XYZ

### 🔒 Security

- Security patch for vulnerability CVE-XXXX
- Updated dependencies with security fixes

### ⚠️ Breaking Changes

- Changed API for function X (see migration guide)
- Removed deprecated feature Y

### 📦 Dependencies

- Updated ethers to v6.10.0
- Updated electron to v28.1.0

### 🙏 Contributors

Thanks to all contributors who made this release possible:
- @user1
- @user2

### 📥 Download

**Desktop Applications:**
- [Windows Installer (x64)](link)
- [Windows Portable (x64)](link)
- [macOS DMG](link)
- [Linux AppImage](link)
- [Linux DEB](link)

**Installation:**
See [Installation Guide](docs/GETTING_STARTED.md)

### 🔗 Full Changelog

[View all changes](CHANGELOG.md#101)
```

### Tips for Great Release Notes

✅ **Clear and concise** - Users should understand what changed  
✅ **Categorized** - Group changes by type (features, bugs, etc.)  
✅ **Linked** - Reference PRs and issues  
✅ **Visual** - Use emojis for quick scanning  
✅ **Complete** - Include breaking changes and migration guides  
✅ **Actionable** - Tell users what to do (update, migrate, etc.)  

## Desktop App Releases

### Building for All Platforms

```bash
# Install dependencies first
npm install

# Build for all platforms
npm run desktop:build-all
```

**Build requirements:**

- **Windows builds**: Can build on Windows, macOS, or Linux
- **macOS builds**: Must build on macOS (requires macOS and Xcode)
- **Linux builds**: Can build on Linux or macOS

### Platform-Specific Builds

```bash
# Windows
npm run desktop:build -- --win

# macOS
npm run desktop:build -- --mac

# Linux
npm run desktop:build -- --linux
```

### Build Outputs

**Windows:**
- `Flash USDT Setup X.X.X.exe` - NSIS installer (recommended)
- `FlashUSDT-X.X.X-portable.exe` - Portable executable

**macOS:**
- `Flash USDT-X.X.X.dmg` - DMG installer (recommended)
- `Flash USDT-X.X.X-mac.zip` - ZIP archive

**Linux:**
- `Flash USDT-X.X.X.AppImage` - AppImage (universal, recommended)
- `flash-usdt_X.X.X_amd64.deb` - DEB package (Debian/Ubuntu)

### Code Signing (Optional but Recommended)

**Windows:**
```bash
# Set environment variables for code signing
export CSC_LINK=/path/to/certificate.p12
export CSC_KEY_PASSWORD=your_password
npm run desktop:build -- --win
```

**macOS:**
```bash
# Set environment variables for code signing
export CSC_LINK=/path/to/certificate.p12
export CSC_KEY_PASSWORD=your_password
export APPLE_ID=your@email.com
export APPLE_ID_PASSWORD=app_specific_password
npm run desktop:build -- --mac
```

### Testing Before Release

```bash
# Test the desktop app locally
npm run desktop

# Test in production mode
NODE_ENV=production npm run desktop
```

**Checklist before releasing desktop apps:**

- [ ] App launches successfully
- [ ] All features work correctly
- [ ] MetaMask connection works
- [ ] Network switching works
- [ ] No console errors
- [ ] UI displays correctly
- [ ] Version number is correct in About section

## Troubleshooting

### Tag Already Exists

```bash
# Delete local tag
git tag -d v1.0.1

# Delete remote tag
git push origin :refs/tags/v1.0.1

# Create new tag
git tag -a v1.0.1 -m "Release v1.0.1"
git push origin v1.0.1
```

### Build Fails

```bash
# Clear cache and rebuild
rm -rf node_modules dist
npm install
npm run desktop:build-all
```

### Release Upload Fails

```bash
# Use GitHub CLI to retry
gh release delete v1.0.1 --yes
gh release create v1.0.1 --title "Flash USDT v1.0.1" dist/*
```

### Wrong Version Number

```bash
# Undo version bump (before pushing)
git reset --hard HEAD~1
npm version [correct-version]
```

## Quick Reference

### Common Commands

```bash
# Create patch release
npm version patch && git push --follow-tags

# Create minor release
npm version minor && git push --follow-tags

# Create major release
npm version major && git push --follow-tags

# Build all platforms
npm run desktop:build-all

# Create release with GitHub CLI
gh release create v1.0.1 --generate-notes dist/*

# List all releases
gh release list

# View specific release
gh release view v1.0.1
```

## Resources

- [Semantic Versioning](https://semver.org/)
- [GitHub Releases Documentation](https://docs.github.com/en/repositories/releasing-projects-on-github)
- [Electron Builder Documentation](https://www.electron.build/)
- [Keep a Changelog](https://keepachangelog.com/)

## Need Help?

- Check [Troubleshooting](#troubleshooting) section
- See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines
- Open an issue on GitHub
- Join our community discussions

---

**Bengali Guide**: [RELEASES_BENGALI.md](RELEASES_BENGALI.md)
