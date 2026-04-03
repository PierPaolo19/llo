# Multi-Chain Network Support

Flash USDT now supports multiple blockchain networks, allowing you to deploy and use flash loans across different chains.

## Supported Networks

### 🔷 ERC20 Networks (Ethereum Compatible)

#### Ethereum Mainnet
- **Chain ID**: 1
- **Token Standard**: ERC20
- **USDT Contract**: `0xdac17f958d2ee523a2206206994597c13d831ec7`
- **Explorer**: https://etherscan.io
- **Gas Token**: ETH
- **RPC**: https://eth.llamarpc.com

#### Sepolia Testnet
- **Chain ID**: 11155111
- **Token Standard**: ERC20
- **Explorer**: https://sepolia.etherscan.io
- **Gas Token**: SepoliaETH
- **RPC**: https://rpc.sepolia.org

#### Polygon Mainnet
- **Chain ID**: 137
- **Token Standard**: ERC20 (Polygon is EVM compatible)
- **USDT Contract**: `0xc2132D05D31c914a87C6611C10748AEb04B58e8F`
- **Explorer**: https://polygonscan.com
- **Gas Token**: MATIC
- **RPC**: https://polygon-rpc.com

#### Mumbai Testnet (Polygon)
- **Chain ID**: 80001
- **Token Standard**: ERC20
- **Explorer**: https://mumbai.polygonscan.com
- **Gas Token**: MATIC
- **RPC**: https://rpc-mumbai.maticvigil.com

### 🟡 BEP20 Networks (Binance Smart Chain)

#### BSC Mainnet
- **Chain ID**: 56
- **Token Standard**: BEP20
- **USDT Contract**: `0x55d398326f99059fF775485246999027B3197955` (BSC-USD)
- **Explorer**: https://bscscan.com
- **Gas Token**: BNB
- **RPC**: https://bsc-dataseed.binance.org

#### BSC Testnet
- **Chain ID**: 97
- **Token Standard**: BEP20
- **Explorer**: https://testnet.bscscan.com
- **Gas Token**: BNB
- **RPC**: https://data-seed-prebsc-1-s1.binance.org:8545

### 🔴 TRC20 Networks (Tron)

**Note**: Tron uses a different architecture and requires separate tooling.

#### Tron Mainnet
- **Token Standard**: TRC20
- **USDT Contract**: `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t`
- **Explorer**: https://tronscan.org
- **Gas Token**: TRX (energy/bandwidth)
- **Tooling Required**: TronWeb, TronBox

#### Tron Shasta Testnet
- **Token Standard**: TRC20
- **Explorer**: https://shasta.tronscan.org
- **Gas Token**: TRX
- **Faucet**: https://www.trongrid.io/shasta

## Network Comparison

| Network | Standard | Gas Cost | Block Time | TVL | Mainnet USDT Address |
|---------|----------|----------|------------|-----|---------------------|
| Ethereum | ERC20 | High ($5-50) | 12s | Highest | 0xdac1...1ec7 |
| BSC | BEP20 | Low ($0.1-1) | 3s | High | 0x55d3...7955 |
| Polygon | ERC20 | Very Low ($0.01-0.1) | 2s | Medium | 0xc213...8e8F |
| Tron | TRC20 | Very Low | 3s | Medium | TR7N...Lj6t |

## Adding Networks to MetaMask

### Using the Desktop App

The Flash USDT desktop application includes quick-add buttons:

1. Connect your MetaMask wallet
2. In the "Network Status & Configuration" section
3. Click "Add BSC Network" or "Add Polygon Network"
4. Approve in MetaMask

### Manual Configuration

#### BSC Mainnet
```
Network Name: Binance Smart Chain
RPC URL: https://bsc-dataseed.binance.org
Chain ID: 56
Symbol: BNB
Explorer: https://bscscan.com
```

#### Polygon Mainnet
```
Network Name: Polygon Mainnet
RPC URL: https://polygon-rpc.com
Chain ID: 137
Symbol: MATIC
Explorer: https://polygonscan.com
```

## Deploying to Different Networks

### Ethereum/Polygon (ERC20)

Using Hardhat:

```bash
# Deploy to BSC Mainnet
npx hardhat run scripts/deploy.js --network bsc

# Deploy to BSC Testnet
npx hardhat run scripts/deploy.js --network bscTestnet

# Deploy to Polygon
npx hardhat run scripts/deploy.js --network polygon

# Deploy to Sepolia
npx hardhat run scripts/deploy.js --network sepolia
```

### Configuration

Create a `.env` file:

