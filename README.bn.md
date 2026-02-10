# মাল্টি-নেটওয়ার্ক USDT টুল 🚀

GitHub-এ কিভাবে এটি ব্যবহার করবেন তার সম্পূর্ণ গাইড (বাংলায়)

## 🌟 এই টুলটি কি করে?

এই Python টুলটি আপনাকে বিভিন্ন ব্লকচেইন নেটওয়ার্কে USDT (Tether) টোকেনের ব্যালেন্স চেক করতে সাহায্য করে:
- ইথেরিয়াম (ERC20)
- বাইন্যান্স স্মার্ট চেইন (BEP20)
- ট্রন (TRC20)

## 📋 প্রয়োজনীয় জিনিস

1. **Python 3.7 বা তার উপরে** - আপনার কম্পিউটারে Python ইনস্টল থাকতে হবে
2. **ইন্টারনেট সংযোগ**
3. **GitHub অ্যাকাউন্ট** (যদি আপনি GitHub থেকে ডাউনলোড করতে চান)

## 🚀 কিভাবে GitHub থেকে চালাবেন?

### ধাপ ১: রিপোজিটরি ডাউনলোড করুন

#### পদ্ধতি ১: Git ব্যবহার করে (যদি Git ইনস্টল থাকে)

```bash
# রিপোজিটরি ক্লোন করুন
git clone https://github.com/PierPaolo19/llo.git

# ফোল্ডারে প্রবেশ করুন
cd llo
```

#### পদ্ধতি ২: সরাসরি ZIP ফাইল ডাউনলোড

1. এই লিংকে যান: https://github.com/PierPaolo19/llo
2. সবুজ **"Code"** বাটনে ক্লিক করুন
3. **"Download ZIP"** নির্বাচন করুন
4. ZIP ফাইল আনজিপ/এক্সট্র্যাক্ট করুন
5. কমান্ড প্রম্পট/টার্মিনাল খুলুন এবং সেই ফোল্ডারে যান

### ধাপ ২: প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন

```bash
# প্রথমে দেখুন Python ইনস্টল আছে কিনা
python3 --version

# যদি না থাকে, Python ডাউনলোড করুন: https://www.python.org/downloads/

# এখন লাইব্রেরি ইনস্টল করুন
pip install -r requirements.txt
```

অথবা ম্যানুয়ালি ইনস্টল করুন:
```bash
pip install web3 tronpy python-dotenv
```

### ধাপ ৩: টুল চালান

#### পদ্ধতি ১: ইন্টারঅ্যাক্টিভ মেনু (সবচেয়ে সহজ)

```bash
python3 flash_usdt.py
```

এটি একটি মেনু দেখাবে যেখানে আপনি:
1. USDT ব্যালেন্স চেক করতে পারবেন
2. টোকেন তথ্য দেখতে পারবেন
3. নেটওয়ার্ক তথ্য দেখতে পারবেন

#### পদ্ধতি ২: কমান্ড লাইন থেকে

```bash
# Ethereum নেটওয়ার্কে ব্যালেন্স চেক করুন
python3 cli.py ethereum 0xYourWalletAddressHere

# BSC নেটওয়ার্কে ব্যালেন্স চেক করুন
python3 cli.py bsc 0xYourWalletAddressHere

# TRON নেটওয়ার্কে ব্যালেন্স চেক করুন
python3 cli.py tron TYourTronAddressHere
```

## 💼 কোন ওয়ালেট সাপোর্ট করে?

এই টুল যেকোনো ওয়ালেটের পাবলিক অ্যাড্রেস দিয়ে কাজ করে:
- ✅ MetaMask
- ✅ Trust Wallet
- ✅ Binance Wallet
- ✅ যেকোনো Web3 ওয়ালেট

## 📖 উদাহরণ

### উদাহরণ ১: Ethereum-এ ব্যালেন্স চেক

```bash
python3 cli.py ethereum 0x5754284f345afc66a98fbB0a0Afe71e0F007B949
```

আউটপুট:
```
==============================================================
Checking USDT Balance
==============================================================
Network: ethereum
Address: 0x5754284f345afc66a98fbB0a0Afe71e0F007B949
==============================================================

✓ Connected to Ethereum

==============================================================
💰 Balance: 1234567.123456 USDT
==============================================================
```

### উদাহরণ ২: টোকেন তথ্য দেখুন

```bash
python3 cli.py ethereum --info
```

