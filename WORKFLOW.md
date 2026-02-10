# How to Run from GitHub - Visual Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    GITHUB থেকে কিভাবে চালাবেন                 │
│                   How to Run from GitHub                         │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────┐
│  ধাপ ১ / Step 1 │
│   ডাউনলোড করুন  │
│    Download      │
└────────┬─────────┘
         │
         ▼
┌────────────────────────────────────┐
│  Option A: Git                     │
│  git clone github.com/PierPaolo19/llo │
│                                    │
│  Option B: ZIP Download            │
│  Download ZIP from GitHub page     │
└────────┬───────────────────────────┘
         │
         ▼
┌──────────────────┐
│  ধাপ ২ / Step 2 │
│  ফোল্ডারে যান    │
│  Go to folder    │
└────────┬─────────┘
         │
         ▼
┌────────────────────────────────────┐
│  cd llo                            │
│  (or cd Downloads/llo-main)        │
└────────┬───────────────────────────┘
         │
         ▼
┌──────────────────┐
│  ধাপ ৩ / Step 3 │
│  ইনস্টল করুন     │
│    Install       │
└────────┬─────────┘
         │
         ▼
┌────────────────────────────────────┐
│  pip install -r requirements.txt   │
│                                    │
│  Or:                               │
│  pip install web3 tronpy           │
└────────┬───────────────────────────┘
         │
         ▼
┌──────────────────┐
│  ধাপ ৪ / Step 4 │
│    চালান         │
│      Run         │
└────────┬─────────┘
         │
         ├──────────────────┬──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
┌─────────────────┐  ┌─────────────┐  ┌──────────────┐
│  Interactive    │  │  Command    │  │  Examples    │
│  Menu           │  │  Line       │  │              │
│                 │  │             │  │              │
│  python3        │  │  python3    │  │  python3     │
│  flash_usdt.py  │  │  cli.py     │  │  examples.py │
└─────────────────┘  └─────────────┘  └──────────────┘
         │                  │                  │
         └──────────────────┴──────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   🎉 SUCCESS! │
                    │   সফল হয়েছে!  │
                    └───────────────┘
```

---

## Quick Start Commands (Copy & Paste)

### Windows (Command Prompt):

```batch
REM Step 1 & 2: Download and navigate
cd %USERPROFILE%\Downloads\llo-main

REM Step 3: Install
pip install -r requirements.txt

REM Step 4: Run
python flash_usdt.py
```

### Mac/Linux (Terminal):

```bash
# Step 1 & 2: Clone and navigate
git clone https://github.com/PierPaolo19/llo.git
cd llo

# Step 3: Install
pip3 install -r requirements.txt

# Step 4: Run
python3 flash_usdt.py
```

---

## Decision Tree (সিদ্ধান্ত গাছ)

```
আপনি কি করতে চান?
What do you want to do?
        │
        ├─► ব্যালেন্স চেক করতে? (Check balance?)
        │   └─► python3 cli.py <network> <address>
        │
        ├─► টোকেন তথ্য দেখতে? (View token info?)
        │   └─► python3 cli.py <network> --info
        │
        ├─► মেনু দিয়ে ব্যবহার? (Use with menu?)
        │   └─► python3 flash_usdt.py
        │
        └─► উদাহরণ দেখতে? (See examples?)
            └─► python3 examples.py
```

---

## File Map (ফাইল ম্যাপ)

```
llo/
│
├── 🟢 START HERE (শুরু করুন এখানে)
│   ├── README.bn.md ................ বাংলা ডকুমেন্টেশন
│   ├── GITHUB_SETUP.bn.md .......... সহজ সেটআপ গাইড
│   └── QUICK_REF.bn.md ............. দ্রুত রেফারেন্স
│
├── 🔵 RUN THESE (এগুলো চালান)
│   ├── flash_usdt.py ............... মূল প্রোগ্রাম (Main)
│   ├── cli.py ...................... কমান্ড লাইন টুল
│   └── examples.py ................. উদাহরণ (Examples)
│
├── 📚 DOCUMENTATION (ডকুমেন্টেশন)
│   ├── README.md ................... English docs
│   ├── QUICKSTART.md ............... Quick start
│   ├── EXAMPLES.md ................. More examples
│   ├── SETUP_GUIDE.md .............. Visual setup
│   └── SECURITY.md ................. Security info
│
└── ⚙️ CONFIGURATION (কনফিগারেশন)
    ├── requirements.txt ............ Dependencies
    ├── config.json ................. Networks
    └── .env.example ................ Environment
```

---

## Timeline (সময়রেখা)

```
0 min  │ ডাউনলোড শুরু (Start download)
       │ ↓
1 min  │ ফোল্ডারে যান (Navigate to folder)
       │ ↓
2 min  │ লাইব্রেরি ইনস্টল (Install libraries)
       │ ↓ ↓ ↓
4 min  │ ইনস্টলেশন সম্পন্ন (Installation complete)
       │ ↓
5 min  │ 🎉 প্রোগ্রাম চলছে! (Program running!)
```

---

## Support Levels (সাহায্যের স্তর)

```
Level 1: Quick Reference
└─► QUICK_REF.bn.md (2 min read)

Level 2: Setup Guide
└─► GITHUB_SETUP.bn.md (5 min read)

Level 3: Full Documentation
└─► README.bn.md (15 min read)

Level 4: Advanced Examples
└─► EXAMPLES.md (20 min read)
```

---

## Troubleshooting Flowchart

```
সমস্যা আছে? (Having issues?)
        │
        ├─► Python খুঁজে পাচ্ছে না? (Can't find Python?)
        │   └─► python.org থেকে ইনস্টল করুন
        │       Add to PATH চেক করুন!
        │
        ├─► Module পাওয়া যাচ্ছে না? (Module not found?)
        │   └─► pip install -r requirements.txt
        │       অথবা: pip3 install web3 tronpy
        │
        ├─► Permission denied?
        │   └─► chmod +x flash_usdt.py (Mac/Linux)
        │       Run as administrator (Windows)
        │
        └─► Network connection failed?
            └─► ইন্টারনেট চেক করুন
                কিছুক্ষণ পর চেষ্টা করুন
```

---

## Success Checklist (সফলতার চেকলিস্ট)

```
✅ Python ইনস্টল হয়েছে (Python installed)
✅ Repository ডাউনলোড হয়েছে (Repo downloaded)
✅ ফোল্ডারে আছি (In correct folder)
✅ Dependencies ইনস্টল হয়েছে (Dependencies installed)
✅ প্রোগ্রাম চলছে (Program running)
✅ মেনু দেখতে পাচ্ছি (Can see menu)
✅ ব্যালেন্স চেক করতে পারছি (Can check balance)
```

---

**মনে রাখবেন (Remember):**

```
প্রশ্ন: GitHub-এ কিভাবে চালাবো?
Question: How to run on GitHub?

উত্তর: ৪টি সহজ ধাপ →
Answer: 4 easy steps →

1. ডাউনলোড (Download)
2. ফোল্ডারে যান (Go to folder)
3. ইনস্টল (Install)
4. চালান (Run)

= সফল! (Success!) 🎉
```

---

Made with ❤️ | বাংলাদেশ থেকে ভালোবাসা সহ
