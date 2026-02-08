# llo

Flash USDT Script - A utility for simulating USDT operations.

## ⚠️ IMPORTANT DISCLAIMER

**This is a simulation tool for educational purposes only.** This script does NOT interact with real blockchains, cryptocurrency networks, or actual USDT tokens. All operations are simulated in memory and have no real-world financial impact. Do not use this for actual cryptocurrency transactions.

## Features

- **Multi-Network Support**: TRC20 (TRON), ERC20 (Ethereum), BEP20 (Binance Smart Chain)
- **Multi-Wallet Support**: Including popular Web3 wallets
  - Centralized: Binance Wallet
  - Decentralized: Trust Wallet
  - Web3: MetaMask, WalletConnect, Coinbase Wallet, Phantom, Rainbow
- **Comprehensive System Check**: Check all configurations, balances, and transactions at once
- Flash (instantly add) USDT to your balance
- Transfer USDT to recipients
- View transaction history with network and wallet information
- Check balance
- Network-specific transaction hash formats
- Wallet-network compatibility validation

## Usage

### Supported Networks

The script supports three blockchain networks:
- **TRC20**: TRON network (transaction hashes without 0x prefix)
- **ERC20**: Ethereum network (default, transaction hashes with 0x prefix)
- **BEP20**: Binance Smart Chain (transaction hashes with 0x prefix)

### Supported Wallets

The script supports seven popular cryptocurrency wallets:

**Traditional Wallets:**
- **Binance Wallet**: Supports all networks (TRC20, ERC20, BEP20) - Centralized exchange wallet
- **Trust Wallet**: Supports all networks (TRC20, ERC20, BEP20) - Multi-chain mobile wallet

**Web3 Wallets:**
- **MetaMask**: Supports EVM-compatible networks (ERC20, BEP20) - Leading Web3 browser wallet
- **WalletConnect**: Supports all networks (TRC20, ERC20, BEP20) - Open protocol for dApp connections
- **Coinbase Wallet**: Supports EVM-compatible networks (ERC20, BEP20) - Self-custody Web3 wallet
- **Phantom**: Supports EVM-compatible networks (ERC20, BEP20) - Multi-chain Web3 wallet
- **Rainbow**: Supports Ethereum only (ERC20) - Ethereum-focused Web3 wallet

Note: The script validates wallet-network compatibility and will show an error if you try to use an incompatible combination (e.g., Rainbow with BEP20).

### Basic Usage

Check balance on default network (ERC20):
```bash
python flash_usdt.py --balance 100.0
```

Use a specific wallet:
```bash
python flash_usdt.py --network ERC20 --wallet metamask --balance 100.0
```

Select a specific network with wallet:
```bash
python flash_usdt.py --network TRC20 --wallet trust --balance 100.0
```

Flash USDT with Binance Wallet on BEP20:
```bash
python flash_usdt.py --network BEP20 --wallet binance --balance 0 --flash 1000.0
```

Flash USDT with MetaMask on ERC20:
```bash
python flash_usdt.py --network ERC20 --wallet metamask --balance 100.0 --flash 50.0
```

Transfer USDT with Trust Wallet:
```bash
python flash_usdt.py --network ERC20 --wallet trust --balance 100.0 --transfer 30.0 --recipient 0x1234567890abcdef
```

Use Web3 wallets:
```bash
# WalletConnect on any network
python flash_usdt.py --network TRC20 --wallet walletconnect --balance 100.0 --flash 50.0

# Coinbase Wallet on Ethereum
python flash_usdt.py --network ERC20 --wallet coinbase --balance 0 --flash 1000.0

# Phantom on BSC
python flash_usdt.py --network BEP20 --wallet phantom --balance 0 --flash 500.0

# Rainbow on Ethereum only
python flash_usdt.py --network ERC20 --wallet rainbow --balance 0 --flash 250.0
```

View transaction history with wallet info:
```bash
python flash_usdt.py --network TRC20 --wallet trust --balance 100.0 --flash 50.0 --transfer 20.0 --recipient TXYZabc123 --history
```

