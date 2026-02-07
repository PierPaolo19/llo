# GitHub রিলিজ গাইড (Bengali)

Flash USDT প্রজেক্টের জন্য রিলিজ তৈরি এবং পরিচালনার সম্পূর্ণ বাংলা গাইড।

## সূচিপত্র

- [GitHub Releases কী?](#github-releases-কী)
- [দ্রুত শুরু করুন](#দ্রুত-শুরু-করুন)
- [ম্যানুয়াল রিলিজ প্রক্রিয়া](#ম্যানুয়াল-রিলিজ-প্রক্রিয়া)
- [স্বয়ংক্রিয় রিলিজ প্রক্রিয়া](#স্বয়ংক্রিয়-রিলিজ-প্রক্রিয়া)
- [ভার্সন নম্বরিং](#ভার্সন-নম্বরিং)
- [ডেস্কটপ অ্যাপ রিলিজ](#ডেস্কটপ-অ্যাপ-রিলিজ)
- [সমস্যা সমাধান](#সমস্যা-সমাধান)

## GitHub Releases কী?

GitHub Releases হল সফটওয়্যার ভার্সন প্যাকেজ করে ব্যবহারকারীদের কাছে পৌঁছানোর একটি উপায়। প্রতিটি রিলিজে থাকে:

- **ভার্সন ট্যাগ** (যেমন: v1.0.0, v2.1.3)
- **রিলিজ নোট** যা পরিবর্তনগুলো বর্ণনা করে
- **বাইনারি ফাইল** (ডেস্কটপ অ্যাপ, এক্সিকিউটেবল)
- **সোর্স কোড** স্ন্যাপশট

### রিলিজ তৈরি করা কেন জরুরি?

✅ **ব্যবহারকারীদের জন্য**: স্থিতিশীল ভার্সন সহজে ডাউনলোড  
✅ **ডেভেলপারদের জন্য**: প্রজেক্ট মাইলস্টোন ট্র্যাক করা  
✅ **ডকুমেন্টেশনের জন্য**: কী পরিবর্তন হয়েছে তা রেকর্ড  
✅ **ডিস্ট্রিবিউশনের জন্য**: প্রি-বিল্ট বাইনারি প্রদান  

## দ্রুত শুরু করুন

### আপনার প্রথম রিলিজ তৈরি করুন

```bash
# ১. নিশ্চিত করুন আপনি main ব্রাঞ্চে আছেন এবং latest কোড আছে
git checkout main
git pull origin main

# ২. package.json এ ভার্সন আপডেট করুন
npm version patch  # অথবা minor, অথবা major

# ৩. CHANGELOG.md আপডেট করুন পরিবর্তনগুলো দিয়ে
# CHANGELOG.md ম্যানুয়ালি এডিট করুন

# ৪. ভার্সন বাম্প কমিট করুন
git add package.json CHANGELOG.md
git commit -m "chore: bump version to v1.0.1"

# ৫. ট্যাগ তৈরি করে পুশ করুন
git tag -a v1.0.1 -m "Release v1.0.1"
git push origin main --tags

# ৬. ডেস্কটপ অ্যাপ্লিকেশন বিল্ড করুন
npm run desktop:build-all

# ৭. GitHub এ গিয়ে ট্যাগ থেকে রিলিজ তৈরি করুন
# dist/ ফোল্ডার থেকে বিল্ড করা ডেস্কটপ অ্যাপ আপলোড করুন
```

## ম্যানুয়াল রিলিজ প্রক্রিয়া

### ধাপ ১: রিলিজ প্রস্তুত করুন

**ভার্সন নম্বর আপডেট করুন:**

```bash
# বাগ ফিক্সের জন্য (1.0.0 → 1.0.1)
npm version patch

# নতুন ফিচারের জন্য (1.0.0 → 1.1.0)
npm version minor

# ব্রেকিং চেঞ্জের জন্য (1.0.0 → 2.0.0)
npm version major
```

**CHANGELOG.md আপডেট করুন:**

```markdown
## [1.0.1] - 2024-01-15

### যোগ করা হয়েছে
- নতুন ফিচার X
- Y এর জন্য সাপোর্ট

### ঠিক করা হয়েছে
- Z তে বাগ
- W এর সাথে সমস্যা

### পরিবর্তন করা হয়েছে
- A ডিপেনডেন্সি আপডেট
- B এর পারফরম্যান্স উন্নত
```

**পরিবর্তনগুলো কমিট করুন:**

```bash
git add package.json package-lock.json CHANGELOG.md
git commit -m "chore: release v1.0.1"
git push origin main
```

### ধাপ ২: Git ট্যাগ তৈরি করুন

```bash
# অ্যানোটেটেড ট্যাগ তৈরি করুন (সুপারিশকৃত)
git tag -a v1.0.1 -m "Release version 1.0.1

- ফিচার X যোগ করা হয়েছে
- বাগ Y ঠিক করা হয়েছে
- ডিপেনডেন্সি আপডেট করা হয়েছে"

# GitHub এ ট্যাগ পুশ করুন
git push origin v1.0.1

# অথবা সব ট্যাগ পুশ করুন
git push origin --tags
```

### ধাপ ৩: ডেস্কটপ অ্যাপ্লিকেশন বিল্ড করুন

```bash
# সব প্ল্যাটফর্মের জন্য বিল্ড (Windows, macOS, Linux)
npm run desktop:build-all

# অথবা নির্দিষ্ট প্ল্যাটফর্মের জন্য বিল্ড:
npm run desktop:build -- --win     # শুধু Windows
npm run desktop:build -- --mac     # শুধু macOS
npm run desktop:build -- --linux   # শুধু Linux
```

**বিল্ড ফাইলের অবস্থান:**
- Windows: `dist/Flash USDT Setup 1.0.1.exe`, `dist/FlashUSDT-1.0.1-portable.exe`
- macOS: `dist/Flash USDT-1.0.1.dmg`, `dist/Flash USDT-1.0.1-mac.zip`
- Linux: `dist/Flash USDT-1.0.1.AppImage`, `dist/flash-usdt_1.0.1_amd64.deb`

### ধাপ ৪: GitHub রিলিজ তৈরি করুন

**GitHub ওয়েব ইন্টারফেসের মাধ্যমে:**

1. GitHub এ আপনার রিপোজিটরিতে যান
2. ডান সাইডবারে "Releases" এ ক্লিক করুন
3. "Draft a new release" এ ক্লিক করুন
4. আপনার ট্যাগ সিলেক্ট করুন (v1.0.1)
5. রিলিজ টাইটেল দিন: "Flash USDT v1.0.1"
6. রিলিজ নোট লিখুন
7. `dist/` ফোল্ডার থেকে বিল্ড ফাইল আপলোড করুন
8. যদি প্রি-রিলিজ হয়, "This is a pre-release" চেক করুন
9. "Publish release" এ ক্লিক করুন

**GitHub CLI এর মাধ্যমে:**

```bash
# GitHub CLI ইনস্টল করুন (যদি প্রয়োজন হয়)
# https://cli.github.com/

# রিলিজ তৈরি করুন
gh release create v1.0.1 \
  --title "Flash USDT v1.0.1" \
  --notes-file RELEASE_NOTES.md \
  dist/*.exe \
  dist/*.dmg \
  dist/*.AppImage \
  dist/*.deb
```

### ধাপ ৫: রিলিজ ঘোষণা করুন

- README.md আপডেট করুন সর্বশেষ ভার্সন ব্যাজ দিয়ে
- আলোচনা/ফোরামে পোস্ট করুন
- সোশ্যাল মিডিয়ায় ব্যবহারকারীদের জানান
- প্রয়োজন হলে ডকুমেন্টেশন আপডেট করুন

## স্বয়ংক্রিয় রিলিজ প্রক্রিয়া

আমরা স্বয়ংক্রিয় রিলিজের জন্য GitHub Actions ওয়ার্কফ্লো প্রদান করি।

### রিলিজ ওয়ার্কফ্লো ব্যবহার করা

**স্বয়ংক্রিয় রিলিজ ট্রিগার করুন:**

```bash
# ১. ভার্সন ট্যাগ তৈরি করে পুশ করুন
git tag v1.0.1
git push origin v1.0.1

# ২. GitHub Actions স্বয়ংক্রিয়ভাবে:
#    - Windows, macOS, Linux এর জন্য ডেস্কটপ অ্যাপ বিল্ড করবে
#    - GitHub রিলিজ তৈরি করবে
#    - সব বিল্ড ফাইল আপলোড করবে
#    - রিলিজ নোট তৈরি করবে
```

## ভার্সন নম্বরিং

আমরা [Semantic Versioning](https://semver.org/) (SemVer) অনুসরণ করি:

### ফরম্যাট: MAJOR.MINOR.PATCH

**MAJOR** (1.0.0 → 2.0.0):
- ব্রেকিং চেঞ্জ
- API এর সাথে incompatible পরিবর্তন
- মেজর রিরাইট

**MINOR** (1.0.0 → 1.1.0):
- নতুন ফিচার
- ব্যাকওয়ার্ড-কমপ্যাটিবল যোগ
- নতুন ফাংশনালিটি

**PATCH** (1.0.0 → 1.0.1):
- বাগ ফিক্স
- সিকিউরিটি প্যাচ
- ছোট উন্নতি

### উদাহরণ

- `1.0.0` - প্রথম স্থিতিশীল রিলিজ
- `1.0.1` - বাগ ফিক্স রিলিজ
- `1.1.0` - নতুন ফিচার রিলিজ
- `2.0.0` - ব্রেকিং চেঞ্জ সহ মেজর আপডেট
- `1.0.0-alpha.1` - আলফা প্রি-রিলিজ
- `1.0.0-beta.1` - বিটা প্রি-রিলিজ
- `1.0.0-rc.1` - রিলিজ ক্যান্ডিডেট

## ডেস্কটপ অ্যাপ রিলিজ

### সব প্ল্যাটফর্মের জন্য বিল্ড করা

```bash
# প্রথমে ডিপেনডেন্সি ইনস্টল করুন
npm install

# সব প্ল্যাটফর্মের জন্য বিল্ড করুন
npm run desktop:build-all
```

**বিল্ড প্রয়োজনীয়তা:**

- **Windows বিল্ড**: Windows, macOS, অথবা Linux এ বিল্ড করা যায়
- **macOS বিল্ড**: অবশ্যই macOS এ বিল্ড করতে হবে (macOS এবং Xcode প্রয়োজন)
- **Linux বিল্ড**: Linux অথবা macOS এ বিল্ড করা যায়

### প্ল্যাটফর্ম-নির্দিষ্ট বিল্ড

```bash
# Windows
npm run desktop:build -- --win

# macOS
npm run desktop:build -- --mac

# Linux
npm run desktop:build -- --linux
```

### বিল্ড আউটপুট

**Windows:**
- `Flash USDT Setup X.X.X.exe` - NSIS ইনস্টলার (সুপারিশকৃত)
- `FlashUSDT-X.X.X-portable.exe` - পোর্টেবল এক্সিকিউটেবল

**macOS:**
- `Flash USDT-X.X.X.dmg` - DMG ইনস্টলার (সুপারিশকৃত)
- `Flash USDT-X.X.X-mac.zip` - ZIP আর্কাইভ

**Linux:**
- `Flash USDT-X.X.X.AppImage` - AppImage (ইউনিভার্সাল, সুপারিশকৃত)
- `flash-usdt_X.X.X_amd64.deb` - DEB প্যাকেজ (Debian/Ubuntu)

### রিলিজ করার আগে টেস্টিং

```bash
# ডেস্কটপ অ্যাপ লোকালি টেস্ট করুন
npm run desktop

# প্রোডাকশন মোডে টেস্ট করুন
NODE_ENV=production npm run desktop
```

**ডেস্কটপ অ্যাপ রিলিজ করার আগে চেকলিস্ট:**

- [ ] অ্যাপ সফলভাবে লঞ্চ হয়
- [ ] সব ফিচার সঠিকভাবে কাজ করে
- [ ] MetaMask কানেকশন কাজ করে
- [ ] নেটওয়ার্ক সুইচিং কাজ করে
- [ ] কোনো কনসোল এরর নেই
- [ ] UI সঠিকভাবে দেখায়
- [ ] About সেকশনে ভার্সন নম্বর সঠিক

## সমস্যা সমাধান

### ট্যাগ ইতিমধ্যে বিদ্যমান

```bash
# লোকাল ট্যাগ ডিলিট করুন
git tag -d v1.0.1

# রিমোট ট্যাগ ডিলিট করুন
git push origin :refs/tags/v1.0.1

# নতুন ট্যাগ তৈরি করুন
git tag -a v1.0.1 -m "Release v1.0.1"
git push origin v1.0.1
```

### বিল্ড ফেইল হয়

```bash
# ক্যাশ ক্লিয়ার করে রিবিল্ড করুন
rm -rf node_modules dist
npm install
npm run desktop:build-all
```

### রিলিজ আপলোড ফেইল হয়

```bash
# GitHub CLI দিয়ে রিট্রাই করুন
gh release delete v1.0.1 --yes
gh release create v1.0.1 --title "Flash USDT v1.0.1" dist/*
```

### ভুল ভার্সন নম্বর

```bash
# ভার্সন বাম্প আনডু করুন (পুশ করার আগে)
git reset --hard HEAD~1
npm version [সঠিক-ভার্সন]
```

## দ্রুত রেফারেন্স

### সাধারণ কমান্ড

```bash
# প্যাচ রিলিজ তৈরি করুন
npm version patch && git push --follow-tags

# মাইনর রিলিজ তৈরি করুন
npm version minor && git push --follow-tags

# মেজর রিলিজ তৈরি করুন
npm version major && git push --follow-tags

# সব প্ল্যাটফর্মের জন্য বিল্ড করুন
npm run desktop:build-all

# GitHub CLI দিয়ে রিলিজ তৈরি করুন
gh release create v1.0.1 --generate-notes dist/*

# সব রিলিজ দেখুন
gh release list

# নির্দিষ্ট রিলিজ দেখুন
gh release view v1.0.1
```

## রিসোর্স

- [Semantic Versioning](https://semver.org/)
- [GitHub Releases Documentation](https://docs.github.com/en/repositories/releasing-projects-on-github)
- [Electron Builder Documentation](https://www.electron.build/)
- [Keep a Changelog](https://keepachangelog.com/)

## সাহায্য প্রয়োজন?

- [সমস্যা সমাধান](#সমস্যা-সমাধান) সেকশন দেখুন
- [CONTRIBUTING.md](../CONTRIBUTING.md) দেখুন
- GitHub এ issue খুলুন
- আমাদের কমিউনিটি আলোচনায় যোগ দিন

---

**English Guide**: [RELEASES.md](RELEASES.md)
