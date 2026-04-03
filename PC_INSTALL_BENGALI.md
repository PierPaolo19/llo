# পিসিতে কিভাবে ইনস্টল করবেন - Flash USDT
# How to Install on PC - Flash USDT

## ati pc te ki vabe install korbo - সম্পূর্ণ গাইড

এই গাইড আপনাকে ধাপে ধাপে দেখাবে কিভাবে Flash USDT আপনার কম্পিউটারে (PC) ইনস্টল করতে হয়।

---

## 📋 শুরু করার আগে (Before You Start)

### আপনার কি কি লাগবে:

1. **কম্পিউটার (PC):**
   - Windows 10/11, macOS, বা Linux
   - ইন্টারনেট সংযোগ
   - কমপক্ষে 4 GB RAM
   - 1 GB খালি স্পেস

2. **MetaMask ওয়ালেট:**
   - Chrome, Firefox, বা Edge ব্রাউজার
   - MetaMask এক্সটেনশন (পরে ইনস্টল করব)

---

## 🚀 ইনস্টলেশন - ৩টি সহজ উপায়

আপনার PC তে Flash USDT ইনস্টল করার ৩টি উপায় আছে:

### উপায় ১: সহজ ইনস্টলার (Windows - সবচেয়ে সহজ) ⭐ সুপারিশকৃত

**Windows ব্যবহারকারীদের জন্য:**

1. **ডাউনলোড করুন:**
   - GitHub Releases পেজে যান: https://github.com/PierPaolo19/llo/releases
   - `Flash-USDT-Setup-1.0.0.exe` ডাউনলোড করুন

2. **ইনস্টল করুন:**
   - ডাউনলোড করা ফাইলে ডাবল ক্লিক করুন
   - যদি "Windows protected your PC" মেসেজ আসে:
     - "More info" ক্লিক করুন
     - "Run anyway" ক্লিক করুন
   - ইনস্টলার চালু হবে
   - ইনস্টল করার জায়গা নির্বাচন করুন (ডিফল্ট ঠিক আছে)
   - "Install" বাটন ক্লিক করুন

3. **চালু করুন:**
   - Desktop এ Flash USDT আইকন দেখতে পাবেন
   - আইকনে ডাবল ক্লিক করুন
   - অথবা Start Menu থেকে খুলুন

**সম্পন্ন! আপনার PC তে Flash USDT ইনস্টল হয়ে গেছে!** ✅

---

### উপায় ২: Portable সংস্করণ (Installation ছাড়া)

**যেকোনো Windows PC তে - Installation এর দরকার নেই:**

1. **ডাউনলোড করুন:**
   - `FlashUSDT-1.0.0-portable.exe` ডাউনলোড করুন

2. **যেকোনো ফোল্ডারে রাখুন:**
   - Desktop এ বা যেকোনো ফোল্ডারে
   - USB drive এও রাখতে পারবেন

3. **চালু করুন:**
   - .exe ফাইলে ডাবল ক্লিক করুন
   - সরাসরি চালু হবে

**সুবিধা:** 
- Installation করার দরকার নেই
- USB drive থেকে চালাতে পারবেন
- কোন Admin access লাগবে না

---

### উপায় ৩: Source Code থেকে (Developers এর জন্য)

**সব OS এর জন্য (Windows, macOS, Linux):**

#### ধাপ ১: Node.js ইনস্টল করুন

**Windows:**
1. https://nodejs.org যান
2. "LTS" সংস্করণ ডাউনলোড করুন (v18 বা তার বেশি)
3. ডাউনলোড করা ফাইল চালু করুন
4. "Next" ক্লিক করে ইনস্টল করুন

**macOS:**
1. https://nodejs.org যান
2. macOS installer ডাউনলোড করুন
3. .pkg ফাইল চালু করুন
4. ইনস্টল করুন

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install nodejs npm
```

#### ধাপ ২: চেক করুন Node.js ইনস্টল হয়েছে কিনা

**Windows:** Command Prompt খুলুন (Win + R, তারপর "cmd" টাইপ করুন)
**macOS/Linux:** Terminal খুলুন

তারপর এই কমান্ড চালান:
```bash
node --version
```

যদি `v18.0.0` বা তার বেশি দেখায়, তাহলে ঠিক আছে! ✅

#### ধাপ ৩: Git ইনস্টল করুন (Optional)

**Windows:**
1. https://git-scm.com/download/win থেকে ডাউনলোড করুন
2. ইনস্টল করুন (সব default অপশন ঠিক আছে)

**macOS/Linux:**
Terminal এ:
```bash
# macOS (Homebrew থাকলে)
brew install git

# Linux
sudo apt install git
```

#### ধাপ ৪: Flash USDT ডাউনলোড করুন

**Command Prompt বা Terminal এ:**

```bash
# Repository ডাউনলোড করুন
git clone https://github.com/PierPaolo19/llo.git

