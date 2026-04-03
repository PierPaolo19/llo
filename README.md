# Flash USDT 💸

An open-source flash loan implementation for USDT (Tether) supporting multiple blockchain networks: **ERC20** (Ethereum, Polygon), **BEP20** (Binance Smart Chain), and **TRC20** (Tron).

> 🎓 **New to Flash Loans?** Start with our **[Education Hub](docs/EDUCATION.md)** and **[Tutorial Series](docs/tutorials/TUTORIAL_INDEX.md)**!

> 🇧🇩 **বাংলায় PC ইনস্টল গাইড (Bengali PC Installation Guide):** [PC_INSTALL_BENGALI.md](PC_INSTALL_BENGALI.md)  
> "ati pc te ki vabe install korbo" - সম্পূর্ণ উত্তর এখানে!

## 🌐 Multi-Chain Support

Flash USDT now works across multiple networks:

- **🔷 ERC20**: Ethereum Mainnet, Sepolia, Polygon, Mumbai
- **🟡 BEP20**: Binance Smart Chain (BSC) Mainnet & Testnet
- **🔴 TRC20**: Tron Mainnet & Shasta (requires separate tooling)

See [Network Documentation](docs/NETWORKS.md) for detailed network information.

## ⚠️ Disclaimer

**IMPORTANT**: This project is for educational and development purposes. Flash loans can be used for both legitimate DeFi operations (arbitrage, collateral swaps, liquidations) and malicious attacks. Use responsibly and ensure you understand the security implications.

- **Not audited**: This code has not been professionally audited
- **Use at your own risk**: No warranties or guarantees are provided
- **Test thoroughly**: Always test on testnets before mainnet deployment
- **Legal compliance**: Ensure compliance with local regulations

## 🚀 Features

- **Zero-collateral loans**: Borrow USDT without collateral
- **Atomic transactions**: Loans must be repaid within the same transaction
- **Low fees**: Default fee of 0.09% (9 basis points)
- **Multi-chain support**: Deploy on Ethereum, BSC, Polygon, or Tron
- **Flexible**: Easy to integrate into your DeFi strategies
- **Gas optimized**: Built with efficiency in mind for all supported chains
- **Well-tested**: Comprehensive test suite included
- **Desktop Application**: User-friendly GUI for managing flash loans across networks
- **Windows 10 Pro optimized**: Full support with detailed setup guide and installers
- **Android support**: Use with MetaMask Mobile or Trust Wallet; Magisk v30.7 compatible

## 📋 Prerequisites

### For Smart Contract Development
- Node.js (v18 or higher)
- npm or yarn
- Hardhat

### For Desktop Application
- **Windows 10 Pro / Home / Enterprise** (Version 1903+) - [Windows Setup Guide](docs/WINDOWS.md)
- **macOS 10.10+** - Intel or Apple Silicon
- **Linux** - Ubuntu 18.04+ / Debian 10+
- MetaMask or Web3-compatible wallet browser extension

### For Android
- Android 8.0 (Oreo) or higher
- MetaMask Mobile, Trust Wallet, or TokenPocket
- Optional: **Magisk v30.7** for rooted device usage — [Android Guide](docs/ANDROID.md)

## 🔧 Installation

### 🇧🇩 Bengali PC Installation (বাংলায় PC ইনস্টলেশন)

**"ati pc te ki vabe install korbo" জানতে চান?**

সম্পূর্ণ বাংলা গাইড দেখুন: **[PC_INSTALL_BENGALI.md](PC_INSTALL_BENGALI.md)**

এই গাইডে আছে:
- Windows, macOS, Linux সব OS এর জন্য ধাপে ধাপে নির্দেশনা
- Installer এবং Portable সংস্করণ
- MetaMask সেটআপ (বাংলায়)
- সমস্যা সমাধান (Troubleshooting)

---

### Quick Installation (English)

1. Clone the repository:
```bash
git clone https://github.com/PierPaolo19/llo.git
cd llo
```

2. Install dependencies:
```bash
npm install
```

## 🏗️ Architecture

The project consists of three main contracts:

### 1. FlashUSDT.sol
The main flash loan provider contract that:
- Manages USDT liquidity pool
- Executes flash loans
- Charges fees (default 0.09%)
- Allows deposits and withdrawals

### 2. IFlashLoanReceiver.sol
Interface that borrowers must implement to receive flash loans:
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

### 3. FlashLoanExample.sol
Example implementation showing how to:
- Borrow USDT via flash loan
- Execute custom logic
- Repay the loan with fees

## 📖 Usage

### Desktop Application (ati ki vabe desktop use korbo)

**Launch the desktop application for a user-friendly interface:**

```bash
npm run desktop
```

The desktop app provides:
- 🔗 Wallet connection (MetaMask/Web3)
- ⚡ Flash loan execution interface
- 💧 Liquidity management
- 📊 Real-time contract data
- 📜 Transaction history
- 🌐 Multi-network support (ETH, BSC, Polygon)
- 🔄 Easy network switching

**For detailed desktop usage instructions, see [Desktop Documentation](docs/DESKTOP.md)**

