# Quick Start: Desktop ব্যবহার করুন (How to Use Desktop)

## ati ki vabe desktop use korbo - সম্পূর্ণ উত্তর

এই গাইড আপনাকে দেখাবে Flash USDT Desktop Application কিভাবে ব্যবহার করতে হয়।

## ⚡ দ্রুত শুরু (Quick Start)

### ১. ইনস্টল করুন (Install)

```bash
# Repository ক্লোন করুন
git clone https://github.com/PierPaolo19/llo.git
cd llo

# Dependencies ইনস্টল করুন
npm install
```

### ২. Desktop অ্যাপ চালু করুন (Launch Desktop App)

```bash
npm run desktop
```

**এইটা একটা নতুন উইন্ডো খুলবে Flash USDT Desktop Application সহ!** 🎉

### ৩. কি করতে পারবেন (What You Can Do)

Desktop অ্যাপ দিয়ে আপনি করতে পারবেন:

- ✅ **ওয়ালেট সংযোগ** - MetaMask বা অন্য Web3 ওয়ালেট
- ✅ **Flash Loan চালান** - সহজ ফর্ম দিয়ে
- ✅ **Liquidity জমা দিন** - USDT ডিপোজিট করুন
- ✅ **Liquidity উত্তোলন** - USDT withdraw করুন
- ✅ **Transaction দেখুন** - সব লেনদেনের ইতিহাস
- ✅ **Real-time তথ্য** - লাইভ কন্ট্রাক্ট ডেটা

## 📱 Desktop Interface দেখতে কেমন (What It Looks Like)

```
╔════════════════════════════════════════════════╗
║  ⚡ Flash USDT         [Connect Wallet] 🔗   ║
║  Desktop Application                           ║
╠════════════════════════════════════════════════╣
║                                                ║
║  📡 Network Status                             ║
║  Network: Ethereum Mainnet                     ║
║  Available Liquidity: 10,000 USDT              ║
║  Flash Loan Fee: 0.09%                         ║
║                                                ║
║  ⚡ Execute Flash Loan                         ║
║  Receiver Address: [________________]          ║
║  Loan Amount: [________] USDT                  ║
║  Estimated Fee: 9 USDT                         ║
║  [Execute Flash Loan]                          ║
║                                                ║
║  💧 Liquidity Management                       ║
║  Deposit: [________] [Deposit]                 ║
║  Withdraw: [________] [Withdraw]               ║
║                                                ║
║  📜 Recent Transactions                        ║
║  • Flash Loan - 1000 USDT                      ║
║  • Deposit - 5000 USDT                         ║
║                                                ║
╚════════════════════════════════════════════════╝
```

## 📖 বিস্তারিত নির্দেশনা (Detailed Instructions)

### A. প্রথম বার ব্যবহার (First Time Use)

1. **MetaMask ইনস্টল করুন** (যদি না থাকে)
   - Chrome/Firefox এ MetaMask extension ইনস্টল করুন
   - একটি ওয়ালেট তৈরি করুন বা import করুন

2. **Desktop অ্যাপ চালু করুন**
   ```bash
   npm run desktop
   ```

3. **"Connect Wallet" ক্লিক করুন**
   - MetaMask পপআপ আসবে
   - "Connect" বাটন ক্লিক করুন
   - আপনার ওয়ালেট সংযুক্ত হবে

### B. Flash Loan ব্যবহার (Using Flash Loan)

1. **Receiver Contract Deploy করুন**
   - আপনার নিজের smart contract deploy করুন
   - IFlashLoanReceiver interface implement করতে হবে
   - Contract address কপি করুন

2. **Desktop App এ যান**
   - "Execute Flash Loan" সেকশনে যান
   - Receiver Address পেস্ট করুন
   - Loan amount লিখুন (যেমন: 1000)
   - "Execute Flash Loan" ক্লিক করুন

3. **MetaMask এ Approve করুন**
   - Transaction details দেখুন
   - "Confirm" ক্লিক করুন
   - অপেক্ষা করুন confirmation এর জন্য

