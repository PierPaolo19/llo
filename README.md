# llo

Flash USDT Script - A utility for simulating USDT operations.

## ⚠️ IMPORTANT DISCLAIMER

**This is a simulation tool for educational purposes only.** This script does NOT interact with real blockchains, cryptocurrency networks, or actual USDT tokens. All operations are simulated in memory and have no real-world financial impact. Do not use this for actual cryptocurrency transactions.

## Features

- **Multi-Network Support**: TRC20 (TRON), ERC20 (Ethereum), BEP20 (Binance Smart Chain)
- Flash (instantly add) USDT to your balance
- Transfer USDT to recipients
- View transaction history with network information
- Check balance
- Network-specific transaction hash formats

## Usage

### Supported Networks

The script supports three blockchain networks:
- **TRC20**: TRON network (transaction hashes without 0x prefix)
- **ERC20**: Ethereum network (default, transaction hashes with 0x prefix)
- **BEP20**: Binance Smart Chain (transaction hashes with 0x prefix)

### Basic Usage

Check balance on default network (ERC20):
```bash
python flash_usdt.py --balance 100.0
```

Select a specific network:
```bash
python flash_usdt.py --network TRC20 --balance 100.0
```

Flash USDT on TRC20:
```bash
python flash_usdt.py --network TRC20 --balance 0 --flash 1000.0
```

Flash USDT on BEP20:
```bash
python flash_usdt.py --network BEP20 --balance 100.0 --flash 50.0
```

Transfer USDT on ERC20:
```bash
python flash_usdt.py --network ERC20 --balance 100.0 --transfer 30.0 --recipient 0x1234567890abcdef
```

View transaction history:
```bash
python flash_usdt.py --network TRC20 --balance 100.0 --flash 50.0 --transfer 20.0 --recipient TXYZabc123 --history
```

### Command-line Options

- `--network`: Blockchain network - TRC20, ERC20, or BEP20 (default: ERC20)
- `--balance`: Initial USDT balance (default: 0.0)
- `--flash`: Amount of USDT to flash (add instantly)
- `--transfer`: Amount of USDT to transfer
- `--recipient`: Recipient address for transfer (required with --transfer)
- `--history`: Show transaction history

## Examples

### Example 1: Flash USDT on TRC20 (TRON)
```bash
$ python flash_usdt.py --network TRC20 --balance 0 --flash 1000.0
Flash USDT Script
==================================================
Network: TRON (TRC20)
Initial Balance: 0.0 USDT

✓ Flashed 1000.0 USDT on TRC20
  TX Hash: eaddb6b9a7d839a95a91509999bd5b9ae7d5f21bf8430ac8ddfce0b15ade3f0f
  New Balance: 1000.0 USDT

Final Balance: 1000.0 USDT
```

### Example 2: Flash USDT on ERC20 (Ethereum)
```bash
$ python flash_usdt.py --network ERC20 --balance 0 --flash 1000.0
Flash USDT Script
==================================================
Network: Ethereum (ERC20)
Initial Balance: 0.0 USDT

✓ Flashed 1000.0 USDT on ERC20
  TX Hash: 0x60ec024f067a36ff2cec144565bfca7421c55ca1d3d8b9ac924bdc39452ab643
  New Balance: 1000.0 USDT

Final Balance: 1000.0 USDT
```

### Example 3: Flash USDT on BEP20 (Binance Smart Chain)
```bash
$ python flash_usdt.py --network BEP20 --balance 0 --flash 1000.0
Flash USDT Script
==================================================
Network: Binance Smart Chain (BEP20)
Initial Balance: 0.0 USDT

✓ Flashed 1000.0 USDT on BEP20
  TX Hash: 0x6f891add782263ccd7225193a1dfc920511d40f505487b9960b81cc72cdc4880
  New Balance: 1000.0 USDT

Final Balance: 1000.0 USDT
```

### Example 4: Full Workflow with TRC20
```bash
$ python flash_usdt.py --network TRC20 --balance 0 --flash 5000.0 --transfer 1500.0 --recipient TXYZabcdef1234567890ABCDEF --history
Flash USDT Script
==================================================
Network: TRON (TRC20)
Initial Balance: 0.0 USDT

✓ Flashed 5000.0 USDT on TRC20
  TX Hash: d57b125b369f00b72bb97c552eefb5e04c4d81d64bcdbe87600571e084e0f120
  New Balance: 5000.0 USDT

✓ Transferred 1500.0 USDT to TXYZabcdef1234567890ABCDEF on TRC20
  TX Hash: 704155511d8a8052bb64be5d86dfc13b29e9fa01585390e26dc07e5e760b23a6
  New Balance: 3500.0 USDT

Transaction History:
--------------------------------------------------
1. FLASH (TRC20)
   Amount: 5000.0 USDT
   Timestamp: 2026-02-07T23:42:04.988554
   TX Hash: d57b125b369f00b72bb97c552eefb5e04c4d81d64bcdbe87600571e084e0f120
   Balance After: 5000.0 USDT

2. TRANSFER (TRC20)
   Amount: 1500.0 USDT
   Recipient: TXYZabcdef1234567890ABCDEF
   Timestamp: 2026-02-07T23:42:04.988585
   TX Hash: 704155511d8a8052bb64be5d86dfc13b29e9fa01585390e26dc07e5e760b23a6
   Balance After: 3500.0 USDT

Final Balance: 3500.0 USDT
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This is a simulation script for educational purposes.