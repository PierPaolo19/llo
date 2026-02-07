# Getting Started with Flash USDT

This guide will help you get started with the Flash USDT project.

## Prerequisites

Before you begin, ensure you have:

- **Node.js** (v18 or higher)
- **npm** or **yarn**
- Basic understanding of:
  - Solidity smart contracts
  - Ethereum/EVM blockchain
  - DeFi concepts
  - Flash loans

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/PierPaolo19/llo.git
cd llo
```

### 2. Install Dependencies

```bash
npm install
```

This will install:
- Hardhat (development framework)
- OpenZeppelin Contracts (security-audited contract library)
- Hardhat Toolbox (testing and development tools)

### 3. Compile Contracts

```bash
npm run compile
```

This compiles all Solidity contracts and generates:
- ABI files in `artifacts/`
- TypeScript types in `typechain-types/`

### 4. Run Tests

```bash
npm test
```

Tests verify:
- Contract deployment
- Deposit/withdrawal functionality
- Flash loan execution
- Fee calculations
- Access control
- Error handling

## Quick Start Guide

### Option 1: Local Testing

#### Start Local Blockchain

In one terminal:
```bash
npm run node
```

This starts a local Hardhat network on `http://127.0.0.1:8545`

#### Deploy Contracts

In another terminal:
```bash
npm run deploy
```

This deploys:
1. MockUSDT (test token)
2. FlashUSDT (flash loan provider)
3. FlashLoanExample (example borrower)

### Option 2: Hardhat Console

Launch interactive console:
```bash
npx hardhat console --network localhost
```

Interact with contracts:
```javascript
// Get contract factories
const MockUSDT = await ethers.getContractFactory("MockUSDT");
const FlashUSDT = await ethers.getContractFactory("FlashUSDT");

// Deploy
const usdt = await MockUSDT.deploy();
const flashUSDT = await FlashUSDT.deploy(await usdt.getAddress());

// Get signers
const [owner, user1] = await ethers.getSigners();

// Provide liquidity
const amount = ethers.parseUnits("10000", 6); // 10K USDT
await usdt.connect(user1).approve(await flashUSDT.getAddress(), amount);
await flashUSDT.connect(user1).deposit(amount);

// Check liquidity
console.log(await flashUSDT.availableLiquidity());
```

## Project Structure

```
llo/
├── contracts/              # Solidity smart contracts
│   ├── FlashUSDT.sol      # Main flash loan contract
│   ├── IFlashLoanReceiver.sol  # Interface for borrowers
│   ├── MockUSDT.sol       # Test USDT token
│   └── FlashLoanExample.sol    # Example implementation
├── examples/               # Additional examples
│   └── ArbitrageExample.sol    # Arbitrage example
├── test/                   # Test suite
│   └── FlashUSDT.test.js  # Comprehensive tests
├── scripts/                # Deployment scripts
│   └── deploy.js          # Deploy script
├── docs/                   # Documentation
│   └── TECHNICAL.md       # Technical documentation
├── hardhat.config.js      # Hardhat configuration
├── package.json           # Dependencies
├── README.md              # Project overview
├── SECURITY.md            # Security policy
├── CONTRIBUTING.md        # Contribution guidelines
└── LICENSE                # MIT license
```

## Basic Usage Example

### 1. Create Your Flash Loan Receiver

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "./IFlashLoanReceiver.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MyFlashLoanStrategy is IFlashLoanReceiver {
    address public flashUSDT;
    IERC20 public usdt;
    
    constructor(address _flashUSDT, address _usdt) {
        flashUSDT = _flashUSDT;
        usdt = IERC20(_usdt);
    }
    
    function executeOperation(
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        require(msg.sender == flashUSDT, "Unauthorized");
        
        // YOUR CUSTOM LOGIC HERE
        // Example: arbitrage, liquidation, etc.
        
        // Repay the loan + fee
        uint256 totalDebt = amount + fee;
        usdt.transfer(flashUSDT, totalDebt);
        
        return true;
    }
}
```

### 2. Execute Flash Loan

```javascript
// Deploy your strategy
const MyStrategy = await ethers.getContractFactory("MyFlashLoanStrategy");
const strategy = await MyStrategy.deploy(flashUSDTAddress, usdtAddress);

