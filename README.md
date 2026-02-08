# Flash USDT Script - Multi-Network & Multi-Wallet Support

A demonstration script for flash loan operations with USDT (Tether USD) across multiple blockchain networks and wallet types:

**Networks:**
- 🔷 **TRC20** (Tron Network)
- ⟠ **ERC20** (Ethereum Network)
- 🟡 **BEP20** (Binance Smart Chain)

**Wallets:**
- 🦊 **MetaMask** - Most popular Ethereum wallet
- 🛡️ **Trust Wallet** - Multi-chain mobile wallet
- 🟡 **Binance Wallet** - Integrated exchange wallet
- 🌐 **Web3 Wallet** - Generic Web3 interface

This script simulates the flash loan process including wallet connection, borrowing, executing arbitrage strategies, and repayment on different networks with various wallet types.

## What is a Flash Loan?

Flash loans are a type of uncollateralized loan that must be borrowed and repaid within the same blockchain transaction. They are commonly used for:
- Arbitrage opportunities across exchanges
- Collateral swapping
- Self-liquidation
- Other DeFi operations

## Supported Wallets

### 🦊 MetaMask
- **Type**: Browser Extension / Mobile App
- **Networks**: Ethereum (ERC20), BSC (BEP20)
- **Best For**: DeFi applications, NFTs, token swaps
- **Features**: DApp browser, hardware wallet integration, extensive DeFi support
- **Website**: https://metamask.io

### 🛡️ Trust Wallet
- **Type**: Mobile Wallet
- **Networks**: Tron (TRC20), Ethereum (ERC20), BSC (BEP20)
- **Best For**: Multi-chain asset management, mobile users
- **Features**: Multi-chain support, DApp browser, staking, NFT gallery
- **Website**: https://trustwallet.com

### 🟡 Binance Wallet
- **Type**: Exchange-Integrated Wallet
- **Networks**: Tron (TRC20), Ethereum (ERC20), BSC (BEP20)
- **Best For**: Trading, low fees, exchange integration
- **Features**: Instant trading, savings products, low transaction fees
- **Website**: https://www.binance.com

### 🌐 Web3 Wallet
- **Type**: Generic Web3 Interface
- **Networks**: All supported (TRC20, ERC20, BEP20)
- **Best For**: Developers, custom integrations
- **Features**: Smart contract interaction, multiple providers, custom networks
- **Website**: https://web3js.org

## Supported Networks

### TRC20 (Tron)
- **Lower Fees**: 0.05% flash loan fee
- **Fast Blocks**: ~3 second block time
- **Low Gas**: Minimal energy/bandwidth costs
- **USDT Contract**: TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
- **Compatible Wallets**: Trust Wallet, Binance Wallet, Web3

### ERC20 (Ethereum)
- **Standard Fees**: 0.09% flash loan fee
- **Established**: Most mature flash loan ecosystem
- **Higher Gas**: Typical ETH gas costs
- **USDT Contract**: 0xdac17f958d2ee523a2206206994597c13d831ec7
- **Compatible Wallets**: MetaMask, Trust Wallet, Binance Wallet, Web3

### BEP20 (Binance Smart Chain)
- **Lower Fees**: 0.05% flash loan fee
- **Fast Blocks**: ~3 second block time
- **Moderate Gas**: BNB gas costs
- **USDT Contract**: 0x55d398326f99059fF775485246999027B3197955
- **Compatible Wallets**: MetaMask, Trust Wallet, Binance Wallet, Web3

## Features

- 🚀 Simulates flash loan borrowing across multiple networks
- 👛 Supports multiple wallet types (MetaMask, Trust Wallet, Binance, Web3)
- 🔗 Wallet connection simulation
- ⚡ Demonstrates arbitrage execution
- 💸 Network-specific fee calculations
- ✅ Validates transaction success/failure
- 📊 Detailed logging with network and wallet information
- 🔄 Network and wallet comparison tools
- 🗺️ Wallet-network compatibility matrix

## Installation

1. Clone the repository
2. Ensure you have Node.js (v14 or higher) installed
3. No additional dependencies required (uses vanilla Node.js)

## Usage

Run the script using Node.js:

```bash
node flash-usdt.js
```

Or use npm:

```bash
npm start
```

The script will:
1. Display wallet information and features
2. Show wallet-network compatibility matrix
3. Compare all three networks (TRC20, ERC20, BEP20)
4. Execute example flash loans with different wallet-network combinations

## Configuration

You can customize the flash loan parameters, network, and wallet:

```javascript
// Example: Flash loan with MetaMask on Ethereum
const config = {
    wallet: 'METAMASK',   // Options: 'METAMASK', 'TRUST_WALLET', 'BINANCE', 'WEB3'
    network: 'ERC20',     // Options: 'TRC20', 'ERC20', 'BEP20'
    loanAmount: 50000,    // Amount to borrow in USDT
    fee: 0.09,            // Fee percentage (network default if not specified)
    profitTarget: 100     // Minimum target profit in USDT
};

const flashLoan = new FlashUSDTLoan(config);
await flashLoan.execute();
```

### Wallet Selection Examples

```javascript
// MetaMask on Ethereum - Best for DeFi
const metamaskEth = new FlashUSDTLoan({ 
    wallet: 'METAMASK',
    network: 'ERC20', 
    loanAmount: 100000 
});

// Trust Wallet on BSC - Multi-chain mobile
const trustBsc = new FlashUSDTLoan({ 
    wallet: 'TRUST_WALLET',
    network: 'BEP20', 
    loanAmount: 100000 
});

// Binance Wallet on Tron - Low fees
const binanceTron = new FlashUSDTLoan({ 
    wallet: 'BINANCE',
    network: 'TRC20', 
    loanAmount: 100000 
});

// Web3 on any network - Developer friendly
const web3Bsc = new FlashUSDTLoan({ 
    wallet: 'WEB3',
    network: 'BEP20', 
    loanAmount: 100000 
});
```

