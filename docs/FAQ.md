# Flash USDT FAQ ❓

Frequently Asked Questions about Flash USDT and flash loans.

## 📋 Table of Contents

- [General Questions](#general-questions)
- [Technical Questions](#technical-questions)
- [Safety & Security](#safety--security)
- [Costs & Profitability](#costs--profitability)
- [Troubleshooting](#troubleshooting)

---

## General Questions

### What is Flash USDT?

Flash USDT is an open-source flash loan implementation for USDT (Tether) that works across multiple blockchain networks including Ethereum, BSC, Polygon, and Tron.

### Do I need collateral to use flash loans?

**No!** That's the beauty of flash loans. You don't need any collateral. The loan must simply be repaid within the same transaction.

### Is Flash USDT free to use?

The smart contracts are open-source and free to deploy. However, there is a small fee for using flash loans:
- **Fee**: 0.09% (9 basis points)
- **Example**: Borrow 10,000 USDT, pay 9 USDT fee

### Can anyone use Flash USDT?

Yes! Flash USDT is permissionless and open to everyone. You just need:
- A smart contract that implements the IFlashLoanReceiver interface
- Gas fees for transactions
- Basic understanding of how flash loans work

### What's the difference between Flash USDT and Aave flash loans?

| Feature | Flash USDT | Aave |
|---------|-----------|------|
| Token | USDT only | Multiple tokens |
| Fee | 0.09% | 0.09% |
| Networks | ETH, BSC, Polygon, Tron | Ethereum, Polygon |
| Open Source | Yes | Yes |
| Desktop App | Yes | No |

---

## Technical Questions

### How do I implement a flash loan receiver?

Your contract must implement the `IFlashLoanReceiver` interface:

```solidity
interface IFlashLoanReceiver {
    function executeOperation(
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external returns (bool);
}
```

**Example**:

```solidity
contract MyFlashLoan is IFlashLoanReceiver {
    function executeOperation(
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        // Your logic here
        
        // Approve repayment
        usdt.approve(msg.sender, amount + fee);
        return true;
    }
}
```

### What networks does Flash USDT support?

Flash USDT supports multiple networks:

**ERC20 Networks**:
- Ethereum Mainnet (Chain ID: 1)
- Sepolia Testnet (Chain ID: 11155111)
- Polygon Mainnet (Chain ID: 137)
- Mumbai Testnet (Chain ID: 80001)

**BEP20 Networks**:
- BSC Mainnet (Chain ID: 56)
- BSC Testnet (Chain ID: 97)

**TRC20 Networks**:
- Tron Mainnet
- Tron Shasta Testnet

See [NETWORKS.md](NETWORKS.md) for details.

### Can I use Flash USDT with other tokens?

Currently, Flash USDT only supports USDT. However, the contracts can be modified to work with any ERC20 token. You would need to:
1. Deploy your own instance
2. Change the token address
3. Provide liquidity for your chosen token

### How much can I borrow?

You can borrow up to the **total available liquidity** in the Flash USDT pool. This varies by network and over time as users deposit/withdraw.

To check available liquidity:
```solidity
uint256 available = usdt.balanceOf(address(flashUSDT));
```

### What happens if my transaction fails?

If your transaction fails for any reason:
- ❌ The entire transaction reverts
- ✅ You don't owe any money
- ✅ No debt is created
- ⚠️ You lose the gas fee for the failed transaction

### Can I call multiple flash loans in one transaction?

**Yes!** You can call multiple flash loans or even nest them:

```solidity
function multipleLoans() external {
    // First flash loan
    flashUSDT1.flashLoan(address(this), amount1, "");
}

function executeOperation(...) external override returns (bool) {
    // During first loan, call second flash loan
    flashUSDT2.flashLoan(address(this), amount2, "");
    // Your logic...
    return true;
}
```

---

## Safety & Security

### Is Flash USDT safe to use?

Flash USDT uses battle-tested patterns from OpenZeppelin and follows security best practices. However:

- ⚠️ **Not audited**: The code has not been professionally audited
- ⚠️ **Use at your own risk**: No warranties provided
- ✅ **Open source**: Code is public for review
- ✅ **Tested**: Comprehensive test suite included

### Can I lose money with flash loans?

**Direct losses**: No. If a flash loan transaction fails, it reverts completely. You only lose gas fees.

**Indirect losses**: Yes, possible through:
- Smart contract bugs in your code
- Poor strategy execution
- Market manipulation
- Oracle attacks
- Failed transactions costing gas

### What security measures should I implement?

**Essential Security Practices**:

1. ✅ **Input Validation**
```solidity
require(amount > 0, "Amount must be positive");
require(receiver != address(0), "Invalid receiver");
```

2. ✅ **Reentrancy Protection**
```solidity
bool private locked;
modifier noReentrant() {
    require(!locked, "Reentrant call");
    locked = true;
    _;
    locked = false;
}
```

3. ✅ **Access Control**
```solidity
address public owner;
modifier onlyOwner() {
    require(msg.sender == owner, "Not owner");
    _;
}
```

4. ✅ **Slippage Protection**
```solidity
require(
    amountOut >= minAmountOut,
    "Slippage too high"
);
```

5. ✅ **Deadline Checks**
```solidity
require(
    block.timestamp <= deadline,
    "Transaction expired"
);
```

### How do I test my flash loan contract safely?

**Testing Steps**:

1. **Unit Tests**: Test individual functions
```bash
npm test
```

2. **Testnet Deployment**: Deploy to Sepolia or BSC Testnet
```bash
npm run deploy:sepolia
```

3. **Small Amounts**: Start with minimal amounts (1-10 USDT)

4. **Gradual Scaling**: Slowly increase amounts

5. **Monitor Closely**: Watch all transactions on block explorers

### What are common security vulnerabilities?

**Top Vulnerabilities**:

1. **Reentrancy Attacks**
   - Always use `nonReentrant` modifier
   - Follow checks-effects-interactions pattern

2. **Integer Overflow/Underflow**
   - Use Solidity 0.8+ (has built-in protection)
   - Or use OpenZeppelin SafeMath

3. **Oracle Manipulation**
   - Use multiple price sources
   - Implement time-weighted averages
   - Validate price deviations

4. **Front-Running**
   - Use private transaction pools
   - Implement deadline parameters
   - Add slippage protection

5. **Access Control Issues**
   - Implement proper access modifiers
   - Use OpenZeppelin AccessControl
   - Validate all msg.sender checks

---

## Costs & Profitability

### What does a flash loan cost?

**Flash Loan Fee**: 0.09% of borrowed amount

**Gas Costs** (varies by network):
- Ethereum: $20-100+
- BSC: $0.50-5
- Polygon: $0.01-0.50

**Total Cost Example** (Ethereum):
```
Borrow: 100,000 USDT
Fee: 90 USDT (0.09%)
Gas: ~$50 (0.02 ETH @ $2,500)
Total: ~140 USDT
```

### How much can I profit?

Profits depend entirely on your strategy. Examples:

**Arbitrage** (varies greatly):
- Small opportunities: $10-50 per trade
- Medium opportunities: $100-500
- Large opportunities: $1,000+ (rare)

**Liquidation Protection**:
- Saves ~10% liquidation penalty
- On 100K position = saves $10,000

**Debt Refinancing**:
- Saves interest difference
- 3% APY on 100K = $3,000/year

### Is it profitable after gas costs?

**Break-even Calculation**:

```
On Ethereum (expensive gas):
Gas Cost: $50
Flash Loan Fee: 0.09%
Break-even: ~$50,090 borrowed

On BSC (cheap gas):
Gas Cost: $2
Flash Loan Fee: 0.09%
Break-even: ~$2,020 borrowed
```

**Tip**: Use cheaper networks (BSC, Polygon) for smaller trades.

### How often can I execute flash loans?

As often as you want! There's no limit. You could:
- Execute multiple per block
- Run 24/7 arbitrage bots
- Respond to market opportunities instantly

**Limitation**: Gas costs and competition with other bots.

---

## Troubleshooting

### My flash loan transaction failed. Why?

**Common Reasons**:

1. **Insufficient Repayment**
   ```
   Error: "Repayment failed"
   Solution: Ensure amount + fee is approved and available
   ```

2. **Out of Gas**
   ```
   Error: "Out of gas"
   Solution: Increase gas limit in transaction
   ```

3. **Slippage Too High**
   ```
   Error: "Slippage exceeded"
   Solution: Increase slippage tolerance or trade smaller amounts
   ```

4. **Deadline Passed**
   ```
   Error: "Transaction expired"
   Solution: Increase deadline parameter
   ```

5. **Insufficient Liquidity**
   ```
   Error: "Insufficient liquidity"
   Solution: Borrow less or wait for more liquidity
   ```

### How do I debug a failed transaction?

**Debugging Steps**:

1. **Check Transaction on Explorer**
   - View on Etherscan/BSCScan
   - Read error message
   - Check gas used

2. **Use Tenderly**
   - Paste transaction hash
   - See detailed execution trace
   - Identify failing line

3. **Test Locally**
   ```bash
   npx hardhat test
   ```

4. **Add Logging**
   ```solidity
   emit Debug("Step 1 completed", value);
   ```

5. **Try on Testnet First**
   - Deploy to Sepolia
   - Test with small amounts
   - Verify all functions

### MetaMask isn't connecting. What do I do?

**Solutions**:

1. **Check Network**
   - Ensure correct network selected
   - Match contract deployment network

2. **Clear Cache**
   - Settings → Advanced → Clear activity data

3. **Update MetaMask**
   - Should be latest version

4. **Check Permissions**
   - Settings → Connected sites
   - Verify Flash USDT has permission

5. **Try Different Browser**
   - Chrome, Firefox, or Brave

### I can't find the Flash USDT contract address

**Contract Addresses by Network**:

See [NETWORKS.md](NETWORKS.md) for complete list.

For latest deployments:
```bash
cd llo
cat deployments/[network]/FlashUSDT.json
```

### Gas prices are too high. What can I do?

**Solutions**:

1. **Use Cheaper Networks**
   - BSC: ~100x cheaper than Ethereum
   - Polygon: ~1000x cheaper

2. **Wait for Lower Gas**
   - Use [ETH Gas Station](https://ethgasstation.info/)
   - Trade during off-peak hours
   - Avoid network congestion

3. **Optimize Your Contract**
   - Minimize computations
   - Use efficient data structures
   - Batch operations

4. **Use Gas Tokens** (advanced)
   - GST2, CHI tokens
   - Pre-purchase gas when cheap

---

## Still Have Questions?

- 💬 **Ask in Discussions**: [GitHub Discussions](https://github.com/PierPaolo19/llo/discussions)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/PierPaolo19/llo/issues)
- 📖 **Read Docs**: [Documentation](README.md)
- 🎓 **Take Tutorials**: [Tutorial Series](tutorials/TUTORIAL_INDEX.md)

---

**Can't find your question?** Open a [new discussion](https://github.com/PierPaolo19/llo/discussions/new) and we'll help!
