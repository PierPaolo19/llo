#!/usr/bin/env node

/**
 * LLO - Learn Ledger Operations
 * Educational Blockchain Testing Tool
 * 
 * ⚠️ FOR EDUCATIONAL PURPOSES ONLY - TESTNET USE ONLY ⚠️
 */

require('dotenv').config();

// Testnet RPC endpoints - THESE ARE TEST NETWORKS ONLY
const TESTNETS = {
  ethereum_sepolia: {
    name: 'Ethereum Sepolia Testnet',
    rpc: 'https://sepolia.infura.io/v3/',
    chainId: 11155111,
    explorer: 'https://sepolia.etherscan.io',
    faucet: 'https://sepoliafaucet.com/',
    currency: 'SepoliaETH'
  },
  ethereum_goerli: {
    name: 'Ethereum Goerli Testnet',
    rpc: 'https://goerli.infura.io/v3/',
    chainId: 5,
    explorer: 'https://goerli.etherscan.io',
    faucet: 'https://goerlifaucet.com/',
    currency: 'GoerliETH'
  },
  bsc_testnet: {
    name: 'Binance Smart Chain Testnet',
    rpc: 'https://data-seed-prebsc-1-s1.binance.org:8545/',
    chainId: 97,
    explorer: 'https://testnet.bscscan.com',
    faucet: 'https://testnet.binance.org/faucet-smart',
    currency: 'tBNB'
  },
  polygon_mumbai: {
    name: 'Polygon Mumbai Testnet',
    rpc: 'https://rpc-mumbai.maticvigil.com/',
    chainId: 80001,
    explorer: 'https://mumbai.polygonscan.com',
    faucet: 'https://faucet.polygon.technology/',
    currency: 'MATIC'
  },
  tron_shasta: {
    name: 'Tron Shasta Testnet',
    rpc: 'https://api.shasta.trongrid.io',
    explorer: 'https://shasta.tronscan.org',
    faucet: 'https://www.trongrid.io/shasta/',
    currency: 'TRX'
  }
};

// MAINNET BLOCKER - Prevent any mainnet usage
const MAINNET_CHAIN_IDS = [1, 56, 137, 728126428]; // Ethereum, BSC, Polygon, Tron mainnet
const MAINNET_KEYWORDS = ['mainnet', 'main-net', 'production', 'prod'];

/**
 * Verify that we're using a testnet and not a mainnet
 * @param {number} chainId - Chain ID to verify
 * @throws {Error} If mainnet detected
 */
function verifyTestnetOnly(chainId) {
  if (MAINNET_CHAIN_IDS.includes(chainId)) {
    throw new Error('🚫 MAINNET BLOCKED: This tool only works with testnets. Never use on mainnet!');
  }
}

/**
 * Check if a configuration contains mainnet references
 * @param {string} config - Configuration string to check
 * @throws {Error} If mainnet keywords detected
 */
function checkForMainnetKeywords(config) {
  const lowerConfig = config.toLowerCase();
  for (const keyword of MAINNET_KEYWORDS) {
    if (lowerConfig.includes(keyword)) {
      throw new Error(`🚫 MAINNET BLOCKED: Configuration contains mainnet keyword "${keyword}". Only testnets allowed!`);
    }
  }
}

/**
 * Display available testnets
 */
function displayTestnets() {
  console.log('\n🎓 LLO - Learn Ledger Operations');
  console.log('═══════════════════════════════════════════════════════');
  console.log('📚 Educational Blockchain Testing Tool');
  console.log('⚠️  FOR EDUCATIONAL PURPOSES ONLY - TESTNET USE ONLY\n');
  
  console.log('🌐 Available Test Networks:\n');
  
  Object.entries(TESTNETS).forEach(([key, network]) => {
    console.log(`📍 ${network.name}`);
    console.log(`   Chain ID: ${network.chainId || 'N/A'}`);
    console.log(`   Currency: ${network.currency}`);
    console.log(`   Explorer: ${network.explorer}`);
    console.log(`   Faucet: ${network.faucet}`);
    console.log('');
  });
  
  console.log('═══════════════════════════════════════════════════════');
  console.log('🔒 Safety Features:');
  console.log('   ✅ Testnet-only configuration');
  console.log('   ✅ Mainnet blocking built-in');
  console.log('   ✅ No real cryptocurrency involved');
  console.log('   ✅ Educational use only\n');
  
  console.log('📖 Next Steps:');
  console.log('   1. Choose a testnet from the list above');
  console.log('   2. Get test tokens from the faucet');
  console.log('   3. Configure your .env file (see .env.example)');
  console.log('   4. Run the examples: npm run examples\n');
  
  console.log('💡 Learn More:');
  console.log('   - Read the README.md for detailed instructions');
  console.log('   - Check the examples/ folder for code samples');
  console.log('   - Visit the testnet explorers to see transactions\n');
  
  console.log('⚠️  Remember: NEVER use real private keys or mainnet!');
  console.log('═══════════════════════════════════════════════════════\n');
}

/**
 * Get testnet configuration
 * @param {string} networkKey - Key of the network to get
 * @returns {object} Network configuration
 */
function getTestnet(networkKey) {
  const network = TESTNETS[networkKey];
  if (!network) {
    throw new Error(`Unknown testnet: ${networkKey}. Use one of: ${Object.keys(TESTNETS).join(', ')}`);
  }
  
  // Verify it's a testnet (double-check safety)
  if (network.chainId) {
    verifyTestnetOnly(network.chainId);
  }
  
  return network;
}

/**
 * Validate a network configuration before use
 * @param {object} config - Network configuration to validate
 * @returns {boolean} True if valid testnet
 */
function validateNetworkConfig(config) {
  if (!config) {
    throw new Error('No network configuration provided');
  }
  
  // Check chain ID if available
  if (config.chainId) {
    verifyTestnetOnly(config.chainId);
  }
  
  // Check for mainnet keywords in all string fields
  Object.values(config).forEach(value => {
    if (typeof value === 'string') {
      checkForMainnetKeywords(value);
    }
  });
  
  return true;
}

// Main execution
if (require.main === module) {
  displayTestnets();
}

// Export for use in other scripts
module.exports = {
  TESTNETS,
  getTestnet,
  verifyTestnetOnly,
  validateNetworkConfig,
  displayTestnets
};