### Command-line Options

- `--network`: Blockchain network - TRC20, ERC20, or BEP20 (default: ERC20)
- `--wallet`: Wallet to use - binance, trust, metamask, walletconnect, coinbase, phantom, or rainbow (optional)
- `--balance`: Initial USDT balance (default: 0.0)
- `--flash`: Amount of USDT to flash (add instantly)
- `--transfer`: Amount of USDT to transfer
- `--recipient`: Recipient address for transfer (required with --transfer)
- `--history`: Show transaction history
- `--check-all`: Perform comprehensive system check

## Examples

### Example 1: Comprehensive System Check
```bash
$ python flash_usdt.py --check-all
Flash USDT Script
==================================================
Network: Ethereum (ERC20)
Initial Balance: 0.0 USDT

System Check Results:
==================================================
Status: OK
Timestamp: 2026-02-08T00:11:25.628858

Network Information:
  Current Network: Ethereum (ERC20) (ERC20)
  Explorer: https://etherscan.io/tx/
  Available Networks: TRC20, ERC20, BEP20

Wallet Information:
  Current Wallet: None
  Available Wallets: binance, trust, metamask, walletconnect, coinbase, phantom, rainbow

Balance Information:
  Current Balance: 0.0 USDT

Transaction Information:
  Total Transactions: 0

Configuration:
  Networks Configured: 3
  Wallets Configured: 7
```

### Example 2: System Check with Specific Network and Wallet
```bash
$ python flash_usdt.py --network TRC20 --wallet walletconnect --balance 1000 --check-all
Flash USDT Script
==================================================
Network: TRON (TRC20)
Wallet: WalletConnect
Initial Balance: 1000.0 USDT

System Check Results:
==================================================
Status: OK
Timestamp: 2026-02-08T00:11:31.784959

Network Information:
  Current Network: TRON (TRC20) (TRC20)
  Explorer: https://tronscan.org/#/transaction/
  Available Networks: TRC20, ERC20, BEP20

Wallet Information:
  Current Wallet: WalletConnect
  Available Wallets: binance, trust, metamask, walletconnect, coinbase, phantom, rainbow

Balance Information:
  Current Balance: 1000.0 USDT

Transaction Information:
  Total Transactions: 0

Configuration:
  Networks Configured: 3
  Wallets Configured: 7
```

### Example 3: Flash USDT with MetaMask on ERC20
```bash
$ python flash_usdt.py --network ERC20 --wallet metamask --balance 0 --flash 1000.0
Flash USDT Script
==================================================
Network: Ethereum (ERC20)
Wallet: MetaMask
Initial Balance: 0.0 USDT

✓ Flashed 1000.0 USDT on ERC20 via MetaMask
  TX Hash: 0xe8c0da6252bb2f617fdd8c1d24f14b497569ee94721253375fa8b70c2fd3dad3
  New Balance: 1000.0 USDT

Final Balance: 1000.0 USDT
```

### Example 4: Flash USDT with Binance Wallet on BEP20
```bash
$ python flash_usdt.py --network BEP20 --wallet binance --balance 0 --flash 2000.0
Flash USDT Script
==================================================
Network: Binance Smart Chain (BEP20)
Wallet: Binance Wallet
Initial Balance: 0.0 USDT

✓ Flashed 2000.0 USDT on BEP20 via Binance Wallet
  TX Hash: 0x656ddcc1639f9b04aac157a1c72a19726f844c5a0af584e401b52dc7c0cf7d40
  New Balance: 2000.0 USDT

Final Balance: 2000.0 USDT
```

### Example 3: Flash USDT with Trust Wallet on TRC20
```bash
$ python flash_usdt.py --network TRC20 --wallet trust --balance 0 --flash 1500.0
Flash USDT Script
==================================================
Network: TRON (TRC20)
Wallet: Trust Wallet
Initial Balance: 0.0 USDT

✓ Flashed 1500.0 USDT on TRC20 via Trust Wallet
  TX Hash: a885c1bcf18889be5c41db8fe9674e796d15563020d6d6b6b97fecdb848662af
  New Balance: 1500.0 USDT

Final Balance: 1500.0 USDT
```

