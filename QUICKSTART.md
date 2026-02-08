# Flash USDT - Quick Start Guide

## What is This?

This script allows you to manage USDT (Tether stablecoin) across three major blockchain networks using Python.

## Supported Networks

1. **Ethereum (ERC20)** - The original Ethereum blockchain
2. **Binance Smart Chain (BEP20)** - Binance's blockchain network
3. **TRON (TRC20)** - TRON blockchain network

## Installation

```bash
# Clone the repository
git clone https://github.com/PierPaolo19/llo.git
cd llo

# Install dependencies
pip install -r requirements.txt
```

## Quick Examples

### 1. Check Balance

```python
from flash_usdt import FlashUSDT
import os

# Initialize
flash = FlashUSDT()

# Add wallet (use environment variable for security)
flash.add_wallet('my_wallet', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')

# Get wallet
wallet = flash.get_wallet('my_wallet')

# Check balances
print(f"Address: {wallet.get_address()}")
print(f"USDT: {wallet.get_balance()}")
print(f"ETH: {wallet.get_native_balance()}")
```

### 2. Transfer USDT on Ethereum

```python
from flash_usdt import FlashUSDT
import os

# Initialize and add wallet
flash = FlashUSDT()
flash.add_wallet('sender', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')

# Get wallet and transfer
wallet = flash.get_wallet('sender')
tx = wallet.transfer_usdt(
    to_address='0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb',
    amount=10.5
)

print(f"Transaction: https://etherscan.io/tx/{tx['tx_hash']}")
```

### 3. Transfer USDT on BSC

```python
from flash_usdt import FlashUSDT
import os

# Initialize with BSC network
flash = FlashUSDT()
flash.add_wallet('sender', os.getenv('BSC_PRIVATE_KEY'), 'bsc')

# Transfer
wallet = flash.get_wallet('sender')
tx = wallet.transfer_usdt(
    to_address='0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb',
    amount=5.0
)

print(f"Transaction: https://bscscan.com/tx/{tx['tx_hash']}")
```

### 4. Transfer USDT on TRON

```python
from flash_usdt import FlashUSDT
import os

# Initialize with TRON network
flash = FlashUSDT()
flash.add_wallet('sender', os.getenv('TRON_PRIVATE_KEY'), 'tron')

# Transfer
wallet = flash.get_wallet('sender')
tx = wallet.transfer_usdt(
    to_address='TLPcjEz5Zsrzpxr3jJvBHZYBU9VLYVJfPw',
    amount=15.0
)

print(f"Transaction: https://tronscan.org/#/transaction/{tx['tx_hash']}")
```

### 5. Manage Multiple Wallets

```python
from flash_usdt import FlashUSDT
import os

flash = FlashUSDT()

# Add multiple wallets
flash.add_wallet('eth', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')
flash.add_wallet('bsc', os.getenv('BSC_PRIVATE_KEY'), 'bsc')
flash.add_wallet('tron', os.getenv('TRON_PRIVATE_KEY'), 'tron')

# Get all balances at once
balances = flash.get_all_balances()

for name, info in balances.items():
    print(f"\n{name}: {info['usdt_balance']} USDT on {info['network']}")
```

## Setting Up Environment Variables

### Linux/Mac

```bash
# Create .env file
cp .env.example .env

# Edit .env and add your private keys
nano .env

# Load environment variables
export $(cat .env | xargs)
```

### Windows (PowerShell)

```powershell
# Create .env file
Copy-Item .env.example .env

# Edit .env with notepad
notepad .env

# Load environment variables
Get-Content .env | ForEach-Object { 
    $name, $value = $_.split('=')
    Set-Item -Path env:$name -Value $value
}
```

### Python Script

```python
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access variables
eth_key = os.getenv('ETH_PRIVATE_KEY')
bsc_key = os.getenv('BSC_PRIVATE_KEY')
tron_key = os.getenv('TRON_PRIVATE_KEY')
```

## Wallet Integration

### MetaMask

1. Open MetaMask
2. Click on account menu → Account Details
3. Click "Export Private Key"
4. Enter password and copy private key
5. Use in script: `flash.add_wallet('metamask', private_key, 'ethereum')`

### Trust Wallet

1. Open Trust Wallet
2. Go to Settings → Wallets
3. Select wallet → Show Recovery Phrase
4. Use a tool to convert mnemonic to private key
5. Use in script with appropriate network

### Binance Wallet

1. Open Binance Wallet
2. Go to Settings → Security
3. Export private key
4. Use in script with appropriate network

## Network Requirements

### Ethereum
- Need ETH for gas fees (recommended: 0.01+ ETH)
- USDT contract: `0xdAC17F958D2ee523a2206206994597C13D831ec7`

### BSC
- Need BNB for gas fees (recommended: 0.01+ BNB)
- USDT contract: `0x55d398326f99059fF775485246999027B3197955`

### TRON
- Need TRX for transaction fees (recommended: 10+ TRX)
- USDT contract: `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t`

## Security Best Practices

1. ✅ **Always use environment variables** for private keys
2. ✅ **Never commit** `.env` file to git
3. ✅ **Test with small amounts** first
4. ✅ **Double-check recipient addresses** before sending
5. ✅ **Keep backup** of your private keys securely
6. ✅ **Use hardware wallets** for large amounts
7. ✅ **Monitor transactions** on block explorers

## Common Issues

### "Insufficient funds for gas"
- Add more native tokens (ETH/BNB/TRX) to your wallet

### "Invalid private key"
- Ensure private key is 64 hex characters
- Can have optional '0x' prefix

### "Transaction failed"
- Check USDT balance is sufficient
- Verify recipient address is correct
- Ensure network is not congested

### "Cannot connect to RPC"
- Check internet connection
- Try alternative RPC in config.json
- Wait and retry if network is busy

## Block Explorers

- **Ethereum**: https://etherscan.io
- **BSC**: https://bscscan.com
- **TRON**: https://tronscan.org

## Gas Fees Comparison

| Network | Average Fee | Speed |
|---------|-------------|-------|
| Ethereum | $5-50 | 12-15 sec |
| BSC | $0.10-0.50 | 3 sec |
| TRON | $0.10-0.50 | 3 sec |

## Getting Test Tokens

### Testnets (for testing)
- **Ethereum Goerli**: https://goerlifaucet.com
- **BSC Testnet**: https://testnet.binance.org/faucet-smart
- **TRON Nile**: https://nileex.io/join/getJoinPage

## Support

For issues and questions:
- Check the README.md
- Review examples in `example_*.py` files
- Check configuration in `config.json`

## License

This project is provided as-is for educational purposes.

---

**Remember**: Cryptocurrency transactions are irreversible. Always verify everything before sending!
