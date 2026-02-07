# Multi-Network Quick Reference

## Supported Networks Overview

| Network | Standard | Chain ID | Gas Cost | Speed | Status |
|---------|----------|----------|----------|-------|---------|
| Ethereum | ERC20 | 1 | High | Medium | ✅ |
| BSC | BEP20 | 56 | Low | Fast | ✅ |
| Polygon | ERC20 | 137 | Very Low | Fast | ✅ |
| TRON | TRC20 | - | Very Low | Fast | 📝 |

## Deployment Commands

### Mainnet
```bash
npm run deploy:mainnet    # Ethereum
npm run deploy:bsc        # Binance Smart Chain
npm run deploy:polygon    # Polygon
```

### Testnet
```bash
npm run deploy:sepolia      # Ethereum Sepolia
npm run deploy:bscTestnet   # BSC Testnet
npx hardhat run scripts/deploy.js --network mumbai  # Polygon Mumbai
```

### TRON (TRC20)
See [Network Guide](NETWORK_GUIDE.md#tron-deployment-trc20) - Requires TronBox

## Testnet Faucets

| Network | Faucet URL | Token |
|---------|-----------|-------|
| Ethereum Sepolia | https://sepoliafaucet.com/ | ETH |
| BSC Testnet | https://testnet.binance.org/faucet-smart | BNB |
| Polygon Mumbai | https://faucet.polygon.technology/ | MATIC |
| TRON Shasta | https://www.trongrid.io/shasta | TRX |

## Block Explorers

| Network | Explorer URL |
|---------|-------------|
| Ethereum | https://etherscan.io |
| BSC | https://bscscan.com |
| Polygon | https://polygonscan.com |
| TRON | https://tronscan.org |

## Popular Token Addresses

### USDT
- **Ethereum (ERC20):** `0xdAC17F958D2ee523a2206206994597C13D831ec7`
- **BSC (BEP20):** `0x55d398326f99059fF775485246999027B3197955`
- **Polygon:** `0xc2132D05D31c914a87C6611C10748AEb04B58e8F`
- **TRON (TRC20):** `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t`

### USDC
- **Ethereum (ERC20):** `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`
- **BSC (BEP20):** `0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d`
- **Polygon:** `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`

## RPC Endpoints

### Ethereum
- Mainnet: `https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY`
- Sepolia: `https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY`

### Binance Smart Chain
- Mainnet: `https://bsc-dataseed1.binance.org`
- Testnet: `https://data-seed-prebsc-1-s1.binance.org:8545`

### Polygon
- Mainnet: `https://polygon-rpc.com`
- Mumbai: `https://rpc-mumbai.maticvigil.com`

### TRON
- Mainnet: `https://api.trongrid.io`
- Shasta: `https://api.shasta.trongrid.io`

## Environment Variables

```bash
# Private Key (All networks)
PRIVATE_KEY=your_private_key_here

# Alchemy API Key (Recommended RPC provider)
ALCHEMY_API_KEY=your_alchemy_api_key

# Ethereum
ETHEREUM_MAINNET_RPC_URL=https://eth-mainnet.g.alchemy.com/v2/${ALCHEMY_API_KEY}
SEPOLIA_RPC_URL=https://eth-sepolia.g.alchemy.com/v2/${ALCHEMY_API_KEY}

# BSC
BSC_MAINNET_RPC_URL=https://bsc-dataseed1.binance.org
BSC_TESTNET_RPC_URL=https://data-seed-prebsc-1-s1.binance.org:8545

# Polygon
POLYGON_MAINNET_RPC_URL=https://polygon-mainnet.g.alchemy.com/v2/${ALCHEMY_API_KEY}
POLYGON_MUMBAI_RPC_URL=https://polygon-mumbai.g.alchemy.com/v2/${ALCHEMY_API_KEY}

# API Keys for verification
ETHERSCAN_API_KEY=your_key
BSCSCAN_API_KEY=your_key
POLYGONSCAN_API_KEY=your_key
```

📖 **For detailed API key setup, see [API_KEYS.md](API_KEYS.md)**

## Contract Verification

```bash
# Ethereum
npx hardhat verify --network mainnet CONTRACT_ADDRESS

# BSC
npx hardhat verify --network bsc CONTRACT_ADDRESS

# Polygon
npx hardhat verify --network polygon CONTRACT_ADDRESS
```

## Quick Start Per Network

### Ethereum (ERC20)
1. Get ETH or testnet ETH
2. Configure `.env` with Ethereum RPC
3. `npm run deploy:mainnet` or `npm run deploy:sepolia`

### BSC (BEP20)
1. Get BNB or testnet BNB
2. Configure `.env` with BSC RPC (or use default)
3. `npm run deploy:bsc` or `npm run deploy:bscTestnet`

### Polygon (ERC20)
1. Get MATIC or testnet MATIC
2. Configure `.env` with Polygon RPC (or use default)
3. `npm run deploy:polygon`

### TRON (TRC20)
1. Install TronBox: `npm install -g tronbox`
2. Get TRX or testnet TRX
3. Follow [TRON guide](NETWORK_GUIDE.md#tron-deployment-trc20)

## Network Features Comparison

### Transaction Costs (Approximate)
- **Ethereum:** $5-50 per transaction
- **BSC:** $0.10-1 per transaction
- **Polygon:** $0.01 per transaction
- **TRON:** $0.01 per transaction

### Block Times
- **Ethereum:** ~12 seconds
- **BSC:** ~3 seconds
- **Polygon:** ~2 seconds
- **TRON:** ~3 seconds

### Finality
- **Ethereum:** ~15 minutes
- **BSC:** ~1 minute
- **Polygon:** ~2 minutes
- **TRON:** ~1 minute

## Token Standards

### ERC20 (Ethereum, Polygon)
- Standard: EIP-20
- Most widely used
- Full OpenZeppelin compatibility
- Works on all EVM chains

### BEP20 (Binance Smart Chain)
- ERC20-compatible
- Same interface as ERC20
- Lower fees than Ethereum
- Fast transactions

### TRC20 (TRON)
- Similar to ERC20
- TRON-specific
- Very low fees
- High throughput

## Common Issues

### "Insufficient funds"
- Add more native tokens (ETH/BNB/MATIC/TRX)

### "Network not found"
- Check RPC URLs in `.env`
- Verify network name in command

### "Nonce too high"
- Reset wallet transaction history
- Wait for pending transactions

### Contract verification fails
- Ensure correct network
- Check API key is valid
- Verify constructor arguments match

## Next Steps

1. **Choose Network** - See comparison above
2. **Get Test Tokens** - Use faucets
3. **Deploy** - Use npm scripts
4. **Test** - On testnet first
5. **Verify** - Verify on block explorer
6. **Deploy Mainnet** - When ready

## More Information

- **Detailed Guide:** [NETWORK_GUIDE.md](NETWORK_GUIDE.md)
- **Quick Start:** [QUICKSTART.md](QUICKSTART.md)
- **Main Docs:** [README.md](README.md)

---

**Multi-Chain Flash Loans** | ERC20 • BEP20 • TRC20
