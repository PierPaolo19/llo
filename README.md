# Flash USDT Multi-Network Script

A comprehensive Python script for managing USDT (Tether) across multiple blockchain networks: **ERC20 (Ethereum)**, **BEP20 (Binance Smart Chain)**, and **TRC20 (TRON)**.

## 🌐 Supported Networks

- **Ethereum (ERC20)** - ETH Mainnet
- **Binance Smart Chain (BEP20)** - BSC Mainnet  
- **TRON (TRC20)** - TRON Mainnet

## 💼 Compatible Wallets

- **MetaMask** (Ethereum, BSC)
- **Trust Wallet** (Ethereum, BSC, TRON)
- **Binance Wallet** (Ethereum, BSC, TRON)
- **TronLink** (TRON)
- **Coinbase Wallet** (Ethereum, BSC)
- Any Web3-compatible wallet

## ✨ Features

- ✅ Check USDT balances across multiple networks
- ✅ Check native token balances (ETH, BNB, TRX)
- ✅ Transfer USDT on any supported network
- ✅ Track transaction status
- ✅ Multi-wallet management
- ✅ Web3 integration
- ✅ Secure private key handling

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

### 1. Basic Usage

Run the script to see supported networks:

```bash
python flash_usdt.py
```

### 2. Programmatic Usage

#### Check USDT Balance

```python
from flash_usdt import FlashUSDT

# Initialize
flash = FlashUSDT()

# Add Ethereum wallet
flash.add_wallet('my_eth_wallet', 'YOUR_PRIVATE_KEY', 'ethereum')

# Get wallet
wallet = flash.get_wallet('my_eth_wallet')

# Check balance
usdt_balance = wallet.get_balance()
eth_balance = wallet.get_native_balance()

print(f"USDT Balance: {usdt_balance}")
print(f"ETH Balance: {eth_balance}")
print(f"Address: {wallet.get_address()}")
```

#### Transfer USDT

```python
from flash_usdt import FlashUSDT

# Initialize and add wallet
flash = FlashUSDT()
flash.add_wallet('my_wallet', 'YOUR_PRIVATE_KEY', 'bsc')

# Get wallet
wallet = flash.get_wallet('my_wallet')

# Transfer USDT
tx_details = wallet.transfer_usdt(
    to_address='RECIPIENT_ADDRESS',
    amount=10.5  # Amount in USDT
)

print(f"Transaction Hash: {tx_details['tx_hash']}")
print(f"Status: {tx_details['status']}")

# Check transaction status
status = wallet.get_transaction_status(tx_details['tx_hash'])
print(f"Final Status: {status}")
```

#### Multi-Network Example

```python
from flash_usdt import FlashUSDT

# Initialize
flash = FlashUSDT()

# Add wallets for different networks
flash.add_wallet('eth_wallet', 'ETH_PRIVATE_KEY', 'ethereum')
flash.add_wallet('bsc_wallet', 'BSC_PRIVATE_KEY', 'bsc')
flash.add_wallet('tron_wallet', 'TRON_PRIVATE_KEY', 'tron')

# Get all balances
all_balances = flash.get_all_balances()

for wallet_name, info in all_balances.items():
    print(f"\n{wallet_name}:")
    print(f"  Network: {info['network']}")
    print(f"  Address: {info['address']}")
    print(f"  USDT: {info['usdt_balance']}")
    print(f"  Native: {info['native_balance']}")
```

## 🔐 Security Best Practices

### Environment Variables (Recommended)

Create a `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
```

Edit `.env` and add your private keys:

```env
ETH_PRIVATE_KEY=your_ethereum_private_key_here
BSC_PRIVATE_KEY=your_bsc_private_key_here
TRON_PRIVATE_KEY=your_tron_private_key_here
```

Load environment variables in your code:

```python
import os
from dotenv import load_dotenv
from flash_usdt import FlashUSDT

# Load environment variables
load_dotenv()

# Initialize with environment variables
flash = FlashUSDT()
flash.add_wallet('eth', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')
```

### Security Warnings

⚠️ **CRITICAL SECURITY RULES:**

1. **NEVER** share or commit your private keys
2. **NEVER** commit your `.env` file (it's in `.gitignore`)
3. **ALWAYS** test with small amounts first
4. **ALWAYS** verify recipient addresses carefully
5. **ALWAYS** use environment variables for private keys
6. **ALWAYS** keep your dependencies updated

## 📋 Network Details

### Ethereum (ERC20)
- **Chain ID**: 1
- **USDT Contract**: `0xdAC17F958D2ee523a2206206994597C13D831ec7`
- **Decimals**: 6
- **Explorer**: https://etherscan.io

### Binance Smart Chain (BEP20)
- **Chain ID**: 56
- **USDT Contract**: `0x55d398326f99059fF775485246999027B3197955`
- **Decimals**: 18
- **Explorer**: https://bscscan.com

### TRON (TRC20)
- **USDT Contract**: `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t`
- **Decimals**: 6
- **Explorer**: https://tronscan.org

## 🔧 Configuration

The `config.json` file contains network configurations, RPC endpoints, and gas settings. You can modify it to:

- Use custom RPC endpoints
- Adjust gas limits
- Change transaction priorities

## 📚 API Reference

### FlashUSDT Class

Main interface for managing multiple wallets.

#### Methods:
- `add_wallet(name, private_key, network)` - Add a wallet
- `get_wallet(name)` - Get wallet by name
- `get_all_balances()` - Get all wallet balances
- `cross_chain_info()` - Get network information

### USDTWallet Class

Individual wallet management.

#### Methods:
- `get_balance()` - Get USDT balance
- `get_native_balance()` - Get native token balance
- `transfer_usdt(to_address, amount)` - Transfer USDT
- `get_transaction_status(tx_hash)` - Check transaction status
- `get_address()` - Get wallet address

## 🧪 Testing

Before using with real funds, test with:

1. Testnets (Goerli, BSC Testnet, Nile)
2. Small amounts
3. Verified recipient addresses

## 🤝 Wallet Integration

### MetaMask
- Supports: Ethereum, BSC
- Export private key from MetaMask settings

### Trust Wallet
- Supports: Ethereum, BSC, TRON
- Export private key from wallet settings

### Binance Wallet
- Supports: Ethereum, BSC, TRON
- Export private key from wallet settings

### TronLink
- Supports: TRON
- Export private key from wallet settings

## 📄 License

This project is provided as-is for educational purposes.

## ⚡ Troubleshooting

### Common Issues

**"Insufficient funds for gas"**
- Ensure you have enough native tokens (ETH, BNB, or TRX) for gas fees

**"Invalid private key"**
- Check that private key format is correct (with or without '0x' prefix)

**"Transaction failed"**
- Verify recipient address is correct
- Check you have sufficient USDT balance
- Ensure network is not congested

**"Cannot connect to RPC"**
- Check your internet connection
- Try alternative RPC endpoints in config.json

## 🛠️ Requirements

- Python 3.8+
- web3.py
- tronpy
- eth-account

See `requirements.txt` for full dependency list.

## 💡 Tips

- Use environment variables for private keys
- Start with testnet before mainnet
- Always verify addresses before sending
- Keep track of transaction hashes
- Monitor gas prices for optimal transaction timing

---

**Made with ❤️ for the Web3 community**