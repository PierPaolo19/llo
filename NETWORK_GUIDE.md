# Multi-Network Deployment Guide

## Supported Networks

Flash USDT supports deployment on multiple blockchain networks with their respective token standards:

| Network | Token Standard | Mainnet Chain ID | Testnet Chain ID | Status |
|---------|---------------|------------------|------------------|---------|
| **Ethereum** | ERC20 | 1 | 11155111 (Sepolia) | ✅ Supported |
| **Binance Smart Chain** | BEP20 | 56 | 97 | ✅ Supported |
| **Polygon** | ERC20 | 137 | 80001 (Mumbai) | ✅ Supported |
| **TRON** | TRC20 | - | - | 📝 Documentation |

## Network Details

### Ethereum (ERC20)

**Mainnet:**
- Chain ID: 1
- RPC URL: https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY
- Block Explorer: https://etherscan.io
- Native Token: ETH

**Testnets:**
- Sepolia (Chain ID: 11155111)
- Goerli (Chain ID: 5) - Being deprecated

**Token Standard:** ERC20
- Most widely used token standard
- Full compatibility with OpenZeppelin ERC20 contracts
- Used by USDT, USDC, DAI, and thousands of other tokens

### Binance Smart Chain (BEP20)

**Mainnet:**
- Chain ID: 56
- RPC URL: https://bsc-dataseed1.binance.org
- Block Explorer: https://bscscan.com
- Native Token: BNB

**Testnet:**
- Chain ID: 97
- RPC URL: https://data-seed-prebsc-1-s1.binance.org:8545
- Block Explorer: https://testnet.bscscan.com
- Testnet BNB Faucet: https://testnet.binance.org/faucet-smart

**Token Standard:** BEP20
- Compatible with ERC20 interface
- Lower gas fees than Ethereum
- Fast block times (~3 seconds)
- Popular tokens: USDT (BEP20), BUSD, CAKE

**Important Notes:**
- BEP20 is fully ERC20-compatible
- Same smart contract code works on BSC
- Different RPC endpoints and chain IDs

### Polygon (ERC20)

**Mainnet:**
- Chain ID: 137
- RPC URL: https://polygon-rpc.com
- Block Explorer: https://polygonscan.com
- Native Token: MATIC

**Testnet:**
- Mumbai (Chain ID: 80001)
- RPC URL: https://rpc-mumbai.maticvigil.com
- Block Explorer: https://mumbai.polygonscan.com
- Testnet MATIC Faucet: https://faucet.polygon.technology/

**Token Standard:** ERC20 (Polygon is EVM-compatible)
- Ethereum sidechain with faster and cheaper transactions
- Uses standard ERC20 interface
- Popular for DeFi applications
- Lower gas fees (fractions of a cent)

### TRON (TRC20)

**Mainnet:**
- Network: TRON Mainnet
- Full Node: https://api.trongrid.io
- Block Explorer: https://tronscan.org
- Native Token: TRX

**Testnet:**
- Network: Shasta Testnet
- Full Node: https://api.shasta.trongrid.io
- Block Explorer: https://shasta.tronscan.org
- Testnet TRX Faucet: https://www.trongrid.io/shasta

**Token Standard:** TRC20
- TRON's token standard (similar to ERC20)
- Lower transaction fees
- High throughput
- Popular tokens: USDT (TRC20)

