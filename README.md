# llo

Flash USDT Script - A utility for simulating USDT operations.

## ⚠️ IMPORTANT DISCLAIMER

**This is a simulation tool for educational purposes only.** This script does NOT interact with real blockchains, cryptocurrency networks, or actual USDT tokens. All operations are simulated in memory and have no real-world financial impact. Do not use this for actual cryptocurrency transactions.

## Features

- Flash (instantly add) USDT to your balance
- Transfer USDT to recipients
- View transaction history
- Check balance

## Usage

### Basic Usage

Check balance:
```bash
python flash_usdt.py --balance 100.0
```

Flash USDT:
```bash
python flash_usdt.py --balance 100.0 --flash 50.0
```

Transfer USDT:
```bash
python flash_usdt.py --balance 100.0 --transfer 30.0 --recipient 0x1234567890abcdef
```

View transaction history:
```bash
python flash_usdt.py --balance 100.0 --flash 50.0 --transfer 20.0 --recipient 0xabcd --history
```

### Command-line Options

- `--balance`: Initial USDT balance (default: 0.0)
- `--flash`: Amount of USDT to flash (add instantly)
- `--transfer`: Amount of USDT to transfer
- `--recipient`: Recipient address for transfer (required with --transfer)
- `--history`: Show transaction history

## Examples

### Example 1: Flash and Check Balance
```bash
$ python flash_usdt.py --balance 0 --flash 1000.0
Flash USDT Script
==================================================
Initial Balance: 0.0 USDT

✓ Flashed 1000.0 USDT
  TX Hash: 0x...
  New Balance: 1000.0 USDT

Final Balance: 1000.0 USDT
```

### Example 2: Flash, Transfer, and View History
```bash
$ python flash_usdt.py --balance 0 --flash 500.0 --transfer 100.0 --recipient 0xRecipientAddress --history
Flash USDT Script
==================================================
Initial Balance: 0.0 USDT

✓ Flashed 500.0 USDT
  TX Hash: 0x...
  New Balance: 500.0 USDT

✓ Transferred 100.0 USDT to 0xRecipientAddress
  TX Hash: 0x...
  New Balance: 400.0 USDT

Transaction History:
--------------------------------------------------
1. FLASH
   Amount: 500.0 USDT
   Timestamp: 2026-02-07T...
   TX Hash: 0x...
   Balance After: 500.0 USDT

2. TRANSFER
   Amount: 100.0 USDT
   Recipient: 0xRecipientAddress
   Timestamp: 2026-02-07T...
   TX Hash: 0x...
   Balance After: 400.0 USDT

Final Balance: 400.0 USDT
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This is a simulation script for educational purposes.