# ফোল্ডারে ঢুকুন
cd llo
```

**Git না থাকলে:**
1. https://github.com/PierPaolo19/llo যান
2. সবুজ "Code" বাটন ক্লিক করুন
3. "Download ZIP" ক্লিক করুন
4. ZIP ফাইল extract করুন
5. Command Prompt/Terminal এ সেই ফোল্ডারে যান

#### ধাপ ৫: Dependencies ইনস্টল করুন

```bash
npm install
```

এটা কয়েক মিনিট সময় নিতে পারে। অপেক্ষা করুন... ⏳

#### ধাপ ৬: Desktop অ্যাপ চালু করুন

```bash
npm run desktop
```

**একটা নতুন উইন্ডো খুলবে Flash USDT এর সাথে!** 🎉

---

## 🔧 Windows এ ইনস্টলেশন (বিস্তারিত)

### Windows 10/11 ব্যবহারকারীদের জন্য বিশেষ নির্দেশনা:

#### সমস্যা: "Windows protected your PC"

যখন installer চালাবেন, এই মেসেজ আসতে পারে:

```
Windows protected your PC
Microsoft Defender SmartScreen prevented an unrecognized app from starting.
```

**সমাধান:**
1. "More info" লিংকে ক্লিক করুন
2. "Run anyway" বাটন ক্লিক করুন
3. এটা নিরাপদ - আমাদের অ্যাপ just unsigned

#### Windows Defender Configuration

**Optional - যদি Defender ব্লক করে:**

1. Windows Security খুলুন
2. "Virus & threat protection" এ যান
3. "Manage settings" ক্লিক করুন
4. "Exclusions" এ যান
5. Flash USDT ফোল্ডার add করুন

#### Setup Script ব্যবহার করুন

Windows এর জন্য আমরা সহজ setup script দিয়েছি:

**PowerShell এ (Run as Administrator):**
```powershell
.\scripts\setup-windows.ps1
```

**অথবা Command Prompt এ:**
```cmd
.\scripts\setup-windows.bat
```

এই script আপনার জন্য সব চেক করে দেবে! ✅

---

## 🍎 macOS এ ইনস্টলেশন

### macOS ব্যবহারকারীদের জন্য:

#### উপায় ১: Installer (Coming Soon)

DMG ফাইল থেকে drag-and-drop ইনস্টলেশন আসছে।

#### উপায় ২: Source Code থেকে

উপরের "উপায় ৩" দেখুন - এটাই সবচেয়ে ভালো উপায়।

**Terminal এ:**
```bash
# Clone করুন
git clone https://github.com/PierPaolo19/llo.git
cd llo

# Install করুন
npm install

# চালু করুন
npm run desktop
```

---

## 🐧 Linux এ ইনস্টলেশন

### Ubuntu/Debian ব্যবহারকারীদের জন্য:

#### উপায় ১: AppImage (সবচেয়ে সহজ)

```bash
# AppImage ডাউনলোড করুন (releases থেকে)
wget https://github.com/PierPaolo19/llo/releases/download/v1.0.0/Flash-USDT.AppImage

# Executable করুন
chmod +x Flash-USDT.AppImage

# চালু করুন
./Flash-USDT.AppImage
```

#### উপায় ২: DEB Package

```bash
# DEB ডাউনলোড করুন
wget https://github.com/PierPaolo19/llo/releases/download/v1.0.0/flash-usdt_1.0.0_amd64.deb

# Install করুন
sudo dpkg -i flash-usdt_1.0.0_amd64.deb

