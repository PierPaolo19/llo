# Tron (TRC20) Deployment Guide

This guide explains how to deploy Flash USDT to the Tron network, which uses TRC20 tokens instead of ERC20.

## Important Differences

Tron is **not EVM-compatible** and requires different tools:

| Aspect | Ethereum/BSC/Polygon | Tron |
|--------|---------------------|------|
| VM | EVM | TVM (Tron Virtual Machine) |
| Language | Solidity (EVM) | Solidity (TVM) |
| Tools | Hardhat, Truffle | TronBox, TronWeb |
| Addresses | 0x... (42 chars) | T... (34 chars) |
| Gas | ETH/BNB/MATIC | TRX (Energy/Bandwidth) |

## Prerequisites

1. **TronLink Wallet**: https://www.tronlink.org
2. **TRX** for fees (very low, ~0.1-1 TRX)
3. **Node.js** v14+
4. **TronBox** (like Hardhat for Tron)

## Installation

### 1. Install TronBox

```bash
npm install -g tronbox
```

### 2. Install TronWeb

```bash
npm install tronweb --save
```

## Tron Network Configuration

### Mainnet

```javascript
const TronWeb = require('tronweb');

const tronWeb = new TronWeb({
    fullHost: 'https://api.trongrid.io',
    headers: { "TRON-PRO-API-KEY": 'your-api-key' },
    privateKey: 'your-private-key'
});
```

### Shasta Testnet

```javascript
const tronWeb = new TronWeb({
    fullHost: 'https://api.shasta.trongrid.io',
    privateKey: 'your-private-key'
});
```

## Smart Contract Modifications

The contracts need minor modifications for Tron:

### 1. Address Format

Tron addresses start with 'T' instead of '0x':

```solidity
// Ethereum: 0xdac17f958d2ee523a2206206994597c13d831ec7
// Tron: TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
```

### 2. USDT on Tron

```javascript
const USDT_TRC20 = 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t';
```

### 3. Compatible Solidity Version

Tron supports Solidity 0.8.x, so our contracts should work:

```solidity
pragma solidity ^0.8.20;
```

## TronBox Configuration

Create `tronbox.js`:

```javascript
module.exports = {
  networks: {
    mainnet: {
      privateKey: process.env.PRIVATE_KEY_MAINNET,
      userFeePercentage: 100,
      feeLimit: 1000 * 1e6,
      fullHost: 'https://api.trongrid.io',
      network_id: '1'
    },
    shasta: {
      privateKey: process.env.PRIVATE_KEY_SHASTA,
      userFeePercentage: 100,
      feeLimit: 1000 * 1e6,
      fullHost: 'https://api.shasta.trongrid.io',
      network_id: '2'
    },
    development: {
      privateKey: 'your-dev-private-key',
      userFeePercentage: 0,
      feeLimit: 1000 * 1e6,
      fullHost: 'http://127.0.0.1:9090',
      network_id: '9'
    }
  },
  solc: {
    version: '0.8.20'
  }
};
```

## Deployment Process

### 1. Prepare Contracts

Copy contracts to TronBox project:

```bash
mkdir tron-deployment
cd tron-deployment
tronbox init
cp ../contracts/*.sol contracts/
```

### 2. Compile

```bash
tronbox compile
```

### 3. Create Migration Script

Create `migrations/2_deploy_contracts.js`:

```javascript
const FlashUSDT = artifacts.require("FlashUSDT");
const MockUSDT = artifacts.require("MockUSDT");

module.exports = function(deployer, network) {
  // USDT address on Tron mainnet
  const USDT_MAINNET = 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t';
  
  if (network === 'mainnet') {
    // Deploy to mainnet with real USDT
    deployer.deploy(FlashUSDT, USDT_MAINNET);
  } else {
    // Deploy mock USDT for testnet
    deployer.deploy(MockUSDT).then(function() {
      return deployer.deploy(FlashUSDT, MockUSDT.address);
    });
  }
};
```

### 4. Deploy to Shasta Testnet

```bash
tronbox migrate --network shasta
```

### 5. Deploy to Mainnet

```bash
tronbox migrate --network mainnet
```

## Verification

### On TronScan

1. Go to https://tronscan.org (mainnet) or https://shasta.tronscan.org (testnet)
2. Search for your contract address
3. Click "Contract" tab
4. Click "Verify Contract"
5. Upload source code and constructor parameters

## TronWeb Integration

### Desktop App Modifications

The desktop app needs TronWeb instead of ethers.js for Tron:

```javascript
// Add to desktop/src/app.js for Tron support

async function connectTronWallet() {
    if (typeof window.tronWeb === 'undefined') {
        alert('Please install TronLink wallet!');
        return;
    }
    
    try {
        const tronWeb = window.tronWeb;
        
        if (!tronWeb.ready) {
            alert('Please unlock TronLink');
            return;
        }
        
        const address = tronWeb.defaultAddress.base58;
        console.log('Connected to Tron address:', address);
        
        // Initialize contract
        const flashUSDTAddress = 'YOUR_DEPLOYED_CONTRACT_ADDRESS';
        const contract = await tronWeb.contract().at(flashUSDTAddress);
        
        return { address, contract };
    } catch (error) {
        console.error('Tron connection error:', error);
        throw error;
    }
}

// Flash loan on Tron
async function executeTronFlashLoan(receiverAddress, amount, params) {
    const tronWeb = window.tronWeb;
    const contract = await tronWeb.contract().at(flashUSDTAddress);
    
    try {
        const result = await contract.flashLoan(
            receiverAddress,
            amount,
            params
        ).send({
            feeLimit: 1000_000_000, // 1000 TRX
            callValue: 0
        });
        
        return result;
    } catch (error) {
        console.error('Tron flash loan error:', error);
        throw error;
    }
}
```

