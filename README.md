# llo

Flash USDT Script - A utility for simulating USDT operations.

## ⚠️ IMPORTANT DISCLAIMER

**This is a simulation tool for educational purposes only.** This script does NOT interact with real blockchains, cryptocurrency networks, or actual USDT tokens. All operations are simulated in memory and have no real-world financial impact. Do not use this for actual cryptocurrency transactions.

## Features

- **Multi-Network Support**: TRC20 (TRON), ERC20 (Ethereum), BEP20 (Binance Smart Chain)
- **Multi-Wallet Support**: Binance Wallet, Trust Wallet, MetaMask
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

The script supports three popular cryptocurrency wallets:
- **Binance Wallet**: Supports all networks (TRC20, ERC20, BEP20)
- **Trust Wallet**: Supports all networks (TRC20, ERC20, BEP20)
- **MetaMask**: Supports EVM-compatible networks only (ERC20, BEP20)

Note: The script validates wallet-network compatibility and will show an error if you try to use an incompatible combination (e.g., MetaMask with TRC20).

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

View transaction history with wallet info:
```bash
python flash_usdt.py --network TRC20 --wallet trust --balance 100.0 --flash 50.0 --transfer 20.0 --recipient TXYZabc123 --history
```

### Command-line Options

- `--network`: Blockchain network - TRC20, ERC20, or BEP20 (default: ERC20)
- `--wallet`: Wallet to use - binance, trust, or metamask (optional)
- `--balance`: Initial USDT balance (default: 0.0)
- `--flash`: Amount of USDT to flash (add instantly)
- `--transfer`: Amount of USDT to transfer
- `--recipient`: Recipient address for transfer (required with --transfer)
- `--history`: Show transaction history

## Examples

### Example 1: Flash USDT with MetaMask on ERC20
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

### Example 2: Flash USDT with Binance Wallet on BEP20
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

### Example 5: Wallet-Network Compatibility Check
```bash
$ python flash_usdt.py --network TRC20 --wallet metamask --balance 0 --flash 1000.0
✗ Error: MetaMask does not support TRC20. Supported networks: ERC20, BEP20
```

## Wallet-Network Compatibility Matrix

| Wallet | TRC20 | ERC20 | BEP20 |
|--------|-------|-------|-------|
| **Binance Wallet** | ✅ | ✅ | ✅ |
| **Trust Wallet** | ✅ | ✅ | ✅ |
| **MetaMask** | ❌ | ✅ | ✅ |

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This is a simulation script for educational purposes.