### C. Liquidity Provide করুন (Provide Liquidity)

1. **USDT আছে কিনা নিশ্চিত করুন**
   - আপনার ওয়ালেটে USDT থাকতে হবে

2. **Deposit করুন**
   - "Liquidity Management" সেকশনে যান
   - Amount লিখুন
   - "Deposit" ক্লিক করুন
   - প্রথমবার approve করতে হবে
   - Deposit transaction confirm করুন

3. **ফি অর্জন করুন**
   - আপনার USDT পুলে থাকবে
   - যখন কেউ flash loan নেবে, আপনি ফি পাবেন!

## 🛠️ System Requirements

- **Operating System**: Windows 7+, macOS 10.10+, Linux (Ubuntu/Debian)
- **RAM**: 4GB minimum
- **Node.js**: Version 18 বা তার বেশি
- **Browser**: MetaMask compatible browser
- **Internet**: Active connection required

## 📦 Build করুন (Build Your Own)

নিজের জন্য executable তৈরি করতে:

```bash
# Windows, macOS, Linux সবার জন্য
npm run desktop:build-all

# শুধু আপনার OS এর জন্য
npm run desktop:build
```

Built files পাবেন `dist/` folder এ।

## 🔧 Troubleshooting (সমস্যা সমাধান)

### Desktop app না খুললে
```bash
# Dependencies আবার install করুন
rm -rf node_modules
npm install

# আবার চেষ্টা করুন
npm run desktop
```

### MetaMask connect না হলে
- MetaMask unlock করা আছে কিনা চেক করুন
- সঠিক network এ আছেন কিনা দেখুন
- Browser এ MetaMask extension active আছে কিনা

### Transaction fail হলে
- পর্যাপ্ত ETH আছে কিনা (gas fee এর জন্য)
- Network congestion চেক করুন
- Gas price বাড়িয়ে দেখুন

## 🌐 Multi-Language Support

- **English**: See `docs/DESKTOP.md`
- **বাংলা**: See `docs/DESKTOP_BENGALI.md`
- **This file**: Quick start in both languages

## 📞 সাহায্য পেতে (Get Help)

- **GitHub Issues**: https://github.com/PierPaolo19/llo/issues
- **Documentation**: `/docs` folder এ সব documentation
- **Community**: GitHub Discussions এ প্রশ্ন করুন

## 🎯 পরবর্তী পদক্ষেপ (Next Steps)

1. ✅ Desktop app চালু করেছেন
2. ✅ Wallet connect করেছেন
3. 📚 পড়ুন: `docs/DESKTOP_BENGALI.md` - সম্পূর্ণ বাংলা গাইড
4. 💡 শিখুন: Smart contract কিভাবে লিখতে হয়
5. 🚀 Deploy করুন: আপনার নিজের flash loan strategy

## ⚠️ গুরুত্বপূর্ণ সতর্কতা

- শুধুমাত্র শিক্ষামূলক উদ্দেশ্যে ব্যবহার করুন
- আসল টাকা ব্যবহারের আগে testnet এ পরীক্ষা করুন
- Smart contract audit করা হয়নি
- আপনার নিজের ঝুঁকিতে ব্যবহার করুন
- Private key/seed phrase কখনো কারো সাথে শেয়ার করবেন না

---

## সংক্ষিপ্ত উত্তর (TL;DR)

**Desktop ব্যবহার করার জন্য:**

```bash
# 1. Install
git clone https://github.com/PierPaolo19/llo.git
cd llo
npm install

# 2. Run
npm run desktop

# 3. Use!
# - Connect MetaMask
# - Execute flash loans
# - Manage liquidity
# - Track transactions
```

**এই তিনটা command ই যথেষ্ট desktop app ব্যবহার করার জন্য!** ✅

---

**Made with ❤️ for the DeFi community**

বিস্তারিত জানতে `docs/DESKTOP_BENGALI.md` পড়ুন! 📖