### Compare Wallets

```javascript
const { compareWallets, displayCompatibilityMatrix } = require('./flash-usdt.js');

// Compare all wallet features
await compareWallets();

// Show wallet-network compatibility
displayCompatibilityMatrix();
```

### Compare Networks

```javascript
const { compareNetworks } = require('./flash-usdt.js');

// Compare all networks for a specific loan amount
await compareNetworks(50000); // Compare networks for 50K USDT loan
```

## Output Example

The script will display:
- Wallet information and features for all supported wallets
- Wallet-network compatibility matrix
- Network comparison showing fees and characteristics
- Wallet connection status with address
- Loan amount and network-specific fees
- Network gas costs and block times
- USDT contract addresses
- Arbitrage execution details
- Repayment status
- Net profit or loss

Example output:
```
╔═══════════════════════════════════════════════════════════╗
║              WALLET COMPARISON                             ║
╚═══════════════════════════════════════════════════════════╝

🦊 MetaMask
   Type: browser-extension
   Networks: ⟠ ERC20, 🟡 BEP20
   Features:
      • DApp Browser
      • Token Swaps
      • NFT Support
      • Hardware Wallet Integration
   Website: https://metamask.io
   Mobile: ✅  Desktop: ✅

... (other wallets)

╔═══════════════════════════════════════════════════════════╗
║        WALLET-NETWORK COMPATIBILITY MATRIX                 ║
╚═══════════════════════════════════════════════════════════╝

Wallet              │ TRC20  │ ERC20  │ BEP20  │
────────────────────┼────────┼────────┼────────┤
🦊 MetaMask         │   ❌   │   ✅   │   ✅   │
🛡️ Trust Wallet     │   ✅   │   ✅   │   ✅   │
🟡 Binance Wallet   │   ✅   │   ✅   │   ✅   │
🌐 Web3 Wallet      │   ✅   │   ✅   │   ✅   │
────────────────────┴────────┴────────┴────────┘

═══════════════════════════════════════
    FLASH USDT LOAN EXECUTION
    Network: ⟠ Ethereum (ERC20)
    Wallet: 🦊 MetaMask
═══════════════════════════════════════

🔗 Connecting to 🦊 MetaMask...
   Wallet Type: browser-extension
   Address: 0xffffffffffffffffffffffffffffffffffffffffffff
   Network: ⟠ Ethereum (ERC20)
   ✅ Wallet Connected Successfully!

🚀 Initiating Flash Loan on ⟠ Ethereum (ERC20)...
   Via 🦊 MetaMask
📊 Loan Amount: 50000 USDT
💰 Fee: 45 USDT (0.09%)
⛽ Network Gas Fee: ~0.15 ETH
💳 Total Repayment Required: 50045 USDT
📍 USDT Contract: 0xdac17f958d2ee523a2206206994597c13d831ec7
👛 Wallet Address: 0xffffffffffffffffffffffffffffffffffffffffffff
```

## Important Notes

⚠️ **This is a demonstration/educational script**

In a production environment, you would need:
- **Wallet Integration Libraries**:
  - MetaMask: @metamask/sdk or window.ethereum API
  - Trust Wallet: WalletConnect protocol
  - Binance Wallet: Binance Chain SDK
  - Web3: web3.js or ethers.js
- **Network Connections**:
  - TRC20: TronWeb library for Tron network interaction
  - ERC20: Web3.js or Ethers.js for Ethereum network interaction
  - BEP20: Web3.js or Ethers.js configured for BSC network
- Connection to respective network RPC endpoints
- Integration with actual flash loan providers:
  - Ethereum: Aave, dYdX, Uniswap V3
  - BSC: PancakeSwap, Venus Protocol
  - Tron: JustLend
- Proper smart contract interfaces and ABIs
- Gas management and transaction handling for each network
- Real arbitrage strategies accounting for network differences
- Security audits
- Private key management and wallet integration
- User authentication and authorization

### Wallet-Network Considerations

- **MetaMask**: Native support for Ethereum and BSC, requires network switching
- **Trust Wallet**: Built-in multi-chain support, mobile-first experience
- **Binance Wallet**: Deep exchange integration, ideal for trading workflows
- **Web3 Wallet**: Framework-agnostic, requires manual provider configuration
- **Gas Costs**: Vary significantly by network (Ethereum > BSC > Tron)
- **Speed**: Tron and BSC have faster block times (~3s) vs Ethereum (~12s)
- **Liquidity**: Ethereum generally has deeper liquidity pools
- **Flash Loan Providers**: Each network has different flash loan protocols available
- **USDT Contracts**: Each network uses a different USDT smart contract address

### Wallet Selection Guide

Choose your wallet based on:
1. **Primary Network**: 
   - Ethereum-focused? → MetaMask
   - Multi-chain? → Trust Wallet or Binance Wallet
   - Tron-focused? → Trust Wallet or Binance Wallet
2. **Use Case**:
   - DeFi interactions? → MetaMask or Trust Wallet
   - Trading? → Binance Wallet
   - Development? → Web3 Wallet
3. **Platform**:
   - Desktop only? → MetaMask or Web3
   - Mobile preferred? → Trust Wallet
   - Exchange user? → Binance Wallet

## License

MIT