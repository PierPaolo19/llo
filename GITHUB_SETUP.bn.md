# GitHub-এ কিভাবে চালাবেন - সহজ গাইড

## পদ্ধতি ১: সরাসরি GitHub থেকে চালান (সবচেয়ে সহজ)

### Windows ব্যবহারকারীদের জন্য:

1. **Python ইনস্টল করুন** (যদি না থাকে):
   - যান: https://www.python.org/downloads/
   - "Download Python" বাটনে ক্লিক করুন
   - ইনস্টলার চালান এবং **"Add Python to PATH"** চেক করুন

2. **এই রিপোজিটরি ডাউনলোড করুন**:
   - এই পেজে যান: https://github.com/PierPaolo19/llo
   - সবুজ **"Code"** বাটন → **"Download ZIP"** ক্লিক করুন
   - ZIP ফাইলটি ডাউনলোড হলে ডান ক্লিক করে **"Extract All"** করুন

3. **Command Prompt খুলুন**:
   - Windows Key চাপুন
   - টাইপ করুন: `cmd`
   - Enter চাপুন

4. **ফোল্ডারে যান**:
   ```cmd
   cd Downloads\llo-main
   ```
   (যেখানে আপনি এক্সট্র্যাক্ট করেছেন সেখানে)

5. **লাইব্রেরি ইনস্টল করুন**:
   ```cmd
   pip install web3 tronpy python-dotenv
   ```

6. **টুল চালান**:
   ```cmd
   python flash_usdt.py
   ```

### Mac/Linux ব্যবহারকারীদের জন্য:

1. **Terminal খুলুন**
   
2. **রিপোজিটরি ডাউনলোড করুন**:
   ```bash
   git clone https://github.com/PierPaolo19/llo.git
   cd llo
   ```

3. **লাইব্রেরি ইনস্টল করুন**:
   ```bash
   pip3 install -r requirements.txt
   ```

4. **টুল চালান**:
   ```bash
   python3 flash_usdt.py
   ```

## পদ্ধতি ২: কমান্ড লাইন থেকে দ্রুত চেক

### যদি আপনার ওয়ালেট অ্যাড্রেস থাকে:

```bash
# Ethereum-এ চেক করুন
python3 cli.py ethereum 0xYourWalletAddress

# Binance Smart Chain-এ চেক করুন
python3 cli.py bsc 0xYourWalletAddress

# TRON-এ চেক করুন
python3 cli.py tron TYourTronAddress
```

## পদ্ধতি ৩: উদাহরণ চালান

```bash
python3 examples.py
```

এটি আপনাকে দেখাবে কিভাবে টুল ব্যবহার করতে হয়।

## সাধারণ সমস্যা এবং সমাধান

### ❌ সমস্যা: "python is not recognized"

**সমাধান:**
- Python ইনস্টল করুন: https://www.python.org/downloads/
- ইনস্টল করার সময় "Add to PATH" চেক করুন

### ❌ সমস্যা: "No module named 'web3'"

**সমাধান:**
```bash
pip install web3 tronpy python-dotenv
```

### ❌ সমস্যা: "Permission denied"

**সমাধান (Mac/Linux):**
```bash
chmod +x flash_usdt.py cli.py
```

### ❌ সমস্যা: "Failed to connect"

**সমাধান:**
- ইন্টারনেট সংযোগ চেক করুন
- কিছুক্ষণ পর আবার চেষ্টা করুন

## দ্রুত টেস্ট

আপনার সবকিছু ঠিকমত কাজ করছে কিনা দেখতে:

```bash
python3 test_tool.py
```

## আপনার প্রথম চেক

1. **টুল চালু করুন**:
   ```bash
   python3 flash_usdt.py
   ```

2. **মেনুতে '1' চাপুন** (Check Balance)

3. **নেটওয়ার্ক লিখুন**: `ethereum` (বা `bsc`, `tron`)

4. **ওয়ালেট অ্যাড্রেস দিন** (আপনার অথবা যেকোনো পাবলিক অ্যাড্রেস)

5. **ফলাফল দেখুন!** 🎉

## ভিডিও টিউটোরিয়াল (যদি তৈরি করা হয়)

_শীঘ্রই আসছে..._

## সাহায্য দরকার?

- 📖 সম্পূর্ণ গাইড: [README.bn.md](README.bn.md) পড়ুন
- 💬 GitHub Issue খুলুন যদি আটকে যান
- 🔍 [EXAMPLES.md](EXAMPLES.md) দেখুন আরও উদাহরণের জন্য

---

## একনজরে কমান্ড

```bash
# ডাউনলোড করুন
git clone https://github.com/PierPaolo19/llo.git
cd llo

# ইনস্টল করুন
pip install -r requirements.txt

# চালান
python3 flash_usdt.py

# অথবা দ্রুত চেক
python3 cli.py ethereum 0xYourAddress
```

**এতটুকুই! আপনি প্রস্তুত! 🚀**
