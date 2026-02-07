# Flash USDT 💸

An open-source flash loan implementation for USDT (Tether) on Ethereum and EVM-compatible blockchains.

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
- **Flexible**: Easy to integrate into your DeFi strategies
- **Gas optimized**: Built with efficiency in mind
- **Well-tested**: Comprehensive test suite included
- **Desktop Application**: User-friendly GUI for managing flash loans (ati ki vabe desktop use korbo)

## 📋 Prerequisites

- Node.js (v18 or higher)
- npm or yarn
- Hardhat

## 🔧 Installation

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
- 🔗 Wallet connection (MetaMask)
- ⚡ Flash loan execution interface
- 💧 Liquidity management
- 📊 Real-time contract data
- 📜 Transaction history

**For detailed desktop usage instructions, see [Desktop Documentation](docs/DESKTOP.md)**

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

## 🔗 Resources

- [Hardhat Documentation](https://hardhat.org/docs)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts)
- [Solidity Documentation](https://docs.soliditylang.org)
- [Flash Loans Explained](https://www.aave.com/flash-loans)
- [Desktop Application Guide](docs/DESKTOP.md) - How to use the desktop app (ati ki vabe desktop use korbo)

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