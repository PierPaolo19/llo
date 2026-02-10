# Quick Start Guide

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PierPaolo19/llo.git
   cd llo
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage Examples

### Method 1: Interactive Menu
```bash
python3 flash_usdt.py
```

Follow the on-screen menu to:
- Check USDT balances
- View token information
- Display network details

### Method 2: Run Examples
```bash
python3 examples.py
```

This will demonstrate:
- Balance checking across all networks
- Token information retrieval
- Network configuration display

### Method 3: Programmatic Usage

```python
from flash_usdt import USDTFlashTool

# Initialize the tool
tool = USDTFlashTool()

# Connect to Ethereum
tool.connect_to_network('ethereum')

# Check a balance
address = "0x..." # Your wallet address
balance = tool.get_balance('ethereum', address)
print(f"Balance: {balance} USDT")

# Get token info
info = tool.get_token_info('ethereum')
print(f"Token: {info['name']} ({info['symbol']})")
```

## Supported Networks

| Network | Type | USDT Contract |
|---------|------|---------------|
| Ethereum | ERC20 | 0xdAC17F958D2ee523a2206206994597C13D831ec7 |
| BSC | BEP20 | 0x55d398326f99059fF775485246999027B3197955 |
| TRON | TRC20 | TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t |

## Wallet Compatibility

This tool works with addresses from:
- ✅ MetaMask
- ✅ Trust Wallet
- ✅ Binance Wallet
- ✅ Any Web3-compatible wallet
- ✅ Hardware wallets (Ledger, Trezor)

## Features

- **Balance Checking**: Query USDT balance for any address
- **Multi-Network**: Supports Ethereum, BSC, and TRON
- **Token Info**: Get contract details and token metadata
- **Read-Only**: Safe, no transaction signing required
- **No Private Keys**: Only needs public wallet addresses

## Safety Notes

⚠️ **Important:**
- This tool only READS data from the blockchain
- You don't need private keys or seed phrases
- Always verify addresses before querying
- Use at your own risk - educational purposes only

## Troubleshooting

**Issue**: "web3 library not installed"
**Solution**: 
```bash
pip install web3
```

**Issue**: "TRC20 support disabled"
**Solution**:
```bash
pip install tronpy
```

**Issue**: "Failed to connect to network"
**Solution**:
- Check your internet connection
- Try again later
- RPC endpoints may be temporarily unavailable

## Advanced Usage

### Custom RPC Endpoints

Copy `.env.example` to `.env` and add your custom RPC endpoints:

```bash
cp .env.example .env
# Edit .env with your preferred RPC URLs
```

### Batch Balance Checking

```python
from flash_usdt import USDTFlashTool

addresses = [
    "0x...",  # Address 1
    "0x...",  # Address 2
    "0x...",  # Address 3
]

tool = USDTFlashTool()
tool.connect_to_network('ethereum')

for addr in addresses:
    balance = tool.get_balance('ethereum', addr)
    print(f"{addr}: {balance} USDT")
```

## Getting Help

- Check the [README.md](README.md) for detailed documentation
- Review [examples.py](examples.py) for code samples
- Open an issue on GitHub for bug reports

---

**Stay safe and verify everything!** 🔒
