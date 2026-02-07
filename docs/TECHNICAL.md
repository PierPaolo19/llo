# Flash Loan Technical Documentation

## Contract Architecture

### FlashUSDT Contract

The main contract that provides flash loan functionality.

#### State Variables

```solidity
IERC20 public immutable usdt;           // USDT token address
uint256 public flashLoanFee = 9;        // Fee in basis points (0.09%)
uint256 public constant MAX_FLASH_LOAN_FEE = 100;  // Max 1%
uint256 public constant FEE_PRECISION = 10000;     // Fee precision
```

#### Key Functions

##### flashLoan()
```solidity
function flashLoan(
    address receiver,
    uint256 amount,
    bytes calldata params
) external nonReentrant
```

Executes a flash loan by:
1. Validating inputs
2. Transferring USDT to receiver
3. Calling executeOperation on receiver
4. Verifying repayment

**Parameters:**
- `receiver`: Contract implementing IFlashLoanReceiver
- `amount`: Amount to borrow (in USDT wei)
- `params`: Additional parameters passed to receiver

**Requires:**
- Sufficient liquidity
- Non-zero amount
- Valid receiver address

##### calculateFee()
```solidity
function calculateFee(uint256 amount) public view returns (uint256)
```

Calculates the fee for a given loan amount.

**Formula:** `fee = (amount * flashLoanFee) / FEE_PRECISION`

##### deposit()
```solidity
function deposit(uint256 amount) external
```

Allows users to provide liquidity to the flash loan pool.

##### withdraw()
```solidity
function withdraw(uint256 amount, address recipient) external onlyOwner
```

Allows contract owner to withdraw liquidity.

### IFlashLoanReceiver Interface

Contracts receiving flash loans must implement this interface:

```solidity
function executeOperation(
    uint256 amount,
    uint256 fee,
    address initiator,
    bytes calldata params
) external returns (bool);
```

**Parameters:**
- `amount`: Amount borrowed
- `fee`: Fee to be paid
- `initiator`: Address that initiated the flash loan
- `params`: Additional parameters

**Returns:** `true` if operation was successful

## Gas Optimization

### Techniques Used

1. **Immutable Variables**: `usdt` is immutable, saving gas on reads
2. **Early Validation**: Fails fast to save gas on invalid inputs
3. **Minimal Storage**: Uses memory where possible
4. **ReentrancyGuard**: Efficient protection against reentrancy

### Estimated Gas Costs

| Operation | Gas Cost (approximate) |
|-----------|----------------------|
| Flash Loan (simple) | ~150,000 gas |
| Deposit | ~50,000 gas |
| Withdraw | ~40,000 gas |

*Note: Actual costs vary based on receiver logic*

## Security Features

### 1. Reentrancy Protection

Uses OpenZeppelin's ReentrancyGuard modifier on `flashLoan()`:
```solidity
function flashLoan(...) external nonReentrant {
    // Protected code
}
```

### 2. Balance Verification

Ensures loan is repaid:
```solidity
require(
    balanceAfter >= balanceBefore + fee,
    "FlashUSDT: Flash loan not repaid"
);
```

### 3. Access Control

Owner-only functions use OpenZeppelin's Ownable:
```solidity
function setFlashLoanFee(uint256 newFee) external onlyOwner {
    // Only owner can update fee
}
```

### 4. Input Validation

All inputs are validated:
```solidity
require(receiver != address(0), "FlashUSDT: Invalid receiver");
require(amount > 0, "FlashUSDT: Amount must be greater than 0");
require(amount <= availableBalance, "FlashUSDT: Insufficient liquidity");
```

## Integration Guide

### Step 1: Deploy Contracts

```javascript
// Deploy FlashUSDT
const FlashUSDT = await ethers.getContractFactory("FlashUSDT");
const flashUSDT = await FlashUSDT.deploy(usdtAddress);
```

### Step 2: Provide Liquidity

```javascript
// Approve USDT
await usdt.approve(flashUSDTAddress, amount);

// Deposit liquidity
await flashUSDT.deposit(amount);
```

### Step 3: Implement Receiver

```solidity
contract MyStrategy is IFlashLoanReceiver {
    function executeOperation(
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        // Your logic here
        
        // Repay loan + fee
        uint256 totalDebt = amount + fee;
        IERC20(usdt).transfer(msg.sender, totalDebt);
        
        return true;
    }
}
```

### Step 4: Execute Flash Loan

```javascript
// Call flash loan
await flashUSDT.flashLoan(
    receiverAddress,
    loanAmount,
    encodedParams
);
```

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Invalid receiver" | Receiver is zero address | Provide valid address |
| "Amount must be greater than 0" | Loan amount is 0 | Specify positive amount |
| "Insufficient liquidity" | Pool doesn't have enough USDT | Reduce amount or add liquidity |
| "Flash loan not repaid" | Loan + fee not returned | Ensure receiver repays correctly |
| "Transfer failed" | USDT transfer failed | Check approvals and balances |
| "Operation execution failed" | Receiver's executeOperation failed | Debug receiver logic |

## Events

### FlashLoan
```solidity
event FlashLoan(
    address indexed receiver,
    address indexed initiator,
    uint256 amount,
    uint256 fee
);
```

Emitted when a flash loan is executed.

### Deposit
```solidity
event Deposit(address indexed depositor, uint256 amount);
```

Emitted when liquidity is deposited.

### Withdraw
```solidity
event Withdraw(address indexed recipient, uint256 amount);
```

Emitted when liquidity is withdrawn.

### FlashLoanFeeUpdated
```solidity
event FlashLoanFeeUpdated(uint256 oldFee, uint256 newFee);
```

Emitted when the flash loan fee is updated.

## Best Practices

### For Liquidity Providers

1. Understand the risks of providing liquidity
2. Monitor flash loan activity
3. Consider the fee structure
4. Start with small amounts

### For Borrowers

1. Test thoroughly on testnets
2. Handle all error cases
3. Calculate gas costs in advance
4. Ensure profitable trades before executing
5. Have enough funds for fees
6. Use proper error handling

### For Contract Owners

1. Set reasonable fees (0.05-0.1% typical)
2. Monitor for suspicious activity
3. Use multi-sig wallets
4. Implement emergency pause if needed
5. Regular security reviews

## Example Use Cases

### 1. Arbitrage

```solidity
function executeArbitrage() external {
    // 1. Flash loan USDT
    // 2. Buy token on DEX A
    // 3. Sell token on DEX B
    // 4. Repay flash loan + fee
    // 5. Keep profit
}
```

### 2. Collateral Swap

```solidity
function swapCollateral() external {
    // 1. Flash loan new collateral
    // 2. Deposit new collateral
    // 3. Withdraw old collateral
    // 4. Swap old to new collateral
    // 5. Repay flash loan + fee
}
```

### 3. Liquidation

```solidity
function liquidate() external {
    // 1. Flash loan USDT
    // 2. Liquidate undercollateralized position
    // 3. Claim liquidation bonus
    // 4. Repay flash loan + fee
    // 5. Keep profit
}
```
