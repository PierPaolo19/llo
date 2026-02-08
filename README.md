# Flash USDT Script - Multi-Network Support

A demonstration script for flash loan operations with USDT (Tether USD) across multiple blockchain networks:
- 🔷 **TRC20** (Tron Network)
- ⟠ **ERC20** (Ethereum Network)  
- 🟡 **BEP20** (Binance Smart Chain)

This script simulates the flash loan process including borrowing, executing arbitrage strategies, and repayment on different networks with their specific characteristics.

## What is a Flash Loan?

Flash loans are a type of uncollateralized loan that must be borrowed and repaid within the same blockchain transaction. They are commonly used for:
- Arbitrage opportunities across exchanges
- Collateral swapping
- Self-liquidation
- Other DeFi operations

## Supported Networks

### TRC20 (Tron)
- **Lower Fees**: 0.05% flash loan fee
- **Fast Blocks**: ~3 second block time
- **Low Gas**: Minimal energy/bandwidth costs
- **USDT Contract**: TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t

### ERC20 (Ethereum)
- **Standard Fees**: 0.09% flash loan fee
- **Established**: Most mature flash loan ecosystem
- **Higher Gas**: Typical ETH gas costs
- **USDT Contract**: 0xdac17f958d2ee523a2206206994597c13d831ec7

### BEP20 (Binance Smart Chain)
- **Lower Fees**: 0.05% flash loan fee
- **Fast Blocks**: ~3 second block time
- **Moderate Gas**: BNB gas costs
- **USDT Contract**: 0x55d398326f99059fF775485246999027B3197955

## Features

- 🚀 Simulates flash loan borrowing across multiple networks
- ⚡ Demonstrates arbitrage execution
- 💸 Network-specific fee calculations
- ✅ Validates transaction success/failure
- 📊 Detailed logging with network information
- 🔄 Network comparison tool

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
1. Compare all three networks (TRC20, ERC20, BEP20)
2. Execute example flash loans on each network
3. Display detailed results and comparisons

## Configuration

You can customize the flash loan parameters and select a specific network:

```javascript
// Example: Flash loan on Tron (TRC20)
const config = {
    network: 'TRC20',     // Options: 'TRC20', 'ERC20', 'BEP20'
    loanAmount: 50000,    // Amount to borrow in USDT
    fee: 0.05,            // Fee percentage (network default if not specified)
    profitTarget: 100     // Minimum target profit in USDT
};

const flashLoan = new FlashUSDTLoan(config);
await flashLoan.execute();
```

### Network Selection Examples

```javascript
// Tron Network (TRC20) - Lowest fees
const tronLoan = new FlashUSDTLoan({ 
    network: 'TRC20', 
    loanAmount: 100000 
});

// Ethereum Network (ERC20) - Most established
const ethLoan = new FlashUSDTLoan({ 
    network: 'ERC20', 
    loanAmount: 100000 
});

// Binance Smart Chain (BEP20) - Fast and affordable
const bscLoan = new FlashUSDTLoan({ 
    network: 'BEP20', 
    loanAmount: 100000 
});
```

### Compare Networks

```javascript
const { compareNetworks } = require('./flash-usdt.js');

// Compare all networks for a specific loan amount
await compareNetworks(50000); // Compare networks for 50K USDT loan
```

## Output Example

The script will display:
- Network comparison showing fees and characteristics for all three networks
- Loan amount and network-specific fees
- Network gas costs and block times
- USDT contract addresses
- Arbitrage execution details
- Repayment status
- Net profit or loss

Example output:
```
╔═══════════════════════════════════════════════════════════╗
║        FLASH LOAN NETWORK COMPARISON                      ║
║        Loan Amount: 50,000 USDT                           ║
╚═══════════════════════════════════════════════════════════╝

🔷 Tron (TRC20)
   Flash Loan Fee: 25.00 USDT (0.05%)
   Gas Fee: ~0.05 TRX
   Block Time: ~3s
   Contract: TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t

⟠ Ethereum (ERC20)
   Flash Loan Fee: 45.00 USDT (0.09%)
   Gas Fee: ~0.15 ETH
   Block Time: ~12s
   Contract: 0xdac17f958d2ee523a2206206994597c13d831ec7

🟡 Binance Smart Chain (BEP20)
   Flash Loan Fee: 25.00 USDT (0.05%)
   Gas Fee: ~0.008 BNB
   Block Time: ~3s
   Contract: 0x55d398326f99059fF775485246999027B3197955

💡 Most Cost-Effective: 🔷 Tron (TRC20)
```

## Important Notes

⚠️ **This is a demonstration/educational script**

In a production environment, you would need:
- **TRC20**: TronWeb library for Tron network interaction
- **ERC20**: Web3.js or Ethers.js for Ethereum network interaction
- **BEP20**: Web3.js or Ethers.js configured for BSC network
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

### Network Considerations

- **Gas Costs**: Ethereum typically has higher gas fees than Tron or BSC
- **Speed**: Tron and BSC have faster block times (~3s) vs Ethereum (~12s)
- **Liquidity**: Ethereum generally has deeper liquidity pools
- **Flash Loan Providers**: Each network has different flash loan protocols available
- **USDT Contracts**: Each network uses a different USDT smart contract address

## License

MIT