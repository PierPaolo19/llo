/**
 * Example: Basic Transfer Understanding
 * 
 * This example demonstrates the structure of a blockchain transaction
 * for educational purposes.
 * 
 * ⚠️ TESTNET ONLY - FOR LEARNING PURPOSES
 */

const { getTestnet, validateNetworkConfig } = require('../src/index');

console.log('\n🎓 Educational Example: Understanding Blockchain Transfers\n');
console.log('═══════════════════════════════════════════════════════\n');

// Get a testnet configuration
const network = getTestnet('ethereum_sepolia');
console.log('📍 Selected Network:', network.name);
console.log('🔗 Chain ID:', network.chainId);
console.log('💰 Currency:', network.currency);
console.log('');

// Validate that it's safe (testnet only)
validateNetworkConfig(network);
console.log('✅ Network validated as testnet\n');

// Example transaction structure (for educational purposes)
const exampleTransaction = {
  to: '0x0000000000000000000000000000000000000000', // Example address (burn address)
  value: '0.001', // 0.001 test ETH
  gasLimit: '21000',
  maxFeePerGas: '20',
  maxPriorityFeePerGas: '2',
  nonce: 0,
  chainId: network.chainId
};

console.log('📝 Example Transaction Structure:');
console.log(JSON.stringify(exampleTransaction, null, 2));
console.log('');

console.log('📚 What this teaches:');
console.log('   • Transaction structure and fields');
console.log('   • Gas concepts (limit, fees, priority)');
console.log('   • Chain ID for network identification');
console.log('   • Address formatting');
console.log('   • Value representation\n');

console.log('🔍 Understanding Each Field:');
console.log('');
console.log('   "to" - Recipient address (160-bit Ethereum address)');
console.log('   "value" - Amount to send (in ETH for Ethereum)');
console.log('   "gasLimit" - Maximum gas units for this transaction');
console.log('   "maxFeePerGas" - Maximum total fee per gas unit (in gwei)');
console.log('   "maxPriorityFeePerGas" - Tip to miners (in gwei)');
console.log('   "nonce" - Transaction counter for the sender');
console.log('   "chainId" - Network identifier to prevent replay attacks\n');

console.log('💡 Next Steps for Learning:');
console.log('   1. Get test tokens from faucet:', network.faucet);
console.log('   2. Use a testnet wallet (NEVER real wallet!)');
console.log('   3. Try sending a small test transaction');
console.log('   4. View it on the explorer:', network.explorer);
console.log('   5. Understand the transaction receipt\n');

console.log('🛡️  Safety Reminders:');
console.log('   • This example uses TESTNET only');
console.log('   • Test tokens have NO real value');
console.log('   • NEVER use real private keys for testing');
console.log('   • NEVER send real cryptocurrency to test addresses\n');

console.log('═══════════════════════════════════════════════════════\n');
console.log('Continue learning by exploring more blockchain concepts! 🚀\n');
