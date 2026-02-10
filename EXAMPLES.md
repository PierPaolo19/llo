# Usage Examples

This document provides practical examples of how to use the Multi-Network USDT Tool.

## Installation

```bash
# Clone the repository
git clone https://github.com/PierPaolo19/llo.git
cd llo

# Install dependencies
pip install -r requirements.txt
```

## Example 1: Interactive Menu

The simplest way to use the tool:

```bash
python3 flash_usdt.py
```

This will present an interactive menu where you can:
1. Check USDT balances
2. View token information
3. Display network information
4. Connect to all networks
5. Exit

## Example 2: Command Line Interface

Quick balance check from the command line:

```bash
# Check Ethereum balance
python3 cli.py ethereum 0x5754284f345afc66a98fbB0a0Afe71e0F007B949

# Check BSC balance
python3 cli.py bsc 0x8894E0a0c962CB723c1976a4421c95949bE2D4E3

# Check TRON balance
python3 cli.py tron TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE

# Get token info
python3 cli.py ethereum --info
```

## Example 3: Programmatic Usage

Use the tool in your own Python scripts:

### Basic Balance Check

```python
from flash_usdt import USDTFlashTool

# Initialize
tool = USDTFlashTool()

# Connect to Ethereum
if tool.connect_to_network('ethereum'):
    # Check balance
    address = "0x5754284f345afc66a98fbB0a0Afe71e0F007B949"
    balance = tool.get_balance('ethereum', address)
    
    if balance:
        print(f"Balance: {balance} USDT")
```

### Check Multiple Networks

```python
from flash_usdt import USDTFlashTool

# Initialize
tool = USDTFlashTool()

# Your wallet address
address = "0xYourAddressHere"

# Check across all networks
networks = ['ethereum', 'bsc']

for network in networks:
    if tool.connect_to_network(network):
        balance = tool.get_balance(network, address)
        if balance:
            print(f"{network.upper()}: {balance} USDT")
```

### Get Token Information

```python
from flash_usdt import USDTFlashTool

tool = USDTFlashTool()

# Connect and get token info
if tool.connect_to_network('ethereum'):
    info = tool.get_token_info('ethereum')
    
    if info:
        print(f"Token: {info['name']}")
        print(f"Symbol: {info['symbol']}")
        print(f"Decimals: {info['decimals']}")
        print(f"Contract: {info['contract']}")
```

### Monitor Multiple Addresses

```python
from flash_usdt import USDTFlashTool
import time

tool = USDTFlashTool()
tool.connect_to_network('ethereum')

# List of addresses to monitor
addresses = [
    "0xAddress1...",
    "0xAddress2...",
    "0xAddress3..."
]

print("Monitoring USDT balances...\n")

while True:
    for addr in addresses:
        balance = tool.get_balance('ethereum', addr)
        if balance:
            print(f"{addr[:10]}...: {balance:.2f} USDT")
    
    print("\n" + "="*50)
    time.sleep(300)  # Check every 5 minutes
```

## Example 4: Network Information

Display all supported networks and their configurations:

```python
from flash_usdt import USDTFlashTool

tool = USDTFlashTool()
tool.display_network_info()
```

## Example 5: Error Handling

Proper error handling in your scripts:

```python
from flash_usdt import USDTFlashTool

def check_balance_safe(network, address):
    """Safely check balance with error handling"""
    tool = USDTFlashTool()
    
    try:
        # Attempt connection
        if not tool.connect_to_network(network):
            return None, "Could not connect to network"
        
        # Get balance
        balance = tool.get_balance(network, address)
        
        if balance is None:
            return None, "Could not retrieve balance"
        
        return balance, None
        
    except Exception as e:
        return None, f"Error: {str(e)}"

# Usage
balance, error = check_balance_safe('ethereum', '0xYourAddress')

if error:
    print(f"Error: {error}")
else:
    print(f"Balance: {balance} USDT")
```

## Example 6: Batch Processing

Check balances for multiple addresses:

```python
from flash_usdt import USDTFlashTool

def batch_check_balances(network, addresses):
    """Check balances for multiple addresses"""
    tool = USDTFlashTool()
    
    if not tool.connect_to_network(network):
        print(f"Could not connect to {network}")
        return
    
    results = {}
    
    for address in addresses:
        balance = tool.get_balance(network, address)
        if balance is not None:
            results[address] = balance
    
    return results

# Usage
addresses = [
    "0xAddress1...",
    "0xAddress2...",
    "0xAddress3..."
]

results = batch_check_balances('ethereum', addresses)

for addr, balance in results.items():
    print(f"{addr}: {balance} USDT")
```

## Example 7: Running Examples Script

Run the included examples:

```bash
python3 examples.py
```

This will demonstrate:
- Checking balances across all networks
- Retrieving token information
- Displaying network configuration

## Example 8: Running Tests

Validate the installation:

```bash
python3 test_tool.py
```

This runs a comprehensive test suite covering:
- Module imports
- Tool initialization
- Network configuration
- Connection tests
- Token information retrieval
- Balance checking
- Display functions

## Tips for Usage

### 1. Use Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Custom RPC Endpoints
Copy `.env.example` to `.env` and add your RPC URLs:
```bash
cp .env.example .env
# Edit .env with your custom endpoints
```

### 3. Rate Limiting
If you're checking many addresses, add delays:
```python
import time
time.sleep(1)  # Wait 1 second between requests
```

### 4. Verify Addresses
Always verify addresses on blockchain explorers:
- Ethereum: https://etherscan.io
- BSC: https://bscscan.com
- TRON: https://tronscan.org

## Troubleshooting

### Issue: Module not found
```bash
pip install -r requirements.txt
```

### Issue: Connection timeout
- Check internet connection
- Try different RPC endpoint
- Wait and retry later

### Issue: Invalid address
- Verify address format
- Use blockchain explorer to validate
- Ensure address matches network type

## Additional Resources

- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [SECURITY.md](SECURITY.md) - Security information
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

---

**Remember:** This tool is for educational purposes only. Always verify information independently and never share private keys.
