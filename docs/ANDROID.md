# Flash USDT on Android 📱

This guide explains how to use Flash USDT on Android devices, including compatibility with **Magisk v30.7** for rooted devices.

---

## Table of Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Option A — Standard Android (Non-Rooted)](#option-a--standard-android-non-rooted)
4. [Option B — Rooted Android with Magisk v30.7](#option-b--rooted-android-with-magisk-v307)
5. [Supported Wallets](#supported-wallets)
6. [Connecting to Flash USDT Contracts](#connecting-to-flash-usdt-contracts)
7. [Network Configuration on Android](#network-configuration-on-android)
8. [Troubleshooting](#troubleshooting)
9. [Security Considerations](#security-considerations)

---

## Overview

Flash USDT smart contracts are deployed on EVM-compatible blockchains (Ethereum, BSC, Polygon) and the Tron network. While the desktop application requires Windows/macOS/Linux, you can **interact with the contracts directly from Android** using:

- **MetaMask Mobile** — for ERC20 / BEP20 networks
- **Trust Wallet** — multi-chain support
- **TokenPocket** — TRC20 (Tron) + EVM chains
- **imToken** — EVM chains

Magisk v30.7 users on rooted Android devices have additional capabilities such as bypassing SSL pinning for DApp inspection and running full node light clients.

---

## Requirements

### Non-Rooted Android
- Android 8.0 (Oreo) or higher
- One of the [supported wallets](#supported-wallets) installed
- Active internet connection
- ETH / BNB / TRX for gas fees

### Rooted Android with Magisk v30.7
- Android 8.0 or higher
- **Magisk v30.7** installed ([Download](https://github.com/topjohnwu/Magisk/releases/tag/v30.7))
- Magisk modules (optional, see below)
- One of the [supported wallets](#supported-wallets) installed

---

## Option A — Standard Android (Non-Rooted)

### Step 1 — Install MetaMask Mobile

1. Open the **Google Play Store** or **App Store**
2. Search for **MetaMask**
3. Install and open the app
4. Create a new wallet or import an existing one
5. **Back up your Secret Recovery Phrase securely**

### Step 2 — Add Custom Networks

Open MetaMask → Settings → Networks → Add Network:

**Binance Smart Chain (BEP20):**
```
Network Name: BSC Mainnet
RPC URL: https://bsc-dataseed.binance.org/
Chain ID: 56
Symbol: BNB
Explorer: https://bscscan.com
```

**Polygon (ERC20-compatible):**
```
Network Name: Polygon Mainnet
RPC URL: https://polygon-rpc.com/
Chain ID: 137
Symbol: MATIC
Explorer: https://polygonscan.com
```

**Ethereum Mainnet** is added by default in MetaMask.

### Step 3 — Import USDT Token

After selecting your network, add USDT as a custom token:

| Network   | USDT Contract Address                        |
|-----------|----------------------------------------------|
| Ethereum  | `0xdAC17F958D2ee523a2206206994597C13D831ec7` |
| BSC       | `0x55d398326f99059fF775485246999027B3197955` |
| Polygon   | `0xc2132D05D31c914a87C6611C10748AEb04B58e8F` |

### Step 4 — Connect to Flash USDT DApp

Once your Flash USDT contract is deployed:

1. Open MetaMask Mobile browser (the globe icon)
2. Navigate to your deployed frontend or use WalletConnect
3. Connect your wallet to the Flash USDT interface
4. Execute flash loans directly from your Android device

---

## Option B — Rooted Android with Magisk v30.7

Magisk v30.7 provides systemless root and a powerful module system that can enhance your DeFi experience on Android.

### Installing Magisk v30.7

1. Download `Magisk-v30.7.apk` from the [official Magisk GitHub releases](https://github.com/topjohnwu/Magisk/releases/tag/v30.7)
2. Install it as an APK (enable "Unknown sources" if needed)
3. Open Magisk and follow the setup instructions for your device
4. Reboot your device after installation

> ⚠️ **Warning**: Rooting your device voids the warranty and may cause security risks. Only root if you understand the implications.

### Verifying Magisk Installation

Open the Magisk app and confirm:
- **Magisk version**: 30.7 (30700)
- **Ramdisk**: Yes
- **App version**: 30.7

### Useful Magisk Modules for DeFi

After installing Magisk v30.7, these modules can help with DeFi usage:

| Module | Purpose | Notes |
|--------|---------|-------|
| **LSPosed** | Framework for Xposed modules | Enables advanced app modifications |
| **Universal SafetyNet Fix** | Pass Play Integrity checks | Helps wallet apps work on rooted devices |
| **MagiskHide (via Shamiko)** | Hide root from apps | Prevents wallets from detecting root |

#### Installing Shamiko (Hide Root from Wallet Apps)

Some wallet apps (MetaMask, Trust Wallet) may refuse to run on rooted devices. Use Shamiko to hide root:

1. In Magisk → Modules → Install from storage
2. Download and install [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases)
3. Enable "Zygisk" in Magisk Settings first
4. Reboot device
5. In Magisk → Configure DenyList → enable for MetaMask

### Running Web3 DApps with Magisk

With Magisk v30.7 and root access, you can:

1. **Inspect DApp traffic** — Use packet capture tools (e.g., HttpCanary) to debug flash loan transactions
2. **Run a light Ethereum client** — Install Geth or similar on rooted Android for direct node access
3. **Full filesystem access** — Store private keys in encrypted secure storage
4. **Custom DNS** — Use your own RPC node for better privacy

### ADB Debugging for Flash USDT

On rooted devices, you can use ADB to interact with the blockchain:

```bash
# Connect via ADB
adb shell

# Check if Magisk is running
su -c "magisk --version"

# Test network connectivity to BSC
curl https://bsc-dataseed.binance.org/ -s | python3 -m json.tool
```

---

## Supported Wallets

### ERC20 / BEP20 Networks

| Wallet | ERC20 | BEP20 | TRC20 | WalletConnect | Root-friendly |
|--------|-------|-------|-------|---------------|---------------|
| **MetaMask Mobile** | ✅ | ✅ | ❌ | ✅ | ✅ (with Shamiko) |
| **Trust Wallet** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **TokenPocket** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **imToken** | ✅ | ✅ | ❌ | ✅ | ⚠️ |
| **Coinbase Wallet** | ✅ | ✅ | ❌ | ✅ | ⚠️ |

> ⚠️ = May detect root; use Shamiko/DenyList to bypass.

### TRC20 (Tron Network)

For Tron/TRC20 USDT, use:
- **TronLink Mobile** — Official Tron wallet
- **TokenPocket** — Supports Tron + TRC20 USDT

---

## Connecting to Flash USDT Contracts

### Via WalletConnect (Recommended for Android)

If you have a web frontend for your Flash USDT deployment:

1. Open the web interface on your desktop browser
2. Click "Connect Wallet" → Select "WalletConnect"
3. A QR code will appear
4. Open MetaMask Mobile → Scan QR code
5. Approve the connection
6. Now your Android wallet controls the desktop interface

### Direct Mobile DApp Usage

For wallets with built-in browsers (MetaMask Mobile, Trust Wallet):

1. Open the in-app browser
2. Navigate to the Flash USDT frontend URL
3. Tap "Connect Wallet" — it will auto-detect MetaMask
4. Interact with flash loan functions directly from Android

### Using Ethers.js from Android (Rooted/Developer Use)

On a rooted device with Termux installed:

```bash
# Install Node.js in Termux
pkg install nodejs

# Install ethers
npm install ethers

# Run a simple flash loan script
node -e "
const { ethers } = require('ethers');
const provider = new ethers.JsonRpcProvider('https://bsc-dataseed.binance.org/');
provider.getBlockNumber().then(console.log);
"
```

---

## Network Configuration on Android

### Adding BSC to MetaMask Mobile

1. Tap the network selector (top of MetaMask)
2. Tap "Add Network"
3. Tap "Add a network manually"
4. Enter BSC details:

```
Network Name:    BNB Smart Chain
New RPC URL:     https://bsc-dataseed.binance.org/
Chain ID:        56
Currency Symbol: BNB
Block Explorer:  https://bscscan.com
```

5. Tap "Save"

### Adding Polygon to MetaMask Mobile

```
Network Name:    Polygon Mainnet
New RPC URL:     https://polygon-rpc.com/
Chain ID:        137
Currency Symbol: MATIC
Block Explorer:  https://polygonscan.com
```

### Testnet Networks (for Testing)

```
# BSC Testnet
Network Name:    BSC Testnet
RPC URL:         https://data-seed-prebsc-1-s1.binance.org:8545/
Chain ID:        97
Symbol:          tBNB
Explorer:        https://testnet.bscscan.com

# Sepolia (Ethereum Testnet)
Network Name:    Sepolia
RPC URL:         https://rpc.sepolia.org
Chain ID:        11155111
Symbol:          SepoliaETH
Explorer:        https://sepolia.etherscan.io
```

---

## Troubleshooting

### MetaMask won't open on rooted device

**Problem**: MetaMask detects root and refuses to launch.

**Solution**:
1. Install **Shamiko** Magisk module
2. Enable **Zygisk** in Magisk settings
3. Go to Magisk → DenyList → Enable for MetaMask
4. Reboot and try again

### "Network connection failed" error

**Problem**: Cannot connect to blockchain RPC.

**Solution**:
1. Check internet connection
2. Try a different RPC URL (see [NETWORKS.md](NETWORKS.md))
3. BSC alternatives:
   - `https://bsc-dataseed1.defibit.io/`
   - `https://bsc-dataseed1.ninicoin.io/`
   - `https://bsc.publicnode.com`

### Transaction fails on Android

**Problem**: Flash loan transaction reverts.

**Solution**:
1. Increase gas limit manually in MetaMask
2. Ensure enough BNB/ETH for gas
3. Check that the Flash USDT contract has sufficient liquidity
4. Test on testnet first

### Magisk modules causing wallet crashes

**Problem**: A Magisk module conflicts with the wallet app.

**Solution**:
1. Boot into Magisk safe mode (hold volume down during boot)
2. Disable modules one by one to find the conflict
3. Remove conflicting module

### Trust Wallet not detecting custom network

**Problem**: Added BSC manually but transactions fail.

**Solution**:
1. Trust Wallet has BSC built-in — use the BNB Smart Chain option
2. No need to add BSC manually in Trust Wallet
3. For custom RPC, go to Settings → Preferences → Node Settings

---

## Security Considerations

> ⚠️ **Important Security Notes**

1. **Magisk hides root from apps** — but your device is still rooted. Be cautious about which apps you grant root access to.

2. **Never store private keys in plaintext** — Use the wallet app's secure storage only.

3. **Use hardware wallets when possible** — Ledger supports WalletConnect and works with MetaMask Mobile.

4. **Test on testnet first** — Always validate flash loan logic on BSC Testnet or Sepolia before mainnet.

5. **Verify contract addresses** — Double-check USDT and Flash USDT contract addresses before transactions.

6. **Use official Magisk releases only** — Download Magisk only from [github.com/topjohnwu/Magisk](https://github.com/topjohnwu/Magisk/releases/tag/v30.7). Avoid unofficial APKs.

7. **Root detection bypass is for wallet compatibility only** — Do not use these tools to deceive DApps about your device security.

---

## Additional Resources

- [Magisk v30.7 Release Notes](https://github.com/topjohnwu/Magisk/releases/tag/v30.7)
- [MetaMask Mobile Documentation](https://support.metamask.io/hc/en-us/categories/360001514312-Using-MetaMask)
- [Trust Wallet Help Center](https://community.trustwallet.com/)
- [WalletConnect Documentation](https://docs.walletconnect.com/)
- [Flash USDT Network Guide](NETWORKS.md)
- [Flash USDT Desktop Guide](DESKTOP.md)
- [Flash USDT Technical Docs](TECHNICAL.md)
- [Getting Started](GETTING_STARTED.md)
