# Flash USDT - Multi-Chain Flash Loan Protocol

A simple, secure, and efficient flash loan implementation for USDT and other tokens across multiple blockchain networks.

> 🌐 **Multi-Network Support:** Works on Ethereum (ERC20), Binance Smart Chain (BEP20), Polygon, and TRON (TRC20). See [Network Guide](NETWORK_GUIDE.md) for deployment instructions.

> 📖 **New to desktop development?** Check out our [Desktop Usage Guide](DESKTOP_GUIDE.md) (ডেস্কটপ ব্যবহার গাইড) for step-by-step instructions on using this project on your computer!

## 🌟 Features

- **Multi-Chain Support**: Deploy on Ethereum, BSC, Polygon, and TRON networks
- **Flash Loans**: Borrow any amount of supported tokens within a single transaction
- **Low Fees**: Default fee of 0.09% (9 basis points), configurable by owner
- **Secure**: Built with OpenZeppelin contracts, includes reentrancy protection
- **Flexible**: Support for multiple token standards (ERC20, BEP20, TRC20)
- **Well-tested**: Comprehensive test suite included
- **Gas Optimized**: Efficient Solidity code with compiler optimizations

## 🌍 Supported Networks

| Network | Token Standard | Chain ID | Status |
|---------|---------------|----------|---------|
| Ethereum | ERC20 | 1 (Mainnet), 11155111 (Sepolia) | ✅ Supported |
| Binance Smart Chain | BEP20 | 56 (Mainnet), 97 (Testnet) | ✅ Supported |
| Polygon | ERC20 | 137 (Mainnet), 80001 (Mumbai) | ✅ Supported |
| TRON | TRC20 | Mainnet, Shasta | 📝 Documentation |

See the [Network Guide](NETWORK_GUIDE.md) for detailed deployment instructions for each network.

## 📋 What are Flash Loans?

Flash loans are uncollateralized loans that must be borrowed and repaid within the same transaction. They're commonly used for:

- **Arbitrage**: Exploiting price differences across DEXs
- **Collateral Swaps**: Changing collateral without closing positions
- **Liquidations**: Liquidating undercollateralized positions for profit
- **Refinancing**: Moving debt between protocols

## 🚀 Quick Start

### Prerequisites

- Node.js v16 or higher
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/PierPaolo19/llo.git
cd llo

# Install dependencies
npm install
```

### Compile Contracts

```bash
npm run compile
```

### Run Tests

```bash
npm run test
```

### Deploy

#### Local Deployment (for testing)
```bash
npm run deploy
```

#### Deploy to Specific Networks

```bash
# Ethereum Mainnet
npm run deploy:mainnet

# Binance Smart Chain
npm run deploy:bsc

# BSC Testnet
npm run deploy:bscTestnet

# Polygon Mainnet
npm run deploy:polygon

# Ethereum Sepolia Testnet
npm run deploy:sepolia
```

**For TRON (TRC20) deployment**, see the [Network Guide](NETWORK_GUIDE.md#tron-deployment-trc20) for detailed instructions.

### Network Configuration

Before deploying, configure your `.env` file with API keys:

```bash
cp .env.example .env
# Edit .env with your network RPC URLs, private key, and API keys
```

**Need API Keys?** See the [API Keys Guide](API_KEYS.md) for detailed instructions on obtaining:
- Alchemy/Infura API keys (RPC providers)
- Etherscan/BSCScan/PolygonScan API keys (contract verification)
- Optional: CoinMarketCap, Moralis, The Graph, and more

See [Network Guide](NETWORK_GUIDE.md) for complete setup instructions for each network.

## 📁 Project Structure

```
.
├── contracts/
│   ├── FlashLoanProvider.sol          # Main flash loan provider contract
│   ├── IFlashLoanReceiver.sol         # Interface for flash loan receivers
│   ├── FlashLoanReceiverExample.sol   # Example receiver implementation
│   └── MockERC20.sol                  # Mock token for testing
├── scripts/
│   └── deploy.js                      # Deployment script
├── test/
│   └── FlashLoanProvider.test.js      # Comprehensive test suite
├── hardhat.config.js                  # Hardhat configuration
└── package.json                       # Project dependencies
```

## 🔧 Usage

### For Liquidity Providers

1. Deploy the `FlashLoanProvider` contract
2. Add token support using `setSupportedToken(tokenAddress, true)`
3. Deposit tokens to the contract
4. Earn fees from flash loan usage

### For Borrowers

1. Create a contract implementing `IFlashLoanReceiver`
2. Implement the `executeOperation` function with your custom logic
3. Call `flashLoan` on the provider with your receiver address
4. Ensure you repay the loan + fee in the same transaction

### Example: Basic Flash Loan Receiver

```solidity
pragma solidity ^0.8.20;