# Dependencies ঠিক করুন (যদি error আসে)
sudo apt-get install -f
```

---

## ✅ ইনস্টলেশন চেক করুন

### ইনস্টল হয়েছে কিনা চেক করার উপায়:

1. **Desktop থেকে খুলুন:**
   - Flash USDT আইকন খুঁজুন
   - ডাবল ক্লিক করুন

2. **অথবা Command Line থেকে:**
   ```bash
   cd llo
   npm run desktop
   ```

3. **যদি সফলভাবে খুলে:**
   - একটা নতুন উইন্ডো আসবে
   - "Flash USDT" শিরোনাম দেখবেন
   - "Connect Wallet" বাটন দেখবেন

**যদি এগুলো দেখতে পান = সফলভাবে ইনস্টল হয়েছে!** ✅

---

## 🔐 MetaMask ইনস্টল করুন

Flash USDT ব্যবহার করার জন্য MetaMask ওয়ালেট লাগবে।

### ধাপ ১: Browser Extension ইনস্টল করুন

**Chrome/Edge:**
1. https://metamask.io যান
2. "Download" বাটন ক্লিক করুন
3. "Install MetaMask for Chrome" ক্লিক করুন
4. Chrome Web Store খুলবে
5. "Add to Chrome" ক্লিক করুন

**Firefox:**
1. https://metamask.io যান
2. "Download for Firefox" বেছে নিন
3. Firefox Add-ons পেজ খুলবে
4. "Add to Firefox" ক্লিক করুন

### ধাপ ২: MetaMask Setup করুন

1. Extension icon ক্লিক করুন (browser এর উপরে)
2. "Get Started" ক্লিক করুন
3. "Create a Wallet" বেছে নিন
4. একটা শক্তিশালী password দিন
5. **Secret Recovery Phrase সেভ করুন** (খুবই গুরুত্বপূর্ণ!)
   - এটা কোথাও লিখে রাখুন (কাগজে)
   - কখনো কাউকে দেখাবেন না
   - হারিয়ে গেলে ওয়ালেট recover করা যাবে না

### ধাপ ৩: MetaMask Flash USDT এর সাথে Connect করুন

1. Flash USDT অ্যাপ খুলুন
2. "Connect Wallet" বাটন ক্লিক করুন
3. MetaMask popup আসবে
4. "Connect" ক্লিক করুন
5. আপনার wallet address দেখতে পাবেন

**সফল! এখন ব্যবহার করতে পারবেন!** 🎉

---

## 🛠️ সমস্যা সমাধান (Troubleshooting)

### সমস্যা ১: "npm: command not found"

**সমাধান:**
- Node.js ঠিকমত ইনস্টল হয়নি
- আবার Node.js ইনস্টল করুন (উপরের ধাপ দেখুন)
- Computer restart করুন

### সমস্যা ২: "Permission denied" (Linux/macOS)

**সমাধান:**
```bash
# sudo দিয়ে চেষ্টা করুন
sudo npm install
```

### সমস্যা ৩: অ্যাপ খুলছে না

**Windows:**
- Antivirus disable করুন সাময়িকভাবে
- Administrator হিসেবে চালান (right-click > Run as administrator)

**macOS:**
- System Preferences > Security & Privacy
- "Open Anyway" ক্লিক করুন

**Linux:**
- AppImage executable করেছেন কিনা চেক করুন:
  ```bash
  chmod +x Flash-USDT.AppImage
  ```

### সমস্যা ৪: "EACCES" error npm install এ

**সমাধান:**
```bash
# npm এর permission ঠিক করুন
sudo chown -R $USER:$USER ~/.npm
sudo chown -R $USER:$USER node_modules
```

### সমস্যা ৫: MetaMask connect হচ্ছে না

**চেক করুন:**
1. MetaMask extension ইনস্টল আছে কিনা
2. MetaMask unlock করেছেন কিনা
3. Browser এ MetaMask permission দিয়েছেন কিনা

**সমাধান:**
- Flash USDT রিফ্রেশ করুন (Ctrl + R)
- MetaMask lock করে আবার unlock করুন
- Browser restart করুন

### সমস্যা ৬: White screen / ফাঁকা পেজ

**সমাধান:**
```bash
# Cache clear করুন
rm -rf node_modules
npm cache clean --force
npm install
npm run desktop
```

---

## 📚 আরও তথ্যের জন্য

### বাংলায় আরো গাইড:
- [Desktop ব্যবহার গাইড](docs/DESKTOP_BENGALI.md) - সম্পূর্ণ ব্যবহার নির্দেশিকা
- [Quick Start](DESKTOP_QUICKSTART.md) - দ্রুত শুরু করার গাইড

### ইংরেজিতে বিস্তারিত:
- [Windows Guide](docs/WINDOWS.md) - Windows 10 Pro এর জন্য
- [Desktop Guide](docs/DESKTOP.md) - সম্পূর্ণ desktop গাইড
- [Network Guide](docs/NETWORKS.md) - Network সেটআপ

### সাহায্যের জন্য:
- GitHub Issues: https://github.com/PierPaolo19/llo/issues
- README: https://github.com/PierPaolo19/llo

---

## 🎯 দ্রুত সারাংশ (Quick Summary)

### Windows ব্যবহারকারীদের জন্য:
```
1. Flash-USDT-Setup.exe ডাউনলোড করুন
2. Run করুন (SmartScreen এ "Run anyway" ক্লিক করুন)
3. Install করুন
4. Desktop থেকে খুলুন
5. MetaMask connect করুন
✅ Done!
```

### Source Code থেকে (সব OS):
```bash
# ডাউনলোড
git clone https://github.com/PierPaolo19/llo.git
cd llo

# ইনস্টল
npm install

# চালু
npm run desktop

✅ Done!
```

---

## 🎊 অভিনন্দন!

আপনি সফলভাবে Flash USDT আপনার PC তে ইনস্টল করেছেন!

### এখন কি করবেন?

1. **MetaMask সেটআপ করুন** (যদি না করে থাকেন)
2. **Testnet এ চেষ্টা করুন** প্রথমে (Sepolia)
3. **Flash Loan চালান** ছোট amount দিয়ে
4. **Documentation পড়ুন** আরো জানার জন্য

### মনে রাখবেন:
- ⚠️ প্রথমে Testnet এ practice করুন
- ⚠️ ছোট amount দিয়ে শুরু করুন
- ⚠️ Secret phrase কখনো কাউকে দেবেন না
- ⚠️ সব ঝুঁকি নিজের দায়িত্বে

**শুভকামনা! Happy Flash Loaning!** 🚀

---

**সংস্করণ:** 1.0.0  
**সর্বশেষ আপডেট:** February 2026  
**ভাষা:** বাংলা (Bengali)

আরো প্রশ্ন থাকলে GitHub issues এ জিজ্ঞেস করুন!
