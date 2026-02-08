# Advanced Usage & API Documentation

## Table of Contents
1. [Class Reference](#class-reference)
2. [Advanced Examples](#advanced-examples)
3. [Custom RPC Endpoints](#custom-rpc-endpoints)
4. [Error Handling](#error-handling)
5. [Transaction Monitoring](#transaction-monitoring)
6. [Batch Operations](#batch-operations)

## Class Reference

### FlashUSDT

Main interface for managing multiple USDT wallets across networks.

#### Methods

##### `__init__()`
Initialize the FlashUSDT manager.

```python
flash = FlashUSDT()
```

##### `add_wallet(name: str, private_key: str, network: str)`
Add a wallet to the manager.

**Parameters:**
- `name`: Unique identifier for the wallet
- `private_key`: Private key (with or without '0x' prefix)
- `network`: Network name ('ethereum', 'bsc', or 'tron')

```python
flash.add_wallet('my_wallet', private_key, 'ethereum')
```

##### `get_wallet(name: str) -> Optional[USDTWallet]`
Retrieve a wallet by name.

```python
wallet = flash.get_wallet('my_wallet')
```

##### `get_all_balances() -> Dict`
Get balances for all registered wallets.

```python
balances = flash.get_all_balances()
```

##### `cross_chain_info() -> Dict`
Get information about all supported networks.

```python
info = flash.cross_chain_info()
```

---

### USDTWallet

Individual wallet for USDT operations on a specific network.

#### Methods

##### `__init__(private_key: str, network: str)`
Initialize a wallet.

```python
from flash_usdt import USDTWallet
wallet = USDTWallet(private_key, 'ethereum')
```

##### `get_balance() -> Decimal`
Get USDT balance.

```python
balance = wallet.get_balance()
```

##### `get_native_balance() -> Decimal`
Get native token balance (ETH/BNB/TRX).

```python
native_balance = wallet.get_native_balance()
```

##### `get_address() -> str`
Get wallet address.

```python
address = wallet.get_address()
```

##### `transfer_usdt(to_address: str, amount: Union[int, float, Decimal]) -> Dict`
Transfer USDT to another address.

**Returns:**
```python
{
    'tx_hash': '0x...',
    'network': 'ethereum',
    'amount': '10.5',
    'to': '0x...',
    'status': 'pending'
}
```

##### `get_transaction_status(tx_hash: str) -> str`
Check transaction status.

**Returns:** 'pending', 'success', 'failed', or 'unknown'

---

## Advanced Examples

### 1. Transaction Monitoring

```python
from flash_usdt import FlashUSDT
import time
import os

flash = FlashUSDT()
flash.add_wallet('sender', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')
wallet = flash.get_wallet('sender')

# Send transaction
tx = wallet.transfer_usdt('0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb', 10)
print(f"Transaction sent: {tx['tx_hash']}")

# Monitor status
while True:
    status = wallet.get_transaction_status(tx['tx_hash'])
    print(f"Status: {status}")
    
    if status in ['success', 'failed']:
        break
    
    time.sleep(10)

print(f"Final status: {status}")
```

### 2. Multi-Network Balance Check

```python
from flash_usdt import FlashUSDT
from decimal import Decimal
import os

flash = FlashUSDT()

# Add wallets for all networks
networks = {
    'ethereum': os.getenv('ETH_PRIVATE_KEY'),
    'bsc': os.getenv('BSC_PRIVATE_KEY'),
    'tron': os.getenv('TRON_PRIVATE_KEY')
}

for network, key in networks.items():
    if key:
        flash.add_wallet(network, key, network)

# Get and display balances
balances = flash.get_all_balances()
total = Decimal('0')

print("=" * 70)
print("MULTI-NETWORK USDT PORTFOLIO")
print("=" * 70)

for name, info in balances.items():
    balance = Decimal(info['usdt_balance'])
    total += balance
    
    print(f"\n{name.upper()}")
    print(f"  Address: {info['address']}")
    print(f"  USDT:    {balance:,.2f} USDT")
    print(f"  Native:  {info['native_balance']}")

print("\n" + "=" * 70)
print(f"TOTAL PORTFOLIO: {total:,.2f} USDT")
print("=" * 70)
```

### 3. Conditional Transfer with Retry

```python
from flash_usdt import FlashUSDT
import time
import os

def transfer_with_retry(wallet, to_address, amount, max_retries=3):
    """Transfer with automatic retry on failure"""
    
    for attempt in range(max_retries):
        try:
            # Check balance first
            balance = wallet.get_balance()
            if float(balance) < amount:
                raise ValueError(f"Insufficient balance: {balance}")
            
            # Attempt transfer
            tx = wallet.transfer_usdt(to_address, amount)
            print(f"Attempt {attempt + 1}: Transaction sent")
            print(f"TX Hash: {tx['tx_hash']}")
            
            # Wait for confirmation
            time.sleep(15)
            status = wallet.get_transaction_status(tx['tx_hash'])
            
            if status == 'success':
                print("✓ Transaction successful!")
                return tx
            elif status == 'failed':
                print(f"✗ Transaction failed, retrying...")
                continue
            else:
                print("⏳ Transaction pending...")
                return tx
                
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
    
    raise Exception("All retry attempts failed")

# Usage
flash = FlashUSDT()
flash.add_wallet('sender', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')
wallet = flash.get_wallet('sender')

tx = transfer_with_retry(wallet, '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb', 10)
```

### 4. Cross-Network Transfer Coordinator

```python
from flash_usdt import FlashUSDT
import os

def find_best_network(flash, amount):
    """Find the network with sufficient balance and lowest fees"""
    
    balances = flash.get_all_balances()
    candidates = []
    
    for name, info in balances.items():
        usdt = float(info['usdt_balance'])
        if usdt >= amount:
            # Estimate fee (simplified)
            fee_estimate = {
                'ethereum': 10.0,  # Higher fees
                'bsc': 0.2,        # Low fees
                'tron': 0.15       # Low fees
            }
            
            candidates.append({
                'network': info['network'],
                'wallet': name,
                'balance': usdt,
                'fee': fee_estimate.get(info['network'], 1.0)
            })
    
    if not candidates:
        return None
    
    # Sort by fee (lowest first)
    candidates.sort(key=lambda x: x['fee'])
    return candidates[0]

# Usage
flash = FlashUSDT()
flash.add_wallet('eth', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')
flash.add_wallet('bsc', os.getenv('BSC_PRIVATE_KEY'), 'bsc')
flash.add_wallet('tron', os.getenv('TRON_PRIVATE_KEY'), 'tron')

amount = 50.0
best = find_best_network(flash, amount)

if best:
    print(f"Best network: {best['network']}")
    print(f"Estimated fee: ${best['fee']}")
    
    wallet = flash.get_wallet(best['wallet'])
    # Proceed with transfer...
else:
    print("Insufficient balance on all networks")
```

### 5. Batch Balance Monitor

```python
from flash_usdt import FlashUSDT
import time
import os
from datetime import datetime

def monitor_balances(flash, interval=60):
    """Monitor balances and alert on changes"""
    
    previous = {}
    
    while True:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        
        balances = flash.get_all_balances()
        
        for name, info in balances.items():
            current = float(info['usdt_balance'])
            
            if name in previous:
                change = current - previous[name]
                if change != 0:
                    symbol = "↑" if change > 0 else "↓"
                    print(f"{symbol} {name}: {previous[name]} → {current} USDT ({change:+.2f})")
            else:
                print(f"• {name}: {current} USDT")
            
            previous[name] = current
        
        time.sleep(interval)

# Usage
flash = FlashUSDT()
flash.add_wallet('eth', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')
flash.add_wallet('bsc', os.getenv('BSC_PRIVATE_KEY'), 'bsc')

# Monitor every 60 seconds
monitor_balances(flash, interval=60)
```

## Custom RPC Endpoints

You can use custom RPC endpoints by modifying the network configuration:

```python
from flash_usdt import USDTWallet, NetworkConfig

# Modify network config before initializing wallet
NetworkConfig.ETHEREUM_MAINNET['rpc_url'] = 'https://your-custom-rpc.com'
NetworkConfig.BSC_MAINNET['rpc_url'] = 'https://your-bsc-rpc.com'

# Now create wallet with custom RPC
wallet = USDTWallet(private_key, 'ethereum')
```

## Error Handling

### Best Practices

```python
from flash_usdt import FlashUSDT
import os

flash = FlashUSDT()

try:
    flash.add_wallet('test', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')
    wallet = flash.get_wallet('test')
    
    # Check balance before transfer
    balance = wallet.get_balance()
    amount = 10.0
    
    if float(balance) < amount:
        raise ValueError(f"Insufficient balance: {balance} < {amount}")
    
    # Check native token for gas
    native = wallet.get_native_balance()
    if float(native) < 0.001:
        print("Warning: Low native token balance for gas fees")
    
    # Execute transfer
    tx = wallet.transfer_usdt('0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb', amount)
    print(f"Success! TX: {tx['tx_hash']}")
    
except ValueError as e:
    print(f"Value error: {e}")
except ConnectionError as e:
    print(f"Connection error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Transaction Monitoring

### Detailed Status Tracking

```python
from flash_usdt import FlashUSDT
import time
import os

flash = FlashUSDT()
flash.add_wallet('sender', os.getenv('ETH_PRIVATE_KEY'), 'ethereum')
wallet = flash.get_wallet('sender')

# Send transaction
tx = wallet.transfer_usdt('0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb', 10)

# Track with timeout
timeout = 300  # 5 minutes
start_time = time.time()

while time.time() - start_time < timeout:
    status = wallet.get_transaction_status(tx['tx_hash'])
    elapsed = int(time.time() - start_time)
    
    print(f"[{elapsed}s] Status: {status}")
    
    if status == 'success':
        print("✓ Transaction confirmed!")
        break
    elif status == 'failed':
        print("✗ Transaction failed!")
        break
    
    time.sleep(15)
else:
    print("⚠ Timeout waiting for transaction")

# View on explorer
network = tx['network']
explorers = {
    'ethereum': 'https://etherscan.io/tx/',
    'bsc': 'https://bscscan.com/tx/',
    'tron': 'https://tronscan.org/#/transaction/'
}

print(f"View: {explorers[network]}{tx['tx_hash']}")
```

## Performance Tips

1. **Reuse wallet instances** - Don't create new wallets for each operation
2. **Cache balances** - If checking frequently, cache results
3. **Batch operations** - Group multiple checks together
4. **Use appropriate timeouts** - Network calls should have timeouts
5. **Handle rate limits** - Respect RPC endpoint rate limits

---

For more examples, see the `example_*.py` files in the repository.
