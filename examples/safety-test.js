/**
 * Safety Test: Verify Mainnet Blocking
 * 
 * This test verifies that the tool properly blocks mainnet usage
 */

const { verifyTestnetOnly, validateNetworkConfig } = require('../src/index');

console.log('\n🛡️  Safety Test: Mainnet Blocking Verification\n');
console.log('═══════════════════════════════════════════════════════\n');

let testsPassed = 0;
let testsFailed = 0;

// Test 1: Block Ethereum Mainnet
console.log('Test 1: Block Ethereum Mainnet (Chain ID 1)');
try {
  verifyTestnetOnly(1);
  console.log('❌ FAILED: Mainnet was not blocked!\n');
  testsFailed++;
} catch (error) {
  console.log('✅ PASSED: Mainnet correctly blocked');
  console.log('   Error message:', error.message);
  console.log('');
  testsPassed++;
}

// Test 2: Block BSC Mainnet
console.log('Test 2: Block BSC Mainnet (Chain ID 56)');
try {
  verifyTestnetOnly(56);
  console.log('❌ FAILED: BSC Mainnet was not blocked!\n');
  testsFailed++;
} catch (error) {
  console.log('✅ PASSED: BSC Mainnet correctly blocked');
  console.log('   Error message:', error.message);
  console.log('');
  testsPassed++;
}

// Test 3: Block Polygon Mainnet
console.log('Test 3: Block Polygon Mainnet (Chain ID 137)');
try {
  verifyTestnetOnly(137);
  console.log('❌ FAILED: Polygon Mainnet was not blocked!\n');
  testsFailed++;
} catch (error) {
  console.log('✅ PASSED: Polygon Mainnet correctly blocked');
  console.log('   Error message:', error.message);
  console.log('');
  testsPassed++;
}

// Test 4: Allow Sepolia Testnet
console.log('Test 4: Allow Sepolia Testnet (Chain ID 11155111)');
try {
  verifyTestnetOnly(11155111);
  console.log('✅ PASSED: Sepolia testnet correctly allowed\n');
  testsPassed++;
} catch (error) {
  console.log('❌ FAILED: Sepolia testnet was blocked!');
  console.log('   Error message:', error.message);
  console.log('');
  testsFailed++;
}

// Test 5: Validate mainnet keyword detection
console.log('Test 5: Block configuration with "mainnet" keyword');
try {
  validateNetworkConfig({
    name: 'Ethereum Mainnet',
    chainId: 11155111 // Even with testnet ID
  });
  console.log('❌ FAILED: Mainnet keyword was not detected!\n');
  testsFailed++;
} catch (error) {
  console.log('✅ PASSED: Mainnet keyword correctly detected');
  console.log('   Error message:', error.message);
  console.log('');
  testsPassed++;
}

// Test 6: Allow valid testnet configuration
console.log('Test 6: Allow valid testnet configuration');
try {
  validateNetworkConfig({
    name: 'Ethereum Sepolia Testnet',
    chainId: 11155111,
    rpc: 'https://sepolia.infura.io/v3/'
  });
  console.log('✅ PASSED: Valid testnet configuration accepted\n');
  testsPassed++;
} catch (error) {
  console.log('❌ FAILED: Valid testnet was blocked!');
  console.log('   Error message:', error.message);
  console.log('');
  testsFailed++;
}

// Summary
console.log('═══════════════════════════════════════════════════════');
console.log('Test Results:');
console.log(`   ✅ Passed: ${testsPassed}/6`);
console.log(`   ❌ Failed: ${testsFailed}/6`);
console.log('');

if (testsFailed === 0) {
  console.log('🎉 All safety tests passed! Mainnet blocking is working correctly.');
  console.log('   This tool is safe for educational use on testnets only.');
} else {
  console.log('⚠️  Some safety tests failed! Do not use until fixed.');
}

console.log('═══════════════════════════════════════════════════════\n');

// Exit with appropriate code
process.exit(testsFailed > 0 ? 1 : 0);
