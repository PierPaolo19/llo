# Desktop Usage Guide / ডেস্কটপ ব্যবহার গাইড

## English Version

### How to Use Flash USDT on Your Desktop

This guide will help you use the Flash USDT protocol from your desktop computer.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Desktop Development Setup](#desktop-development-setup)
3. [Using with MetaMask (Desktop Browser)](#using-with-metamask-desktop-browser)
4. [Using with Remix IDE](#using-with-remix-ide)
5. [Using with Desktop Wallets](#using-with-desktop-wallets)
6. [Local Node Setup](#local-node-setup)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software for Desktop

1. **Node.js and npm** (Required for development)
   - Download from: https://nodejs.org/
   - Version: 16 or higher
   - Installation:
     ```bash
     # Windows: Download installer from nodejs.org
     # macOS: brew install node
     # Linux: sudo apt install nodejs npm
     ```

2. **Git** (Required for cloning the repository)
   - Download from: https://git-scm.com/
   - Installation:
     ```bash
     # Windows: Download installer from git-scm.com
     # macOS: brew install git
     # Linux: sudo apt install git
     ```

3. **Web Browser** (Chrome, Firefox, or Brave)
   - For MetaMask extension

4. **Code Editor** (Optional but recommended)
   - Visual Studio Code: https://code.visualstudio.com/
   - Sublime Text
   - Atom

---

## Desktop Development Setup

### Step 1: Clone the Repository

Open your terminal/command prompt:

```bash
# Clone the repository
git clone https://github.com/PierPaolo19/llo.git

# Navigate to the project directory
cd llo
```

### Step 2: Install Dependencies

```bash
# Install all required packages
npm install
```

This will install:
- Hardhat (Ethereum development environment)
- OpenZeppelin contracts
- Testing libraries
- Other dependencies

### Step 3: Compile Contracts

```bash
# Compile the smart contracts
npm run compile
```

### Step 4: Run Tests Locally

```bash
# Run the test suite
npm run test
```

### Step 5: Start Local Blockchain

Open a terminal and run:

```bash
# Start a local Hardhat node
npx hardhat node
```

Keep this terminal open. This runs a local Ethereum blockchain on your desktop.

### Step 6: Deploy Contracts Locally

Open a new terminal:

```bash
# Deploy to local network
npm run deploy
```

---

## Using with MetaMask (Desktop Browser)

### Install MetaMask

1. Open Chrome/Firefox/Brave browser
2. Visit: https://metamask.io/
3. Click "Download" and install the browser extension
4. Create a new wallet or import existing one
5. Save your seed phrase securely

### Connect to Local Network

1. Open MetaMask
2. Click network dropdown (top of MetaMask)
3. Click "Add Network"
4. Enter local network details:
   - Network Name: `Hardhat Local`
   - RPC URL: `http://127.0.0.1:8545`
   - Chain ID: `1337`
   - Currency Symbol: `ETH`
5. Click "Save"

### Import Test Account

When you run `npx hardhat node`, it shows test accounts with private keys:

1. Copy a private key from the Hardhat node output
2. Open MetaMask
3. Click account icon → "Import Account"
4. Paste the private key
5. Click "Import"

Now you have test ETH to use!

### Interact with Contracts

Use the deployed contract addresses with:
- Web3.js
- Ethers.js
- Remix IDE
- Custom web interface

---

## Using with Remix IDE

Remix is a web-based IDE perfect for desktop use.

### Step 1: Open Remix

Visit: https://remix.ethereum.org/

### Step 2: Create New File

1. In File Explorer panel (left side), click "+"
2. Name it: `FlashLoanProvider.sol`
3. Copy the contract code from `contracts/FlashLoanProvider.sol`

### Step 3: Compile

1. Click "Solidity Compiler" icon (left panel)
2. Select compiler version: `0.8.20`
3. Click "Compile FlashLoanProvider.sol"

### Step 4: Deploy

1. Click "Deploy & Run Transactions" icon
2. Select "Environment": 
   - "Injected Provider - MetaMask" (for testnet/mainnet)
   - "Hardhat Provider" (for local)
3. Enter constructor parameters
4. Click "Deploy"

### Step 5: Interact

After deployment:
- Contract appears under "Deployed Contracts"
- Click to expand and see all functions
- Call functions directly from Remix interface

---

## Using with Desktop Wallets

### Option 1: Frame Wallet

Frame is a desktop Ethereum wallet:

1. Download from: https://frame.sh/
2. Install on your desktop
3. Create or import wallet
4. Connect to your preferred network
5. Approve transactions when using dApps

### Option 2: Ledger Live (Hardware Wallet)

For maximum security:

1. Download Ledger Live: https://www.ledger.com/ledger-live
2. Connect your Ledger hardware wallet
3. Install Ethereum app on your Ledger
4. Use with MetaMask or Web3 applications

### Option 3: Exodus Wallet

Desktop wallet with good UI:

1. Download from: https://www.exodus.com/
2. Install on desktop (Windows/Mac/Linux)
3. Set up wallet
4. Add custom tokens if needed

---

## Local Node Setup

### Full Node on Desktop

Running your own Ethereum node:

#### Option 1: Geth (Go Ethereum)

```bash
# Download from: https://geth.ethereum.org/downloads/

# Linux/Mac installation
sudo apt install geth  # Ubuntu/Debian
brew install geth      # macOS

# Start sync (mainnet)
geth --syncmode "snap"

# Start with HTTP RPC
geth --http --http.api eth,net,web3
```

#### Option 2: Hardhat Network (For Development)

Best for local testing:

```bash
# In your project directory
npx hardhat node

# This provides:
# - Local blockchain
# - 10+ test accounts with 10000 ETH each
# - Fast mining
# - Console logging
# - Reset between sessions
```

---

## Desktop Development Workflow

### Daily Development Process

1. **Morning Setup**:
   ```bash
   cd llo
   git pull origin main
   npm install  # if package.json changed
   ```

2. **Start Development**:
   ```bash
   # Terminal 1: Start local node
   npx hardhat node

   # Terminal 2: Run tests
   npm run test

   # Terminal 3: Development work
   code .  # Open in VS Code
   ```

3. **Make Changes**:
   - Edit contracts in `contracts/`
   - Update tests in `test/`
   - Run tests frequently

4. **Test Changes**:
   ```bash
   npm run compile
   npm run test
   ```

5. **Deploy Locally**:
   ```bash
   npm run deploy
   ```

---

## Desktop Tools and Extensions

### VS Code Extensions

Install these for better development:

1. **Solidity** (by Juan Blanco)
   - Syntax highlighting
   - Code completion

2. **Hardhat Solidity** (by Nomic Foundation)
   - Hardhat integration

3. **Prettier - Code Formatter**
   - Auto-format code

4. **GitLens**
   - Git integration

### Terminal Improvements

**Windows:**
- Install Windows Terminal from Microsoft Store
- Or use Git Bash

**Mac:**
- iTerm2: https://iterm2.com/
- Oh My Zsh for better shell

**Linux:**
- Terminator
- Tilix

---

## Troubleshooting

### Common Issues

#### 1. "Command not found: npm"

**Solution**: Install Node.js
```bash
# Check if installed
node --version
npm --version

# If not installed, download from nodejs.org
```

#### 2. "Cannot find module"

**Solution**: Install dependencies
```bash
npm install
```

#### 3. "Port 8545 already in use"

**Solution**: Kill existing process
```bash
# Windows
netstat -ano | findstr :8545
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :8545
kill -9 <PID>
```

#### 4. MetaMask Not Connecting

**Solutions**:
- Refresh the page
- Disconnect and reconnect in MetaMask
- Clear browser cache
- Update MetaMask extension

#### 5. Transaction Failing

**Check**:
- Sufficient balance for gas
- Correct network selected
- Contract address is correct
- Function parameters are valid

#### 6. Compilation Errors

**Solutions**:
```bash
# Clear cache
npx hardhat clean

# Reinstall dependencies
rm -rf node_modules
rm package-lock.json
npm install

# Compile again
npm run compile
```

---

## Best Practices for Desktop Use

### Security

1. **Never commit private keys**
   - Use `.env` file (already in `.gitignore`)
   - Use hardware wallets for real funds

2. **Use test networks first**
   - Goerli, Sepolia for testing
   - Never test on mainnet with real money

3. **Backup your work**
   - Regular git commits
   - Backup `.env` file separately
   - Keep seed phrases offline

### Performance

1. **Use SSD for blockchain data**
   - Faster sync times
   - Better performance

2. **Allocate enough RAM**
   - Minimum 4GB for development
   - 8GB+ recommended

3. **Keep software updated**
   - Update Node.js
   - Update npm packages: `npm update`
   - Update MetaMask

---

## Bengali Version / বাংলা সংস্করণ

## ডেস্কটপে Flash USDT কীভাবে ব্যবহার করবেন

### প্রয়োজনীয় সফটওয়্যার

১. **Node.js এবং npm** (ডেভেলপমেন্টের জন্য আবশ্যক)
   - ডাউনলোড: https://nodejs.org/
   - ইনস্টলেশন: ওয়েবসাইট থেকে ডাউনলোড করে ইনস্টল করুন

২. **Git** (রিপোজিটরি ক্লোন করার জন্য)
   - ডাউনলোড: https://git-scm.com/
   - ইনস্টলেশন: ডাউনলোড করে সেটআপ চালান

৩. **ওয়েব ব্রাউজার** (Chrome, Firefox, বা Brave)
   - MetaMask এক্সটেনশনের জন্য

### ধাপে ধাপে সেটআপ

#### ধাপ ১: প্রজেক্ট ডাউনলোড করুন

টার্মিনাল/কমান্ড প্রম্পট খুলুন:

```bash
# রিপোজিটরি ক্লোন করুন
git clone https://github.com/PierPaolo19/llo.git

# ফোল্ডারে প্রবেশ করুন
cd llo
```

#### ধাপ ২: ডিপেন্ডেন্সি ইনস্টল করুন

```bash
npm install
```

#### ধাপ ৩: কন্ট্রাক্ট কম্পাইল করুন

```bash
npm run compile
```

#### ধাপ ৪: টেস্ট চালান

```bash
npm run test
```

### MetaMask সেটআপ (ডেস্কটপ ব্রাউজার)

১. **MetaMask ইনস্টল করুন**:
   - https://metamask.io/ ভিজিট করুন
   - "Download" ক্লিক করে ব্রাউজার এক্সটেনশন ইনস্টল করুন
   - নতুন ওয়ালেট তৈরি করুন
   - সিড ফ্রেজ নিরাপদে রাখুন

২. **লোকাল নেটওয়ার্ক যোগ করুন**:
   - MetaMask খুলুন
   - নেটওয়ার্ক ড্রপডাউন ক্লিক করুন
   - "Add Network" নির্বাচন করুন
   - বিস্তারিত লিখুন:
     - নেটওয়ার্ক নাম: `Hardhat Local`
     - RPC URL: `http://127.0.0.1:8545`
     - Chain ID: `1337`
   - "Save" ক্লিক করুন

### লোকাল ব্লকচেইন শুরু করুন

একটি টার্মিনাল খুলে চালান:

```bash
npx hardhat node
```

এটি আপনার ডেস্কটপে একটি লোকাল ইথেরিয়াম ব্লকচেইন চালু করবে।

### কন্ট্রাক্ট ডিপ্লয় করুন

নতুন টার্মিনাল খুলে:

```bash
npm run deploy
```

### সমস্যা সমাধান

#### "npm: command not found" ত্রুটি

**সমাধান**: Node.js ইনস্টল করুন
- https://nodejs.org/ থেকে ডাউনলোড করুন
- ইনস্টলার চালান
- কম্পিউটার রিস্টার্ট করুন

#### "Cannot find module" ত্রুটি

**সমাধান**: 
```bash
npm install
```

#### MetaMask সংযুক্ত হচ্ছে না

**সমাধান**:
- পেজ রিফ্রেশ করুন
- MetaMask-এ Disconnect এবং পুনরায় Connect করুন
- ব্রাউজার ক্যাশ পরিষ্কার করুন

---

## Quick Reference Commands

```bash
# Install dependencies
npm install

# Compile contracts
npm run compile

# Run tests
npm run test

# Start local node
npx hardhat node

# Deploy to local
npm run deploy

# Clean build artifacts
npx hardhat clean
```

---

## Additional Resources

- **Hardhat Documentation**: https://hardhat.org/docs
- **MetaMask Guide**: https://metamask.io/faqs/
- **Remix IDE**: https://remix.ethereum.org/
- **OpenZeppelin**: https://docs.openzeppelin.com/
- **Ethereum.org**: https://ethereum.org/en/developers/

---

## Support

For help with desktop usage:
- Check [README.md](README.md) for general documentation
- See [QUICKSTART.md](QUICKSTART.md) for quick setup
- Visit [examples/EXAMPLES.md](examples/EXAMPLES.md) for code examples
- Open an issue on GitHub for specific problems

---

**Last Updated**: February 7, 2026

**Platforms Tested**:
- ✅ Windows 10/11
- ✅ macOS (Intel and Apple Silicon)
- ✅ Linux (Ubuntu 20.04+, Debian, Fedora)
