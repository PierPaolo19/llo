# llo

## Flash USDT Python Script

A Python script for simulating USDT (Tether) flash loan operations and transactions.

### Features

- **Flash Loan Simulation**: Simulate borrowing USDT without collateral
- **Arbitrage Operations**: Execute price arbitrage between different markets
- **Fee Calculation**: Automatic fee calculation (0.09% default)
- **Profit Analysis**: Calculate net profit after fees and slippage
- **Transaction Safety**: Automatic reversion if operation is not profitable
- **Comprehensive Logging**: Detailed logging of all operations

### Installation

No external dependencies required! The script uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/PierPaolo19/llo.git
cd llo

# Make the script executable (optional)
chmod +x flash_usdt.py
```

### Requirements

- Python 3.7 or higher

### Usage

#### Run the Script

```bash
python flash_usdt.py
```

#### Import as a Module

```python
from flash_usdt import FlashUSDT, FlashLoanConfig
from decimal import Decimal

# Create a flash loan instance
flash = FlashUSDT()

# Execute a flash loan with arbitrage
result = flash.execute_flash_loan(
    amount=Decimal("10000"),      # Borrow 10,000 USDT
    buy_price=Decimal("0.999"),   # Buy price
    sell_price=Decimal("1.002")   # Sell price
)

print(result)
```

#### Custom Configuration

```python
from flash_usdt import FlashUSDT, FlashLoanConfig
from decimal import Decimal

# Create custom configuration
config = FlashLoanConfig(
    min_loan_amount=Decimal("1000"),
    max_loan_amount=Decimal("500000"),
    fee_percentage=Decimal("0.05"),
    slippage_tolerance=Decimal("0.3")
)

# Initialize with custom config
flash = FlashUSDT(config)
```

### How It Works

1. **Borrow**: Request a flash loan for a specific USDT amount
2. **Execute**: Perform arbitrage or other operations with borrowed funds
3. **Calculate**: Determine profit after fees and slippage
4. **Repay**: Return the borrowed amount plus fees
5. **Revert**: If not profitable, the entire transaction is reverted

### Examples

The script includes three demonstration examples:

1. **Profitable Arbitrage**: Shows a successful flash loan with profit
2. **Unprofitable Arbitrage**: Demonstrates automatic reversion when not profitable
3. **Large Scale Operation**: Example with larger amounts

### Configuration Options

- `min_loan_amount`: Minimum loan amount (default: 100 USDT)
- `max_loan_amount`: Maximum loan amount (default: 1,000,000 USDT)
- `fee_percentage`: Flash loan fee percentage (default: 0.09%)
- `slippage_tolerance`: Maximum acceptable slippage (default: 0.5%)
- `gas_limit`: Gas limit for transactions (default: 300,000)

### Flash Loan Status

The script tracks the following statuses:
- `PENDING`: Initial state
- `EXECUTING`: Operation in progress
- `SUCCESS`: Loan completed successfully
- `FAILED`: Operation failed
- `REVERTED`: Transaction reverted due to unprofitability

### Safety Features

- Amount validation (min/max limits)
- Automatic profit calculation
- Transaction reversion if unprofitable
- Comprehensive error handling
- Detailed logging

### Disclaimer

This is a simulation/educational tool for understanding flash loan mechanics. It does not interact with real blockchain networks or real USDT tokens. For production use, you would need to integrate with actual DeFi protocols (e.g., Aave, dYdX, Uniswap) and handle real blockchain transactions.

### License

MIT License