**For Windows 10 Pro users, see [Windows Setup Guide](docs/WINDOWS.md)**

### Desktop Application Installation

#### Windows 10 Pro
```powershell
# Quick setup (PowerShell)
.\scripts\setup-windows.ps1

# Or use batch script
.\scripts\setup-windows.bat

# Run application
npm run desktop
```

See [Windows 10 Pro Guide](docs/WINDOWS.md) for detailed installation instructions, including:
- NSIS installer setup
- Portable version usage
- Windows Defender configuration
- Troubleshooting

#### macOS / Linux
```bash
npm install
npm run desktop
```

### Deploy to Different Networks

The project supports deployment to multiple blockchain networks:

#### Ethereum & EVM-Compatible Chains

```bash
# Deploy to Ethereum Mainnet
npx hardhat run scripts/deploy.js --network mainnet

# Deploy to Sepolia Testnet
npx hardhat run scripts/deploy.js --network sepolia

# Deploy to BSC Mainnet
npx hardhat run scripts/deploy.js --network bsc

# Deploy to BSC Testnet
npx hardhat run scripts/deploy.js --network bscTestnet

# Deploy to Polygon Mainnet
npx hardhat run scripts/deploy.js --network polygon

# Deploy to Mumbai Testnet
npx hardhat run scripts/deploy.js --network mumbai
```

#### Configuration

Create a `.env` file with your private key:

```bash
PRIVATE_KEY=your_private_key_without_0x_prefix
```

#### Tron (TRC20)

Tron requires different tooling. See the [Tron Deployment Guide](docs/TRON.md) for detailed instructions.

**For complete network information, see [Network Documentation](docs/NETWORKS.md)**

### Compile Contracts

```bash
npm run compile
```

### Run Tests

```bash
npm run test
```

### Deploy Contracts

Deploy to local Hardhat network:
```bash
npm run node  # In one terminal
npm run deploy  # In another terminal
```

### Using Flash Loans

#### 1. Implement IFlashLoanReceiver

```solidity
contract MyFlashLoanStrategy is IFlashLoanReceiver {
    function executeOperation(
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        // Your custom logic here
        // Example: arbitrage, liquidation, collateral swap
        
        // Calculate total debt
        uint256 totalDebt = amount + fee;
        
        // Repay the loan
        IERC20(usdt).transfer(msg.sender, totalDebt);
        
        return true;
    }
}
```

#### 2. Execute Flash Loan

```solidity
// Get flash loan contract
IFlashUSDT flashUSDT = IFlashUSDT(flashUSDTAddress);

// Execute flash loan
flashUSDT.flashLoan(
    receiverAddress,  // Your contract implementing IFlashLoanReceiver
    loanAmount,       // Amount to borrow (in USDT wei)
    params           // Additional parameters as bytes
);
```

## 💡 Use Cases

Flash loans are commonly used for:

1. **Arbitrage**: Exploit price differences across DEXs
2. **Collateral Swaps**: Change collateral without closing positions
3. **Liquidations**: Liquidate under-collateralized positions
4. **Debt Refinancing**: Move debt between protocols
5. **Self-liquidation**: Prevent liquidation penalties

## 🔒 Security Considerations

1. **Reentrancy Protection**: Uses OpenZeppelin's ReentrancyGuard
2. **Access Control**: Owner-only functions for sensitive operations
3. **Input Validation**: Comprehensive checks on all parameters
4. **Fee Limits**: Maximum fee capped at 1%
5. **Balance Verification**: Ensures loans are repaid before transaction ends

### Security Best Practices

- Always test on testnets first
- Verify contract addresses
- Use timelock contracts for admin functions
- Consider multi-sig wallets for contract ownership
- Monitor for suspicious activity
- Implement circuit breakers for emergency stops
- Get professional audits before mainnet deployment

## 📊 Contract Parameters

| Parameter | Default Value | Description |
|-----------|--------------|-------------|
| Flash Loan Fee | 9 basis points (0.09%) | Fee charged per flash loan |
| Max Fee | 100 basis points (1%) | Maximum allowed fee |
| Fee Precision | 10,000 | Precision for fee calculations |

## 🧪 Testing

The test suite covers:

- Contract deployment
- Deposit and withdrawal functionality
- Fee calculations and updates
- Flash loan execution
- Error handling
- Access control

Run tests with coverage:
```bash
npm test
```

## 📚 Examples

See `contracts/FlashLoanExample.sol` for a complete working example.

### Quick Example

```solidity
// 1. Deploy your strategy contract
MyStrategy strategy = new MyStrategy();

// 2. Fund it with enough USDT to cover fees
usdt.transfer(address(strategy), feeAmount);

// 3. Execute flash loan
flashUSDT.flashLoan(
    address(strategy),
    1000000 * 10**6,  // Borrow 1M USDT
    ""  // No additional params
);
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📦 Releases

### Latest Release

Check out the [latest release](https://github.com/PierPaolo19/llo/releases/latest) for:
- Pre-built desktop applications (Windows, macOS, Linux)
- Release notes and changelog
- Source code snapshots

### Creating Releases

**Want to create a release?** See our comprehensive guides:

- [📖 Releases Guide (English)](docs/RELEASES.md) - Complete guide for creating releases
- [📖 Releases Guide (বাংলা/Bengali)](docs/RELEASES_BENGALI.md) - **"git Releases kivabe korbo"** - সম্পূর্ণ উত্তর
- [📋 CHANGELOG.md](CHANGELOG.md) - Version history and changes

**Quick release commands:**

```bash
# Create a patch release (bug fixes)
./scripts/release.sh patch

