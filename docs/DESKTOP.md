# Flash USDT Desktop Application

## Overview

The Flash USDT Desktop Application provides a user-friendly graphical interface for interacting with Flash USDT smart contracts. Built with Electron and ethers.js, it allows users to execute flash loans, manage liquidity, and monitor transactions directly from their desktop.

## Features

- 🔗 **Wallet Integration**: Connect MetaMask or any Web3-compatible wallet
- ⚡ **Flash Loan Execution**: Execute flash loans with a simple form interface
- 💧 **Liquidity Management**: Deposit and withdraw USDT from the liquidity pool
- 📊 **Real-time Data**: View available liquidity, fees, and network status
- 📜 **Transaction History**: Track your flash loan transactions
- 🌐 **Multi-Network Support**: Works with Ethereum Mainnet, Sepolia testnet, and local Hardhat networks

## Installation

### From Source

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PierPaolo19/llo.git
   cd llo
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the desktop app:**
   ```bash
   npm run desktop
   ```

### Build Executable

To build standalone executables:

```bash
# Build for your current platform
npm run desktop:build

# Build for all platforms (Windows, macOS, Linux)
npm run desktop:build-all
```

The built applications will be in the `dist/` directory.

## How to Use (ati ki vabe desktop use korbo)

### 1. Launch the Application

- **Windows**: Double-click `Flash USDT.exe`
- **macOS**: Open `Flash USDT.app`
- **Linux**: Run `./Flash USDT.AppImage`

Or from source:
```bash
npm run desktop
```

### 2. Connect Your Wallet

1. Click the **"Connect Wallet"** button in the top right
2. MetaMask (or your Web3 wallet) will prompt for permission
3. Approve the connection
4. Your wallet address will appear in the header

### 3. Check Network Status

The Network Status card shows:
- Current network (Ethereum Mainnet, Sepolia, etc.)
- Flash USDT contract address
- Available liquidity in the pool
- Current flash loan fee percentage

### 4. Execute a Flash Loan

1. **Enter Receiver Contract Address**: 
   - This must be a contract you've deployed that implements `IFlashLoanReceiver`
   - Example: `0x1234567890123456789012345678901234567890`

2. **Enter Loan Amount**: 
   - Amount of USDT to borrow
   - Example: `1000` for 1000 USDT
   
3. **View Estimated Fee**: 
   - Automatically calculated based on amount
   - Default is 0.09% of loan amount

4. **Add Custom Parameters (Optional)**:
   - Hex-encoded data to pass to your receiver contract
   - Leave as `0x` if not needed

5. **Click "Execute Flash Loan"**:
   - Approve the transaction in MetaMask
   - Wait for confirmation
   - Transaction will appear in history

### 5. Provide Liquidity

**To earn fees from flash loans:**

1. Scroll to **"Liquidity Management"** section
2. Under **"Provide Liquidity"**:
   - Enter amount of USDT to deposit
   - Click **"Deposit"**
   - Approve USDT spending (first time only)
   - Confirm deposit transaction

**Your USDT will earn fees from flash loans!**

### 6. Withdraw Liquidity (Owner Only)

If you're the contract owner:

1. Under **"Withdraw Liquidity"**:
   - Enter amount to withdraw
   - Click **"Withdraw"**
   - Confirm transaction

### 7. View Transaction History

All your flash loan transactions appear in the **"Recent Transactions"** section:
- Transaction type and details
- Transaction hash
- Block number
- Gas used

## Prerequisites

- **Web3 Wallet**: MetaMask or compatible wallet installed
- **Network**: Connect to Ethereum Mainnet, Sepolia testnet, or local network
- **USDT**: For deposits and flash loan fees
- **ETH**: For gas fees

## Configuration

### Contract Addresses

Update contract addresses in `desktop/src/app.js`:

```javascript
const CONTRACT_ADDRESSES = {
    1: { // Mainnet
        flashUSDT: 'YOUR_MAINNET_CONTRACT_ADDRESS',
        usdt: '0xdac17f958d2ee523a2206206994597c13d831ec7'
    },
    11155111: { // Sepolia
        flashUSDT: 'YOUR_SEPOLIA_CONTRACT_ADDRESS',
        usdt: 'YOUR_USDT_ADDRESS'
    }
};
```

### Custom Networks

To add support for other networks, update the `CONTRACT_ADDRESSES` object with the chain ID and contract addresses.

## Troubleshooting

### "Please install MetaMask"
- Install MetaMask browser extension
- Or use another Web3-compatible wallet

### "Contract not deployed on this network"
- Switch to a supported network in MetaMask
- Or update contract addresses in configuration

### "Transaction failed"
- Check you have enough ETH for gas
- Ensure receiver contract is correct
- Verify sufficient liquidity in pool

### "Withdrawal failed"
- Only contract owner can withdraw
- Ensure you're connected with owner wallet

## Keyboard Shortcuts

- `Ctrl+R` / `Cmd+R`: Reload app
- `Ctrl+Shift+I` / `Cmd+Opt+I`: Open DevTools (development mode)
- `Ctrl+Q` / `Cmd+Q`: Quit application

## Security Notes

- ⚠️ The desktop app connects to your Web3 wallet
- ⚠️ Always verify transaction details before approving
- ⚠️ Only use with audited smart contracts
- ⚠️ Keep your wallet seed phrase secure
- ⚠️ Test on testnets before using real funds

## Development

### Running in Development Mode

```bash
# Set development mode
export NODE_ENV=development

# Run with DevTools open
npm run desktop
```

### Project Structure

```
desktop/
├── main.js              # Electron main process
├── src/
│   ├── index.html       # UI structure
│   ├── styles.css       # Styling
│   └── app.js          # Application logic
└── assets/
    └── icon.png        # Application icon
```

## Building

### Prerequisites for Building

- **Windows**: Windows 7+ with npm
- **macOS**: macOS 10.10+ with Xcode Command Line Tools
- **Linux**: Ubuntu/Debian with build essentials

### Build Commands

```bash
# Build for current platform only
npm run desktop:build

# Build for all platforms
npm run desktop:build-all

# Outputs will be in dist/ directory
```

## Support

For issues or questions:
- GitHub Issues: https://github.com/PierPaolo19/llo/issues
- Documentation: See `/docs` directory
- Smart Contract Docs: See `docs/TECHNICAL.md`

## License

MIT License - See LICENSE file

## Disclaimer

This desktop application is for educational purposes. It interfaces with smart contracts that have not been professionally audited. Use at your own risk. Always test thoroughly on testnets before using real funds.

---

**Built with ❤️ using Electron & ethers.js**
