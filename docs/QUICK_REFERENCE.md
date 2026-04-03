# Flash USDT Quick Reference

## Contract Addresses (Update After Deployment)

| Network | FlashUSDT | USDT |
|---------|-----------|------|
| Mainnet | TBD | 0xdac17f958d2ee523a2206206994597c13d831ec7 |
| Sepolia | TBD | TBD |
| Mumbai | TBD | TBD |

## Key Functions

### FlashUSDT.sol

#### Read Functions

```solidity
// Get available liquidity
function availableLiquidity() public view returns (uint256)

// Calculate fee for amount
function calculateFee(uint256 amount) public view returns (uint256)

// Get current fee (in basis points)
function flashLoanFee() public view returns (uint256)
```

#### Write Functions

```solidity
// Execute flash loan
function flashLoan(
    address receiver,
    uint256 amount,
    bytes calldata params
) external nonReentrant

// Deposit liquidity
function deposit(uint256 amount) external

// Withdraw liquidity (owner only)
function withdraw(uint256 amount, address recipient) external onlyOwner

// Update fee (owner only)
function setFlashLoanFee(uint256 newFee) external onlyOwner
```

### IFlashLoanReceiver.sol

```solidity
// Implement this in your contract
function executeOperation(
    uint256 amount,
    uint256 fee,
    address initiator,
    bytes calldata params
) external returns (bool)
```

## Common Code Snippets

### Deploy FlashUSDT

```javascript
const FlashUSDT = await ethers.getContractFactory("FlashUSDT");
const flashUSDT = await FlashUSDT.deploy(usdtAddress);
await flashUSDT.waitForDeployment();
```

### Provide Liquidity

```javascript
const amount = ethers.parseUnits("10000", 6); // 10K USDT
await usdt.approve(flashUSDTAddress, amount);
await flashUSDT.deposit(amount);
```

### Execute Flash Loan

```javascript
const loanAmount = ethers.parseUnits("5000", 6); // 5K USDT
const params = "0x"; // or encode your params

await flashUSDT.flashLoan(
    receiverAddress,
    loanAmount,
    params
);
```

### Calculate Fees

```javascript
const loanAmount = ethers.parseUnits("10000", 6);
const fee = await flashUSDT.calculateFee(loanAmount);
console.log("Fee:", ethers.formatUnits(fee, 6), "USDT");
```

### Check Liquidity

```javascript
const available = await flashUSDT.availableLiquidity();
console.log("Available:", ethers.formatUnits(available, 6), "USDT");
```

## Events

### FlashLoan Event

```solidity
event FlashLoan(
    address indexed receiver,
    address indexed initiator,
    uint256 amount,
    uint256 fee
)
```

Listen for events:
```javascript
flashUSDT.on("FlashLoan", (receiver, initiator, amount, fee) => {
    console.log("Flash loan executed:");
    console.log("- Receiver:", receiver);
    console.log("- Initiator:", initiator);
    console.log("- Amount:", ethers.formatUnits(amount, 6));
    console.log("- Fee:", ethers.formatUnits(fee, 6));
});
```

## Fee Structure

| Fee (basis points) | Percentage | Example on 10K USDT |
|-------------------|------------|---------------------|
| 5 | 0.05% | $5 |
| 9 (default) | 0.09% | $9 |
| 10 | 0.10% | $10 |
| 25 | 0.25% | $25 |
| 50 | 0.50% | $50 |

## Error Messages

| Error | Meaning | Solution |
|-------|---------|----------|
| "Invalid receiver" | Zero address provided | Use valid address |
| "Amount must be greater than 0" | Zero loan amount | Use positive amount |
| "Insufficient liquidity" | Not enough USDT in pool | Add liquidity or reduce amount |
| "Flash loan not repaid" | Loan + fee not returned | Check receiver logic |
| "Unauthorized caller" | Wrong caller | Verify addresses |
| "Fee exceeds maximum" | Fee > 1% | Use lower fee |

## Gas Estimates

| Operation | Gas (approx) |
|-----------|--------------|
| Flash Loan (simple) | 150,000 |
| Flash Loan (with logic) | 200,000+ |
| Deposit | 50,000 |
| Withdraw | 40,000 |
| Update Fee | 30,000 |

## Security Checklist

- [ ] Test on testnet first
- [ ] Verify all contract addresses
- [ ] Ensure sufficient funds for fees
- [ ] Check gas prices
- [ ] Test with small amounts
- [ ] Monitor for suspicious activity
- [ ] Use multi-sig for ownership
- [ ] Have emergency plan

## Common Patterns

### Pattern 1: Simple Arbitrage

```solidity
function executeOperation(...) external override returns (bool) {
    // 1. Swap on DEX A
    // 2. Swap on DEX B
    // 3. Calculate profit
    // 4. Repay loan + fee
    return true;
}
```

### Pattern 2: Collateral Swap

```solidity
function executeOperation(...) external override returns (bool) {
    // 1. Deposit new collateral
    // 2. Withdraw old collateral
    // 3. Swap old to new
    // 4. Repay loan + fee
    return true;
}
```

### Pattern 3: Liquidation

```solidity
function executeOperation(...) external override returns (bool) {
    // 1. Liquidate position
    // 2. Claim bonus
    // 3. Sell collateral
    // 4. Repay loan + fee
    return true;
}
```

## Testing Commands

```bash
# Run all tests
npm test

# Run specific test
npx hardhat test test/FlashUSDT.test.js

# Run with gas reporter
REPORT_GAS=true npm test

# Run with coverage
npx hardhat coverage

# Run demo script
npx hardhat run scripts/demo.js
```

## Useful Links

- [Repository](https://github.com/PierPaolo19/llo)
- [Issues](https://github.com/PierPaolo19/llo/issues)
- [Hardhat Docs](https://hardhat.org/)
- [OpenZeppelin](https://openzeppelin.com/)

## Constants

```solidity
MAX_FLASH_LOAN_FEE = 100 // 1% maximum
FEE_PRECISION = 10000    // Basis points
DEFAULT_FEE = 9          // 0.09%
```

## USDT Decimals

**IMPORTANT**: USDT uses 6 decimals (not 18 like most tokens)

```javascript
// Correct
ethers.parseUnits("1000", 6) // 1000 USDT

// Wrong
ethers.parseUnits("1000", 18) // Way too much!
```

## Support

Questions? Issues?
- 📖 Read [docs/GETTING_STARTED.md](GETTING_STARTED.md)
- 🐛 Report [bugs](https://github.com/PierPaolo19/llo/issues)
- 💬 Ask [questions](https://github.com/PierPaolo19/llo/discussions)
