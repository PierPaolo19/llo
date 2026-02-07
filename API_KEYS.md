# API Keys Guide

This document provides detailed information about all API keys used in the Flash USDT project.

## Table of Contents

1. [Required API Keys](#required-api-keys)
2. [Optional API Keys](#optional-api-keys)
3. [How to Obtain API Keys](#how-to-obtain-api-keys)
4. [Security Best Practices](#security-best-practices)

---

## Required API Keys

### 1. Private Key (Wallet)

**Variable:** `PRIVATE_KEY`

**Description:** Your Ethereum wallet private key for deploying contracts and signing transactions.

**How to get:**
- Export from MetaMask: Account menu → Account details → Export Private Key
- Generate new wallet: Use tools like `ethers.js` or MetaMask

⚠️ **CRITICAL:** Never share or commit your private key!

### 2. RPC Provider API Keys

#### Alchemy API Key

**Variable:** `ALCHEMY_API_KEY`

**Description:** Provides access to Ethereum, Polygon, and other blockchain networks.

**How to get:**
1. Visit https://www.alchemy.com/
2. Sign up for free account
3. Create a new app
4. Copy your API key from the dashboard

**Free Tier:** 
- 300M compute units/month
- Sufficient for development and testing

#### Alternative: Infura API Key

**Variable:** `INFURA_API_KEY`

**Description:** Alternative RPC provider for blockchain access.

**How to get:**
1. Visit https://infura.io/
2. Sign up for free account
3. Create a new project
4. Copy your Project ID (API key)

**Free Tier:**
- 100,000 requests/day
- Good for development

### 3. Block Explorer API Keys

#### Etherscan API Key

**Variable:** `ETHERSCAN_API_KEY`

**Description:** For verifying smart contracts on Ethereum mainnet and testnets.

**How to get:**
1. Visit https://etherscan.io/
2. Sign up for account
3. Go to API Keys section
4. Create new API key

**Free Tier:**
- 5 calls/second
- 100,000 calls/day

#### BSCScan API Key

**Variable:** `BSCSCAN_API_KEY`

**Description:** For verifying contracts on Binance Smart Chain.

**How to get:**
1. Visit https://bscscan.com/
2. Sign up for account
3. Navigate to API-KEYs
4. Create new API key

**Free Tier:**
- 5 calls/second
- Similar to Etherscan

#### PolygonScan API Key

**Variable:** `POLYGONSCAN_API_KEY`

**Description:** For verifying contracts on Polygon network.

**How to get:**
1. Visit https://polygonscan.com/
2. Sign up for account
3. Go to API Keys
4. Generate new key

**Free Tier:**
- 5 calls/second
- Standard rate limits

---

## Optional API Keys

### 1. TronGrid API Key

**Variable:** `TRONGRID_API_KEY`

**Description:** For TRON network access (TRC20 deployments).

**How to get:**
1. Visit https://www.trongrid.io/
2. Sign up for account
3. Get API key from dashboard

**Usage:** Required only if deploying to TRON network.

### 2. CoinMarketCap API Key

**Variable:** `COINMARKETCAP_API_KEY`

**Description:** For gas price oracle and cryptocurrency price data.

**How to get:**
1. Visit https://coinmarketcap.com/api/
2. Sign up for free account
3. Copy API key from dashboard

**Usage:** 
- Gas price estimation
- Token price feeds
- Gas reporter in Hardhat

**Free Tier:**
- 10,000 calls/month
- Basic plan

### 3. Moralis API Key

**Variable:** `MORALIS_API_KEY`

**Description:** Web3 development platform for blockchain data and APIs.

**How to get:**
1. Visit https://moralis.io/
2. Sign up for account
3. Create new project
4. Copy API key

**Usage:**
- NFT APIs
- Token data
- Transaction history
- Real-time events

### 4. The Graph API Key

**Variable:** `THEGRAPH_API_KEY`

**Description:** For querying indexed blockchain data via GraphQL.

**How to get:**
1. Visit https://thegraph.com/
2. Sign up and create account
3. Generate API key in dashboard

**Usage:**
- Querying blockchain data
- Custom subgraphs
- Historical data

### 5. Tenderly API Keys

**Variables:** 
- `TENDERLY_ACCESS_KEY`
- `TENDERLY_PROJECT_SLUG`

**Description:** Smart contract monitoring, debugging, and analytics.

**How to get:**
1. Visit https://tenderly.co/
2. Sign up for account
3. Create project
4. Generate access key in settings

**Usage:**
- Transaction debugging
- Smart contract monitoring
- Gas profiling
- Alert notifications

### 6. OpenZeppelin Defender

**Variables:**
- `DEFENDER_API_KEY`
- `DEFENDER_API_SECRET`

**Description:** Secure smart contract automation and operations.

**How to get:**
1. Visit https://defender.openzeppelin.com/
2. Sign up for account
3. Go to Team API Keys
4. Create new API key

**Usage:**
- Automated operations
- Transaction relaying
- Security monitoring
- Access control

---

## How to Obtain API Keys

### Quick Setup Guide

1. **Start with Alchemy** (Highest Priority)
   ```bash
   # Sign up at https://www.alchemy.com/
   # Get your API key
   ALCHEMY_API_KEY=your_alchemy_key_here
   ```

2. **Add Block Explorer Keys**
   ```bash
   # Etherscan - https://etherscan.io/myapikey
   ETHERSCAN_API_KEY=your_etherscan_key

   # BSCScan - https://bscscan.com/myapikey
   BSCSCAN_API_KEY=your_bscscan_key

   # PolygonScan - https://polygonscan.com/myapikey
   POLYGONSCAN_API_KEY=your_polygonscan_key
   ```

3. **Optional: Add CoinMarketCap** (For gas estimation)
   ```bash
   # CoinMarketCap - https://coinmarketcap.com/api/
   COINMARKETCAP_API_KEY=your_cmc_key
   ```

### Configuration Steps

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit .env file:**
   ```bash
   nano .env  # or use your preferred editor
   ```

3. **Add your API keys:**
   - Replace placeholder values with actual keys
   - Keep the `.env` file private (it's in `.gitignore`)

4. **Verify configuration:**
   ```bash
   # Test with Hardhat
   npx hardhat compile
   ```

---

## Security Best Practices

### DO's ✅

1. **Use Environment Variables**
   - Always use `.env` file for sensitive data
   - Never hardcode API keys in source code

2. **Keep .env Private**
   - Ensure `.env` is in `.gitignore`
   - Never commit `.env` to version control

3. **Use Different Keys for Different Environments**
   - Development keys for local testing
   - Separate keys for production

4. **Rotate Keys Regularly**
   - Change API keys periodically
   - Especially after team member changes

5. **Use Read-Only Keys When Possible**
   - Many services offer read-only API keys
   - Use these for non-critical operations

6. **Monitor API Usage**
   - Check API dashboards regularly
   - Set up usage alerts
   - Watch for suspicious activity

### DON'Ts ❌

1. **Never Commit Private Keys**
   - Don't commit `.env` file
   - Don't paste keys in public channels
   - Don't screenshot keys

2. **Don't Share API Keys**
   - Each developer should have their own keys
   - Don't email or message keys

3. **Don't Use Production Keys in Development**
   - Keep environments separate
   - Use testnet keys for testing

4. **Don't Expose Keys in Logs**
   - Be careful with console.log
   - Review log files before sharing

---

## API Key Limits and Pricing

### Free Tier Comparison

| Service | Free Tier | Rate Limit | Notes |
|---------|-----------|------------|-------|
| Alchemy | 300M CU/month | High | Recommended |
| Infura | 100k req/day | Medium | Good alternative |
| Etherscan | 100k calls/day | 5/sec | Standard |
| BSCScan | Unlimited* | 5/sec | *With limits |
| PolygonScan | 100k calls/day | 5/sec | Standard |
| CoinMarketCap | 10k calls/month | Basic | Limited |
| Moralis | 40k req/day | Medium | Generous free tier |

### When to Upgrade

Consider paid plans when:
- Exceeding free tier limits
- Need higher rate limits
- Require advanced features
- Running production applications

---

## Troubleshooting

### Common Issues

#### "Invalid API Key" Error

**Solution:**
1. Verify key is correctly copied
2. Check for extra spaces
3. Ensure key is active in dashboard
4. Regenerate key if needed

#### Rate Limit Exceeded

**Solution:**
1. Check your usage dashboard
2. Implement request caching
3. Add delays between requests
4. Upgrade to paid plan

#### Network Connection Issues

**Solution:**
1. Verify RPC URL is correct
2. Check API key is included
3. Test with curl:
   ```bash
   curl -X POST https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
   ```

#### Environment Variables Not Loading

**Solution:**
1. Ensure `.env` file is in project root
2. Check `dotenv` is installed: `npm install dotenv`
3. Verify `require('dotenv').config()` is in config file
4. Restart your terminal/IDE

---

## Additional Resources

### Documentation Links

- **Alchemy:** https://docs.alchemy.com/
- **Infura:** https://docs.infura.io/
- **Etherscan:** https://docs.etherscan.io/
- **Hardhat:** https://hardhat.org/hardhat-runner/docs/config
- **OpenZeppelin:** https://docs.openzeppelin.com/defender/

### Support

- Check provider-specific documentation
- Join Discord communities
- Review Stack Overflow
- Open GitHub issues for project-specific problems

---

## Quick Reference

### Minimum Required for Development

```bash
PRIVATE_KEY=your_wallet_private_key
ALCHEMY_API_KEY=your_alchemy_key
ETHERSCAN_API_KEY=your_etherscan_key
```

### Recommended for Full Features

```bash
PRIVATE_KEY=your_wallet_private_key
ALCHEMY_API_KEY=your_alchemy_key
ETHERSCAN_API_KEY=your_etherscan_key
BSCSCAN_API_KEY=your_bscscan_key
POLYGONSCAN_API_KEY=your_polygonscan_key
COINMARKETCAP_API_KEY=your_cmc_key
```

### Complete Setup (All Features)

See `.env.example` for the complete list of all available API keys.

---

**Last Updated:** February 7, 2026

**Need Help?** Open an issue on GitHub or check the [README.md](README.md)