**Important Notes:**
- TRON uses different tooling than EVM chains
- Requires TronBox or TronWeb instead of Hardhat
- Contract syntax is similar but deployment differs
- See [TRON Deployment](#tron-deployment-trc20) section below

---

## Quick Start

### Prerequisites

1. Node.js v16 or higher
2. npm or yarn
3. Private key with funds for gas fees

### Setup

1. Clone the repository:
```bash
git clone https://github.com/PierPaolo19/llo.git
cd llo
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

4. Compile contracts:
```bash
npm run compile
```

---

## Deployment Instructions

### Ethereum Deployment (ERC20)

#### Mainnet Deployment

```bash
# Deploy to Ethereum Mainnet
npm run deploy:mainnet
```

**Requirements:**
- ETH for gas fees (~0.05-0.1 ETH recommended)
- Set `ETHEREUM_MAINNET_RPC_URL` in .env
- Set `PRIVATE_KEY` in .env

#### Testnet Deployment (Sepolia)

```bash
# Deploy to Sepolia Testnet
npm run deploy:sepolia
```

**Getting Testnet ETH:**
- Sepolia Faucet: https://sepoliafaucet.com/
- Alchemy Sepolia Faucet: https://sepoliafaucet.com/

### Binance Smart Chain Deployment (BEP20)

#### BSC Mainnet Deployment

```bash
# Deploy to BSC Mainnet
npm run deploy:bsc
```

**Requirements:**
- BNB for gas fees (~0.01-0.05 BNB recommended)
- Set `BSC_MAINNET_RPC_URL` in .env (or use default)
- Set `PRIVATE_KEY` in .env

**Gas Price:**
- Default: 5 gwei
- Can be adjusted in hardhat.config.js

#### BSC Testnet Deployment

```bash
# Deploy to BSC Testnet
npm run deploy:bscTestnet
```

**Getting Testnet BNB:**
- BSC Testnet Faucet: https://testnet.binance.org/faucet-smart

### Polygon Deployment (ERC20)

#### Polygon Mainnet Deployment

```bash
# Deploy to Polygon Mainnet
npm run deploy:polygon
```

**Requirements:**
- MATIC for gas fees (~0.1-0.5 MATIC recommended)
- Set `POLYGON_MAINNET_RPC_URL` in .env (or use default)
- Set `PRIVATE_KEY` in .env

**Gas Price:**
- Default: 50 gwei
- Can be adjusted based on network conditions

#### Polygon Mumbai Testnet

```bash
# Deploy to Mumbai Testnet
npx hardhat run scripts/deploy.js --network mumbai
```

**Getting Testnet MATIC:**
- Polygon Faucet: https://faucet.polygon.technology/

---

## TRON Deployment (TRC20)

TRON uses a different architecture and requires different tooling.

### Prerequisites for TRON

1. **Install TronBox:**
```bash
npm install -g tronbox
```

2. **Install TronWeb:**
```bash
npm install tronweb
```

### TRON Deployment Steps

#### 1. Convert Contract for TRON

The contracts are EVM-compatible, but TRON has some differences:
- TRON uses `address payable` differently
- Some gas optimizations differ
- Event handling is similar

**Good News:** Our contracts are already compatible! They use standard Solidity and OpenZeppelin contracts that work on TRON.

#### 2. Create tronbox.js Configuration

Create a `tronbox.js` file in the project root:

```javascript
module.exports = {
  networks: {
    mainnet: {
      privateKey: process.env.TRON_PRIVATE_KEY,
      userFeePercentage: 100,
      feeLimit: 1000000000,
      fullHost: 'https://api.trongrid.io',
      network_id: '1'
    },
    shasta: {
      privateKey: process.env.TRON_PRIVATE_KEY,
      userFeePercentage: 100,
      feeLimit: 1000000000,
      fullHost: 'https://api.shasta.trongrid.io',
      network_id: '2'
    }
  },
  solc: {
    version: '0.8.20'
  }
};
```

#### 3. Create TRON Deployment Script

Create `scripts/deploy-tron.js`:

```javascript
const TronWeb = require('tronweb');

async function deployToTron() {
  const tronWeb = new TronWeb({
    fullHost: process.env.TRON_TESTNET_FULL_NODE,
    privateKey: process.env.TRON_PRIVATE_KEY
  });

  // Load compiled contract
  const contract = require('../build/contracts/FlashLoanProvider.json');
  
  // Deploy contract
  const deployed = await tronWeb.contract().new({
    abi: contract.abi,
    bytecode: contract.bytecode,
    feeLimit: 1000000000,
    callValue: 0,
    parameters: [tronWeb.defaultAddress.base58] // Initial owner
  });

  console.log('Contract deployed to TRON at:', deployed.address);
  return deployed;
}

deployToTron();
```

#### 4. Deploy to TRON

```bash
# Compile for TRON
tronbox compile

# Deploy to Shasta Testnet
tronbox migrate --network shasta

# Deploy to TRON Mainnet
tronbox migrate --network mainnet
```

### TRON-Specific Considerations

1. **Energy and Bandwidth:**
   - TRON transactions consume Energy (for smart contract execution)
   - Bandwidth (for transaction size)
   - Consider freezing TRX to get Energy

2. **TRC20 Token Addresses:**
   - TRON uses base58 addresses (starting with T)
   - Example: `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t` (USDT on TRON)

3. **Gas vs Energy:**
   - TRON uses "Energy" instead of gas
   - Energy is obtained by freezing TRX
   - Or paid directly in TRX

4. **Transaction Fees:**
   - Generally lower than Ethereum
   - Free transactions possible with frozen TRX

---

## Network Comparison

| Feature | Ethereum | BSC | Polygon | TRON |
|---------|----------|-----|---------|------|
| Token Standard | ERC20 | BEP20 | ERC20 | TRC20 |
| Average Gas Cost | High ($5-50) | Low ($0.10-1) | Very Low ($0.01) | Very Low ($0.01) |
| Block Time | ~12s | ~3s | ~2s | ~3s |
| Finality | ~15 min | ~1 min | ~2 min | ~1 min |
| Smart Contract Language | Solidity | Solidity | Solidity | Solidity |
| Deployment Tool | Hardhat | Hardhat | Hardhat | TronBox |
| EVM Compatible | Yes | Yes | Yes | Partial |

---

## Post-Deployment

### Verify Contracts

#### Ethereum/BSC/Polygon (via Etherscan-like explorers)

```bash
# Verify on Ethereum
npx hardhat verify --network mainnet DEPLOYED_CONTRACT_ADDRESS

# Verify on BSC
npx hardhat verify --network bsc DEPLOYED_CONTRACT_ADDRESS

# Verify on Polygon
npx hardhat verify --network polygon DEPLOYED_CONTRACT_ADDRESS
```

#### TRON (via TronScan)

1. Visit https://tronscan.org
2. Search for your contract address
3. Click "Contract" → "Verify and Publish"
4. Upload source code and select compiler version

### Configure the Contract

After deployment on any network:

1. **Add token support:**
```javascript
await flashLoanProvider.setSupportedToken(tokenAddress, true);
```

2. **Deposit liquidity:**
```javascript
await token.transfer(flashLoanProviderAddress, amount);
```

3. **Set fees (if needed):**
```javascript
await flashLoanProvider.setFlashLoanFee(9); // 0.09%
```

---

## Network-Specific Token Addresses

### USDT Addresses

- **Ethereum (ERC20):** `0xdAC17F958D2ee523a2206206994597C13D831ec7`
- **BSC (BEP20):** `0x55d398326f99059fF775485246999027B3197955`
- **Polygon (ERC20):** `0xc2132D05D31c914a87C6611C10748AEb04B58e8F` (USDT Polygon POS)
- **TRON (TRC20):** `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t`

### USDC Addresses

- **Ethereum (ERC20):** `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`
- **BSC (BEP20):** `0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d`
- **Polygon (ERC20):** `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`

---

## Troubleshooting

### Common Issues

#### 1. "Insufficient funds for gas"

**Solution:** Add more native tokens (ETH, BNB, MATIC) to your wallet.

#### 2. "Nonce too high"

**Solution:** Reset your wallet's transaction history or wait for pending transactions.

#### 3. "Network not found"

**Solution:** Check your .env file and ensure RPC URLs are correct.

#### 4. TRON deployment fails

**Solutions:**
- Ensure you have TRX for fees
- Check TronGrid API is accessible
- Verify private key format (64 character hex)

### Network Status

Check network status:
- Ethereum: https://ethstats.net/
- BSC: https://bscscan.com/
- Polygon: https://polygon.technology/
- TRON: https://tronscan.org/

---

## Security Considerations

### Multi-Chain Security

1. **Test on testnets first** - Always deploy to testnet before mainnet
2. **Verify contracts** - Verify source code on block explorers
3. **Different audits** - Each network may have different attack vectors
4. **Cross-chain risks** - Be aware of bridge vulnerabilities
5. **Private key management** - Use different keys for different networks

### Network-Specific Risks

- **Ethereum:** High gas costs can make small transactions unprofitable
- **BSC:** Centralization concerns (21 validators)
- **Polygon:** Dependent on Ethereum for security (sidechain)
- **TRON:** Different ecosystem, fewer audit tools

---

## Best Practices

1. **Start with testnet** - Deploy and test thoroughly
2. **Use hardware wallets** - For mainnet deployments with real funds
3. **Set up monitoring** - Track contract activity on each network
4. **Document addresses** - Keep a record of all deployed contracts
5. **Gradual rollout** - Deploy to one network, validate, then expand

---

## Resources

### Documentation

- [Hardhat Documentation](https://hardhat.org/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/)
- [BSC Documentation](https://docs.bnbchain.org/)
- [Polygon Documentation](https://wiki.polygon.technology/)
- [TRON Documentation](https://developers.tron.network/)

### Block Explorers

- Ethereum: https://etherscan.io
- BSC: https://bscscan.com
- Polygon: https://polygonscan.com
- TRON: https://tronscan.org

### Faucets

- Sepolia: https://sepoliafaucet.com/
- BSC Testnet: https://testnet.binance.org/faucet-smart
- Mumbai: https://faucet.polygon.technology/
- Shasta: https://www.trongrid.io/shasta

---

## Support

For network-specific questions:
- Check the main [README.md](README.md)
- See [QUICKSTART.md](QUICKSTART.md)
- Open an issue on GitHub

---

**Last Updated:** February 7, 2026

**Supported Networks:**
- ✅ Ethereum (ERC20)
- ✅ Binance Smart Chain (BEP20)
- ✅ Polygon (ERC20)
- 📝 TRON (TRC20) - Documentation and tooling guidance provided
