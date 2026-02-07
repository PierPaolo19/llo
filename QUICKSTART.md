# Quick Start Guide

Get started with Flash USDT in under 5 minutes!

## Prerequisites

- Node.js v16 or higher
- npm or yarn
- Basic understanding of Ethereum and smart contracts

## Installation

```bash
# Clone the repository
git clone https://github.com/PierPaolo19/llo.git
cd llo

# Install dependencies
npm install
```

## Compile the Contracts

```bash
npm run compile
```

This will compile all Solidity contracts in the `contracts/` directory.

## Run the Tests

```bash
npm run test
```

You should see all tests passing:
```
✓ Should set the right owner
✓ Should set default fee to 9 basis points
✓ Should allow owner to add token support
✓ Should execute a successful flash loan
... and more
```

## Deploy to Local Network

1. Start a local Hardhat node in one terminal:
```bash
npx hardhat node
```

2. Deploy the contracts in another terminal:
```bash
npm run deploy
```

You'll see output like:
```
FlashLoanProvider deployed to: 0x5FbDB2315678afecb367f032d93F642f64180aa3
FlashLoanReceiverExample deployed to: 0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512
```

## Deploy to Testnet

1. Create a `.env` file:
```bash
cp .env.example .env
```

2. Add your configuration to `.env`:
```
PRIVATE_KEY=your_private_key_here
GOERLI_RPC_URL=https://goerli.infura.io/v3/YOUR_INFURA_KEY
ETHERSCAN_API_KEY=your_etherscan_key_here
```

3. Update `hardhat.config.js` to include your network:
```javascript
networks: {
  goerli: {
    url: process.env.GOERLI_RPC_URL,
    accounts: [process.env.PRIVATE_KEY]
  }
}
```

4. Deploy:
```bash
npx hardhat run scripts/deploy.js --network goerli
```

## Using Flash Loans

### Step 1: Create Your Receiver Contract

```solidity
pragma solidity ^0.8.20;

import "./IFlashLoanReceiver.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MyStrategy is IFlashLoanReceiver {
    address public immutable flashLoanProvider;
    
    constructor(address _provider) {
        flashLoanProvider = _provider;
    }
    
    function executeOperation(
        address token,
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        require(msg.sender == flashLoanProvider, "Unauthorized");
        
        // YOUR STRATEGY HERE
        // Example: arbitrage, liquidation, etc.
        
        // Repay the loan
        uint256 totalDebt = amount + fee;
        IERC20(token).approve(flashLoanProvider, totalDebt);
        
        return true;
    }
}
```

### Step 2: Request a Flash Loan

```javascript
const { ethers } = require("hardhat");

async function executeFlashLoan() {
    const provider = await ethers.getContractAt(
        "FlashLoanProvider",
        "0xYourProviderAddress"
    );
    
    const myStrategy = await ethers.getContractAt(
        "MyStrategy",
        "0xYourStrategyAddress"
    );
    
    const usdtAddress = "0xdAC17F958D2ee523a2206206994597C13D831ec7";
    const loanAmount = ethers.parseUnits("10000", 6); // 10k USDT
    
    await provider.flashLoan(
        myStrategy.address,
        usdtAddress,
        loanAmount,
        "0x" // params
    );
    
    console.log("Flash loan executed!");
}

executeFlashLoan();
```

## Example Use Case: Simple Arbitrage

Here's a complete example of using a flash loan for arbitrage:

```solidity
contract SimpleArbitrage is IFlashLoanReceiver {
    address public immutable flashLoanProvider;
    IUniswapV2Router public immutable dexA;
    IUniswapV2Router public immutable dexB;
    
    function executeOperation(
        address token,
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        // 1. Sell on DEX A
        uint256 receivedOnA = sellOnDex(dexA, token, amount);
        
        // 2. Buy back on DEX B
        uint256 receivedOnB = buyOnDex(dexB, token, receivedOnA);
        
        // 3. Ensure profit
        uint256 totalDebt = amount + fee;
        require(receivedOnB > totalDebt, "Not profitable");
        
        // 4. Repay loan
        IERC20(token).approve(flashLoanProvider, totalDebt);
        
        return true;
    }
}
```

## Troubleshooting

### "Token not supported" error
Make sure the token is added to the provider:
```javascript
await provider.setSupportedToken(tokenAddress, true);
```

### "Insufficient liquidity" error
The provider needs tokens. Deposit some:
```javascript
await token.transfer(providerAddress, amount);
```

### "Flash loan not repaid with fee" error
Make sure your strategy:
1. Generates enough profit to cover the fee
2. Approves the provider to pull tokens back
3. Has sufficient balance after operations

## Next Steps

1. **Read the documentation**: Check out [README.md](README.md) for detailed info
2. **Explore examples**: See [examples/EXAMPLES.md](examples/EXAMPLES.md) for more use cases
3. **Review security**: Read [SECURITY.md](SECURITY.md) before mainnet deployment
4. **Join the community**: Contribute via [CONTRIBUTING.md](CONTRIBUTING.md)

## Need Help?

- 📖 Read the [full documentation](README.md)
- 🔍 Browse [example contracts](examples/EXAMPLES.md)
- 🐛 Report issues on [GitHub](https://github.com/PierPaolo19/llo/issues)
- 💬 Ask questions in discussions

## Resources

- [Hardhat Documentation](https://hardhat.org/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts)
- [Flash Loans Explained](https://docs.aave.com/faq/flash-loans)

---

Happy flash loaning! 🚀