### Example 4: Full Workflow with Trust Wallet
```bash
$ python flash_usdt.py --network ERC20 --wallet trust --balance 0 --flash 500.0 --transfer 200.0 --recipient 0xABCD1234 --history
Flash USDT Script
==================================================
Network: Ethereum (ERC20)
Wallet: Trust Wallet
Initial Balance: 0.0 USDT

✓ Flashed 500.0 USDT on ERC20 via Trust Wallet
  TX Hash: 0x2454f59c21c0fc07878b259a1be27ccca1c8f5274d049d1562cb314ff696c3bc
  New Balance: 500.0 USDT

✓ Transferred 200.0 USDT to 0xABCD1234 on ERC20 via Trust Wallet
  TX Hash: 0x45431b5d6e569c465bab47216f031ecfca4902784789672e323b60f779fa7d29
  New Balance: 300.0 USDT

Transaction History:
--------------------------------------------------
1. FLASH (ERC20 via Trust Wallet)
   Amount: 500.0 USDT
   Timestamp: 2026-02-07T23:50:05.902040
   TX Hash: 0x2454f59c21c0fc07878b259a1be27ccca1c8f5274d049d1562cb314ff696c3bc
   Balance After: 500.0 USDT

2. TRANSFER (ERC20 via Trust Wallet)
   Amount: 200.0 USDT
   Recipient: 0xABCD1234
   Timestamp: 2026-02-07T23:50:05.902093
   TX Hash: 0x45431b5d6e569c465bab47216f031ecfca4902784789672e323b60f779fa7d29
   Balance After: 300.0 USDT

Final Balance: 300.0 USDT
```

### Example 7: Web3 Wallet with WalletConnect on TRC20
```bash
$ python flash_usdt.py --network TRC20 --wallet walletconnect --balance 0 --flash 1000.0
Flash USDT Script
==================================================
Network: TRON (TRC20)
Wallet: WalletConnect
Initial Balance: 0.0 USDT

✓ Flashed 1000.0 USDT on TRC20 via WalletConnect
  TX Hash: 50a440b1ac81db7c2693c517451e35f62042bf4b65dcd92ff76debe1fd3b9266
  New Balance: 1000.0 USDT

Final Balance: 1000.0 USDT
```

### Example 8: Web3 Wallet with Coinbase Wallet on ERC20
```bash
$ python flash_usdt.py --network ERC20 --wallet coinbase --balance 0 --flash 2000.0
Flash USDT Script
==================================================
Network: Ethereum (ERC20)
Wallet: Coinbase Wallet
Initial Balance: 0.0 USDT

✓ Flashed 2000.0 USDT on ERC20 via Coinbase Wallet
  TX Hash: 0xe857dd9cdd64cf0d6e8625e915d9d93125aa60020ecb5e30df3bb6d93a1a6a5b
  New Balance: 2000.0 USDT

Final Balance: 2000.0 USDT
```

### Example 9: Web3 Wallet Compatibility Check
```bash
$ python flash_usdt.py --network BEP20 --wallet rainbow --balance 0 --flash 1000.0
✗ Error: Rainbow does not support BEP20. Supported networks: ERC20
```

## Wallet-Network Compatibility Matrix

| Wallet | TRC20 | ERC20 | BEP20 | Type |
|--------|-------|-------|-------|------|
| **Binance Wallet** | ✅ | ✅ | ✅ | Centralized |
| **Trust Wallet** | ✅ | ✅ | ✅ | Decentralized |
| **MetaMask** | ❌ | ✅ | ✅ | Web3 |
| **WalletConnect** | ✅ | ✅ | ✅ | Web3 |
| **Coinbase Wallet** | ❌ | ✅ | ✅ | Web3 |
| **Phantom** | ❌ | ✅ | ✅ | Web3 |
| **Rainbow** | ❌ | ✅ | ❌ | Web3 |

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This is a simulation script for educational purposes.