```bash
# Private key (without 0x prefix)
PRIVATE_KEY=your_private_key_here

# RPC URLs (optional - defaults provided)
ETHEREUM_RPC_URL=https://eth.llamarpc.com
BSC_RPC_URL=https://bsc-dataseed.binance.org
POLYGON_RPC_URL=https://polygon-rpc.com
SEPOLIA_RPC_URL=https://rpc.sepolia.org
```

### Tron (TRC20)

Tron requires different tooling. See the [Tron Deployment Guide](TRON.md) for details.

## Network-Specific Considerations

### Ethereum (ERC20)
- ✅ Highest security and decentralization
- ✅ Most liquidity
- ❌ Highest gas fees
- ⚠️ Best for large transactions where security is paramount

### BSC (BEP20)
- ✅ Low gas fees
- ✅ Fast transactions
- ✅ Good liquidity
- ⚠️ More centralized than Ethereum
- ⚠️ Best for medium transactions

### Polygon (ERC20)
- ✅ Very low gas fees
- ✅ Fast transactions
- ✅ EVM compatible
- ⚠️ Lower liquidity than Ethereum/BSC
- ⚠️ Best for small-medium transactions

### Tron (TRC20)
- ✅ Very low fees
- ✅ High throughput
- ✅ Popular in Asia
- ❌ Requires different development tools
- ⚠️ Different programming model (not EVM)

## Gas Optimization Tips

### For BSC and Polygon
```solidity
// Already optimized in FlashUSDT.sol
// - Uses immutable for constant addresses
// - Minimal storage operations
// - Efficient loops
```

### Estimating Costs

| Network | Flash Loan (Est.) | Deposit | Withdraw |
|---------|------------------|---------|----------|
| Ethereum | $10-30 | $5-15 | $3-10 |
| BSC | $0.20-0.50 | $0.10-0.30 | $0.10-0.30 |
| Polygon | $0.01-0.05 | $0.01-0.02 | $0.01-0.02 |
| Tron | ~$0.01 | ~$0.01 | ~$0.01 |

## Security Considerations

### Network-Specific Risks

1. **Ethereum**: Most secure, but highest cost
2. **BSC**: Good security, watch for centralization risks
3. **Polygon**: Check validator set, bridge security
4. **Tron**: Different security model, verify with TronScan

### Bridge Risks

When moving USDT between networks:
- Always use official bridges
- Verify contract addresses
- Start with small amounts
- Check bridge liquidity

### Smart Contract Addresses

**Always verify contract addresses on official block explorers before interacting!**

Official USDT addresses:
- Ethereum: https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7
- BSC: https://bscscan.com/token/0x55d398326f99059fF775485246999027B3197955
- Polygon: https://polygonscan.com/token/0xc2132D05D31c914a87C6611C10748AEb04B58e8F
- Tron: https://tronscan.org/#/token20/TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t

## Testing on Testnets

Before deploying to mainnet:

1. **Get testnet tokens**:
   - Sepolia ETH: https://sepoliafaucet.com
   - BSC Testnet BNB: https://testnet.binance.org/faucet-smart
   - Mumbai MATIC: https://faucet.polygon.technology
   - Tron Shasta TRX: https://www.trongrid.io/shasta

2. **Deploy contracts** to testnet
3. **Test all functions** thoroughly
4. **Monitor gas usage**
5. **Verify on testnet explorer**

## Troubleshooting

### "Wrong Network" Error
- Check MetaMask is on the correct network
- Verify chain ID matches deployment

### "Insufficient Gas" Error
- Ensure you have native tokens (ETH/BNB/MATIC/TRX)
- Increase gas limit if needed

### "Contract Not Found"
- Verify contract is deployed on this network
- Check CONTRACT_ADDRESSES in app.js
- Confirm you're on the right network

### Can't Add Network
- Update MetaMask to latest version
- Try adding manually via Settings > Networks
- Check RPC URL is accessible

## Resources

- [Ethereum Documentation](https://ethereum.org/developers)
- [BSC Documentation](https://docs.bnbchain.org)
- [Polygon Documentation](https://docs.polygon.technology)
- [Tron Documentation](https://developers.tron.network)

## Support

For network-specific issues:
- Ethereum/Sepolia: Ethereum Discord
- BSC: Binance Smart Chain Forum
- Polygon: Polygon Discord
- Tron: Tron Discord

For Flash USDT issues:
- GitHub: https://github.com/PierPaolo19/llo/issues

---

**Updated**: February 2026  
**Multi-chain support**: ERC20, BEP20, TRC20 (documentation)