### উদাহরণ ৩: ইন্টারঅ্যাক্টিভ মেনু ব্যবহার করুন

```bash
python3 flash_usdt.py
```

তারপর স্ক্রিনে দেখানো অপশন অনুসরণ করুন।

## 🔧 সমস্যা সমাধান

### সমস্যা ১: "python3: command not found"

**সমাধান:**
- Windows: `python` ব্যবহার করুন `python3` এর বদলে
- Mac/Linux: Python ইনস্টল করুন: https://www.python.org/downloads/

### সমস্যা ২: "No module named 'web3'"

**সমাধান:**
```bash
pip install web3 tronpy python-dotenv
```

অথবা:
```bash
pip3 install web3 tronpy python-dotenv
```

### সমস্যা ৩: "Failed to connect to network"

**সমাধান:**
- আপনার ইন্টারনেট সংযোগ চেক করুন
- কিছুক্ষণ পর আবার চেষ্টা করুন
- RPC সার্ভার ব্যস্ত থাকতে পারে

### সমস্যা ৪: Permission denied

**সমাধান (Linux/Mac):**
```bash
chmod +x flash_usdt.py cli.py examples.py
```

## 🌐 সাপোর্টেড নেটওয়ার্ক

| নেটওয়ার্ক | টাইপ | USDT কন্ট্র্যাক্ট |
|----------|------|-------------------|
| Ethereum | ERC20 | 0xdAC17F958D2ee523a2206206994597C13D831ec7 |
| BSC | BEP20 | 0x55d398326f99059fF775485246999027B3197955 |
| TRON | TRC20 | TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t |

## ⚠️ গুরুত্বপূর্ণ সতর্কতা

- 🔒 **এই টুল শুধু পড়ে** - এটি কোনো লেনদেন করে না
- 🔑 **প্রাইভেট কী লাগবে না** - শুধু পাবলিক অ্যাড্রেস দরকার
- 📚 **শিক্ষামূলক উদ্দেশ্যে** - নিজের ঝুঁকিতে ব্যবহার করুন
- ✅ **সবসময় অ্যাড্রেস যাচাই করুন** ব্লকচেইন এক্সপ্লোরারে

## 📱 আপনার নিজের কোডে ব্যবহার করুন

```python
# flash_usdt.py থেকে টুল ইমপোর্ট করুন
from flash_usdt import USDTFlashTool

# টুল চালু করুন
tool = USDTFlashTool()

# Ethereum-এ সংযোগ করুন
tool.connect_to_network('ethereum')

# আপনার ওয়ালেট অ্যাড্রেস
address = "0xYourAddressHere"

# ব্যালেন্স পান
balance = tool.get_balance('ethereum', address)

# ফলাফল প্রিন্ট করুন
if balance:
    print(f"ব্যালেন্স: {balance} USDT")
```

## 🎓 আরও শিখুন

1. **সম্পূর্ণ ডকুমেন্টেশন:** [README.md](README.md) পড়ুন
2. **দ্রুত শুরু:** [QUICKSTART.md](QUICKSTART.md) দেখুন
3. **আরও উদাহরণ:** [EXAMPLES.md](EXAMPLES.md) দেখুন
4. **নিরাপত্তা:** [SECURITY.md](SECURITY.md) পড়ুন

## 💡 টিপস

1. **Virtual Environment ব্যবহার করুন** (ঐচ্ছিক কিন্তু সুপারিশকৃত):
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **নিয়মিত চেক করার জন্য** `examples.py` দেখুন

3. **ব্যাচ চেক** এর জন্য একাধিক অ্যাড্রেস একসাথে চেক করুন

## 🆘 সাহায্য দরকার?

- GitHub Issue খুলুন: https://github.com/PierPaolo19/llo/issues
- ডকুমেন্টেশন পড়ুন: সকল .md ফাইল দেখুন
- টেস্ট চালান: `python3 test_tool.py`

## 📞 যোগাযোগ

সমস্যা বা প্রশ্নের জন্য GitHub-এ issue খুলুন।

---

**মনে রাখবেন:** 
- 🔐 প্রাইভেট কী কখনো শেয়ার করবেন না
- ✅ সবসময় অ্যাড্রেস যাচাই করুন
- 📖 নিরাপত্তা ডকুমেন্টেশন পড়ুন
- 🎯 শুধু শিক্ষামূলক উদ্দেশ্যে ব্যবহার করুন

**নিরাপদ থাকুন! 🔒**