## Gas/Energy Considerations

### Tron Fee Model

Tron uses **Energy** and **Bandwidth** instead of traditional gas:

- **Bandwidth**: Free daily allowance for simple transfers
- **Energy**: Required for smart contract calls
- **Fee Limit**: Maximum TRX you're willing to spend

### Estimating Costs

```javascript
// Get energy estimate
const transaction = await contract.flashLoan(...).send({
    feeLimit: 1000_000_000,
    shouldPollResponse: false
});

console.log('Energy used:', transaction.receipt.energy_usage_total);
console.log('Fee paid (SUN):', transaction.receipt.energy_fee);
```

### Cost Optimization

1. **Stake TRX**: Get free energy (1 TRX = ~300 energy/day)
2. **Energy Rental**: Rent energy for cheaper fees
3. **Optimize Code**: Minimize storage operations

## Testing on Shasta

### 1. Get Test TRX

Faucet: https://www.trongrid.io/shasta

### 2. Get Test USDT

Deploy MockUSDT or use existing test tokens

### 3. Test Flash Loans

```javascript
const tronWeb = new TronWeb({
    fullHost: 'https://api.shasta.trongrid.io',
    privateKey: 'your-private-key'
});

const flashUSDT = await tronWeb.contract().at('YOUR_CONTRACT');
const result = await flashUSDT.flashLoan(
    receiverAddress,
    tronWeb.toSun(1000), // 1000 USDT
    '0x'
).send();

console.log('Transaction:', result);
```

## Differences from EVM

### 1. Address Conversion

```javascript
// Hex to Base58
const base58 = tronWeb.address.fromHex('41...');

// Base58 to Hex
const hex = tronWeb.address.toHex('T...');
```

### 2. Event Handling

```javascript
// Get events
const events = await contract.FlashLoan().watch((err, event) => {
    if (err) return console.error(err);
    console.log('Event:', event);
});
```

### 3. Transaction Confirmation

```javascript
// Wait for confirmation
const tx = await contract.method(...).send();
const confirmed = await tronWeb.trx.getTransaction(tx);
```

## Troubleshooting

### "Out of Energy"
- Stake more TRX for energy
- Rent energy: https://www.tronscan.org/#/energy
- Increase feeLimit

### "Transaction Reverted"
- Check contract logic
- Verify USDT approval
- Ensure sufficient balance

### "Invalid Address"
- Use Base58 format (starts with 'T')
- Convert from hex if needed
- Verify on TronScan

### "Contract Not Found"
- Verify deployment succeeded
- Check network (mainnet vs shasta)
- Wait for block confirmation

## Resources

### Official Documentation
- TronWeb: https://developers.tron.network/docs/tronweb
- TronBox: https://developers.tron.network/docs/tronbox
- TronGrid API: https://www.trongrid.io

### Tools
- TronScan: https://tronscan.org
- TronLink: https://www.tronlink.org
- Shasta Faucet: https://www.trongrid.io/shasta

### Community
- Tron Discord: https://discord.gg/tron
- Developer Forum: https://forum.tron.network
- GitHub: https://github.com/tronprotocol

## Example: Complete Tron Deployment

```bash
# 1. Setup
mkdir tron-flash-usdt
cd tron-flash-usdt
tronbox init
npm install tronweb

# 2. Copy contracts
cp ../contracts/FlashUSDT.sol contracts/
cp ../contracts/IFlashLoanReceiver.sol contracts/
cp ../contracts/MockUSDT.sol contracts/

# 3. Configure tronbox.js
# (see configuration above)

# 4. Compile
tronbox compile

# 5. Deploy to Shasta
tronbox migrate --network shasta

# 6. Test
tronbox console --network shasta
> let instance = await FlashUSDT.deployed()
> let liquidity = await instance.availableLiquidity()
> console.log(liquidity.toString())

# 7. Deploy to Mainnet (when ready)
tronbox migrate --network mainnet
```

## Security Notes

- ⚠️ Test thoroughly on Shasta before mainnet
- ⚠️ Verify all addresses are in Base58 format
- ⚠️ Start with small amounts
- ⚠️ Monitor energy costs
- ⚠️ Get contract audited before production use

## Conclusion

While Tron requires different tooling, the core Flash USDT logic remains the same. The main differences are:
1. Use TronBox instead of Hardhat
2. Use TronWeb instead of ethers.js
3. Handle Base58 addresses instead of hex
4. Manage Energy instead of gas

For most users, we recommend starting with Ethereum/BSC/Polygon (ERC20/BEP20) as they're easier to work with using the existing desktop application.

---

**Note**: Full Tron integration in the desktop app is planned for a future release. Current desktop app supports ERC20/BEP20 networks only.