// Fund strategy with fee amount
const loanAmount = ethers.parseUnits("5000", 6); // 5K USDT
const fee = await flashUSDT.calculateFee(loanAmount);
await usdt.transfer(await strategy.getAddress(), fee);

// Execute flash loan
await flashUSDT.flashLoan(
    await strategy.getAddress(),
    loanAmount,
    "0x" // params
);
```

## Configuration

### Hardhat Networks

Edit `hardhat.config.js` to add networks:

```javascript
networks: {
  // Local development
  hardhat: {
    chainId: 31337
  },
  
  // Ethereum Sepolia Testnet
  sepolia: {
    url: process.env.SEPOLIA_RPC_URL,
    accounts: [process.env.PRIVATE_KEY],
    chainId: 11155111
  },
  
  // Polygon Mumbai Testnet
  mumbai: {
    url: process.env.MUMBAI_RPC_URL,
    accounts: [process.env.PRIVATE_KEY],
    chainId: 80001
  }
}
```

### Environment Variables

Create `.env` file:

```bash
SEPOLIA_RPC_URL=https://sepolia.infura.io/v3/YOUR_KEY
MUMBAI_RPC_URL=https://polygon-mumbai.infura.io/v3/YOUR_KEY
PRIVATE_KEY=your_private_key_here
ETHERSCAN_API_KEY=your_etherscan_api_key
```

**IMPORTANT**: Never commit `.env` to version control!

## Common Commands

```bash
# Compile contracts
npm run compile

# Run tests
npm test

# Run tests with coverage
npx hardhat coverage

# Deploy to localhost
npm run deploy

# Deploy to specific network
npx hardhat run scripts/deploy.js --network sepolia

# Clean build artifacts
npx hardhat clean

# Start Hardhat console
npx hardhat console

# Run specific test file
npx hardhat test test/FlashUSDT.test.js

# Get help
npx hardhat help
```

## Troubleshooting

### Issue: "Cannot find module"

**Solution**: Run `npm install`

### Issue: "Out of gas"

**Solution**: 
- Increase gas limit in transaction
- Optimize contract logic
- Reduce loan amount

### Issue: "Flash loan not repaid"

**Solution**:
- Ensure receiver has enough USDT to pay fee
- Check receiver logic for errors
- Verify approve() was called

### Issue: "Insufficient liquidity"

**Solution**:
- Reduce loan amount
- Add more liquidity to pool
- Check available liquidity with `availableLiquidity()`

## Next Steps

1. **Read the Documentation**
   - [Technical Documentation](docs/TECHNICAL.md)
   - [Security Policy](SECURITY.md)
   - [Contributing Guide](CONTRIBUTING.md)

2. **Explore Examples**
   - See `contracts/FlashLoanExample.sol`
   - See `examples/ArbitrageExample.sol`

3. **Test on Testnets**
   - Deploy to Sepolia or Mumbai
   - Test with small amounts first
   - Monitor transactions on Etherscan

4. **Join the Community**
   - Open issues for bugs
   - Submit PRs for improvements
   - Star the repo if helpful!

## Safety Checklist

Before using on mainnet:

- [ ] Thoroughly tested on testnets
- [ ] Code reviewed by team
- [ ] Consider professional audit
- [ ] Understand all risks
- [ ] Start with small amounts
- [ ] Have emergency plan
- [ ] Monitor for issues
- [ ] Use multi-sig for ownership

## Resources

- [Hardhat Documentation](https://hardhat.org/)
- [OpenZeppelin](https://openzeppelin.com/)
- [Solidity Docs](https://docs.soliditylang.org/)
- [Ethereum Development](https://ethereum.org/developers)

## Support

Need help?
- Check [existing issues](https://github.com/PierPaolo19/llo/issues)
- Open a [new issue](https://github.com/PierPaolo19/llo/issues/new)
- Read the [FAQ](docs/TECHNICAL.md)

---

**Happy Flash Loaning! 💸**

Remember: With great power comes great responsibility.