# Create a minor release (new features)
./scripts/release.sh minor

# Create a major release (breaking changes)
./scripts/release.sh major
```

The release workflow automatically:
- ✅ Builds desktop apps for Windows, macOS, and Linux
- ✅ Creates GitHub release with notes
- ✅ Uploads all binaries
- ✅ Tags the release

## 🔗 Resources

### 🎓 Educational Resources

**Start Here** (New to Flash Loans):
- [📚 Education Hub](docs/EDUCATION.md) - **Complete guide to understanding flash loans**
- [🎯 Tutorial Series](docs/tutorials/TUTORIAL_INDEX.md) - **Step-by-step hands-on tutorials**
  - [Tutorial 1: Flash Loan Basics](docs/tutorials/TUTORIAL_01_BASICS.md)
  - [Tutorial 2: Your First Flash Loan](docs/tutorials/TUTORIAL_02_FIRST_LOAN.md)
  - [Tutorial 3: Arbitrage Strategies](docs/tutorials/TUTORIAL_03_ARBITRAGE.md)
  - [Tutorial 4: Security Best Practices](docs/tutorials/TUTORIAL_04_SECURITY.md)
- [💡 Use Cases](docs/USE_CASES.md) - **Real-world applications with examples**
- [❓ FAQ](docs/FAQ.md) - **Frequently Asked Questions**

### Documentation

**Bengali (বাংলা) Guides:**
- [PC Installation Guide (বাংলা)](PC_INSTALL_BENGALI.md) - **"ati pc te ki vabe install korbo"** - সম্পূর্ণ উত্তর
- [Releases Guide (বাংলা)](docs/RELEASES_BENGALI.md) - **"git Releases kivabe korbo"** - সম্পূর্ণ উত্তর
- [Desktop Quick Start (বাংলা)](DESKTOP_QUICKSTART.md) - দ্রুত শুরু করার গাইড
- [Desktop Usage (বাংলা)](docs/DESKTOP_BENGALI.md) - ব্যবহার নির্দেশিকা

**English Guides:**
- [Network Guide](docs/NETWORKS.md) - Multi-chain support (ERC20, BEP20, TRC20)
- [Tron Deployment](docs/TRON.md) - TRC20 deployment instructions
- [Desktop Application Guide](docs/DESKTOP.md) - How to use the desktop app
- [Windows 10 Pro Guide](docs/WINDOWS.md) - Windows installation and troubleshooting
- [Android Guide](docs/ANDROID.md) - Android usage with MetaMask Mobile & Magisk v30.7
- [Releases Guide](docs/RELEASES.md) - **How to create GitHub releases**
- [Getting Started](docs/GETTING_STARTED.md) - Complete setup guide
- [Technical Documentation](docs/TECHNICAL.md) - Technical specifications

### External Resources
- [Hardhat Documentation](https://hardhat.org/docs)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts)
- [Solidity Documentation](https://docs.soliditylang.org)
- [Flash Loans Explained](https://www.aave.com/flash-loans)

### Network-Specific
- [Ethereum](https://ethereum.org/developers)
- [Binance Smart Chain](https://docs.bnbchain.org)
- [Polygon](https://docs.polygon.technology)
- [Tron](https://developers.tron.network)

## ⚡ Flash Loan Flow

```
┌─────────────┐
│   Borrower  │
└──────┬──────┘
       │ 1. Request Flash Loan
       ▼
┌─────────────────┐
│   FlashUSDT     │
│   (Lender)      │
└────────┬────────┘
         │ 2. Transfer USDT
         ▼
┌─────────────────┐
│  Your Contract  │
│  (Receiver)     │
└────────┬────────┘
         │ 3. Execute Strategy
         │    (Arbitrage, etc.)
         │
         │ 4. Repay Loan + Fee
         ▼
┌─────────────────┐
│   FlashUSDT     │
│   (Verified)    │
└─────────────────┘
```

## 🎯 Roadmap

- [x] Core flash loan functionality
- [x] Comprehensive test suite
- [x] Example implementations
- [ ] Multi-token support (USDC, DAI, etc.)
- [ ] Flash loan aggregator
- [ ] Advanced examples (arbitrage, liquidation)
- [ ] Frontend interface
- [ ] Mainnet deployment scripts
- [ ] Professional security audit
- [ ] Gas optimization improvements

## 💬 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Submit a pull request
- Star the repository if you find it useful!

## 📝 Changelog

### Version 1.0.0
- Initial release
- Core flash loan functionality
- USDT support
- Example implementations
- Test suite

---

**Remember**: With great power comes great responsibility. Use flash loans ethically and legally.