import "./IFlashLoanReceiver.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MyFlashLoanReceiver is IFlashLoanReceiver {
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
        
        // Your custom logic here
        // Example: arbitrage, liquidation, etc.
        
        // Approve repayment
        uint256 totalDebt = amount + fee;
        IERC20(token).approve(flashLoanProvider, totalDebt);
        
        return true;
    }
}
```

### Example: Requesting a Flash Loan

```javascript
const flashLoanProvider = await ethers.getContractAt("FlashLoanProvider", providerAddress);
const myReceiver = await ethers.getContractAt("MyFlashLoanReceiver", receiverAddress);

// Request flash loan
const loanAmount = ethers.parseUnits("100000", 6); // 100k USDT
const params = ethers.AbiCoder.defaultAbiCoder().encode(["uint256"], [someValue]);

await flashLoanProvider.flashLoan(
    myReceiver.address,
    usdtAddress,
    loanAmount,
    params
);
```

## 🔐 Security

- Uses OpenZeppelin's battle-tested contracts
- Includes reentrancy guards
- Owner-controlled token support and fee management
- Maximum fee cap of 1%
- Comprehensive test coverage

### Security Considerations

- Always audit your flash loan receiver implementation
- Ensure you can repay the loan + fee before calling
- Be aware of potential MEV (Maximal Extractable Value) attacks
- Test thoroughly on testnet before mainnet deployment

## 🧪 Testing

The project includes comprehensive tests covering:

- Deployment and initialization
- Token support management
- Flash loan execution
- Fee calculations and updates
- Withdrawal functionality
- Edge cases and error conditions

Run tests with:
```bash
npm run test
```

## 📊 Gas Costs

Approximate gas costs (may vary):
- Deploy FlashLoanProvider: ~2,500,000 gas
- Flash loan execution: ~150,000-250,000 gas (depends on receiver logic)
- Add token support: ~45,000 gas

## 🛠️ Configuration

### Update Flash Loan Fee

```javascript
// Fee in basis points (9 = 0.09%)
await flashLoanProvider.setFlashLoanFee(9);
```

### Add Token Support

```javascript
await flashLoanProvider.setSupportedToken(tokenAddress, true);
```

### Withdraw Tokens

```javascript
await flashLoanProvider.withdraw(tokenAddress, amount, recipientAddress);
```

## 📜 Contract Addresses

Deploy your own instances or use community-deployed versions.

| Network | Chain ID | FlashLoanProvider | Status |
|---------|----------|------------------|--------|
| Ethereum Mainnet | 1 | TBD | Not deployed |
| Ethereum Sepolia | 11155111 | TBD | Not deployed |
| BSC Mainnet | 56 | TBD | Not deployed |
| BSC Testnet | 97 | TBD | Not deployed |
| Polygon Mainnet | 137 | TBD | Not deployed |
| Polygon Mumbai | 80001 | TBD | Not deployed |
| TRON Mainnet | - | TBD | Not deployed |

See [Network Guide](NETWORK_GUIDE.md) for deployment instructions.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Documentation

- **[API Keys Guide](API_KEYS.md)** - Complete guide to obtaining and configuring all API keys
- **[Network Guide](NETWORK_GUIDE.md)** - Complete multi-chain deployment guide (ERC20, BEP20, TRC20)
- **[Desktop Usage Guide](DESKTOP_GUIDE.md)** - Complete guide for using this project on your desktop (includes Bengali/বাংলা version)
- **[Quick Start](QUICKSTART.md)** - Get started in 5 minutes
- **[Implementation Details](IMPLEMENTATION.md)** - Technical architecture and design
- **[Security](SECURITY.md)** - Security best practices and vulnerability reporting
- **[Examples](examples/EXAMPLES.md)** - Code examples and use cases
- **[Contributing](CONTRIBUTING.md)** - Contribution guidelines

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This software is provided "as is", without warranty of any kind. Use at your own risk. Always conduct thorough testing and audits before deploying to mainnet or using with real funds.

## 🔗 Resources

- [Hardhat Documentation](https://hardhat.org/docs)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts)
- [Flash Loans Explained](https://docs.aave.com/faq/flash-loans)

## 📞 Support

For questions and support, please open an issue in the GitHub repository.

---

**Built with ❤️ for the DeFi community**