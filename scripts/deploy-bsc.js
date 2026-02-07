const hre = require("hardhat");

/**
 * Deploy Flash USDT to BSC (Binance Smart Chain)
 * 
 * Usage:
 *   npx hardhat run scripts/deploy-bsc.js --network bsc
 *   npx hardhat run scripts/deploy-bsc.js --network bscTestnet
 */
async function main() {
  const network = await hre.ethers.provider.getNetwork();
  console.log("Deploying to BSC network:", network.chainId.toString());

  // BSC USDT addresses
  const USDT_ADDRESSES = {
    56: '0x55d398326f99059fF775485246999027B3197955',  // BSC Mainnet
    97: '0x0000000000000000000000000000000000000000'   // BSC Testnet (update with actual)
  };

  const chainId = Number(network.chainId);
  let usdtAddress = USDT_ADDRESSES[chainId];

  // For testnet, deploy mock USDT if address is not set
  if (chainId === 97 && usdtAddress === '0x0000000000000000000000000000000000000000') {
    console.log("Deploying MockUSDT for BSC Testnet...");
    const MockUSDT = await hre.ethers.getContractFactory("MockUSDT");
    const usdt = await MockUSDT.deploy();
    await usdt.waitForDeployment();
    usdtAddress = await usdt.getAddress();
    console.log("MockUSDT deployed to:", usdtAddress);
  }

  // Deploy FlashUSDT
  console.log("Deploying FlashUSDT with USDT address:", usdtAddress);
  const FlashUSDT = await hre.ethers.getContractFactory("FlashUSDT");
  const flashUSDT = await FlashUSDT.deploy(usdtAddress);
  await flashUSDT.waitForDeployment();
  const flashUSDTAddress = await flashUSDT.getAddress();
  console.log("FlashUSDT deployed to:", flashUSDTAddress);

  // Deploy FlashLoanExample
  console.log("Deploying FlashLoanExample...");
  const FlashLoanExample = await hre.ethers.getContractFactory("FlashLoanExample");
  const example = await FlashLoanExample.deploy(flashUSDTAddress, usdtAddress);
  await example.waitForDeployment();
  const exampleAddress = await example.getAddress();
  console.log("FlashLoanExample deployed to:", exampleAddress);

  console.log("\n=== Deployment Summary ===");
  console.log("Network:", chainId === 56 ? "BSC Mainnet" : "BSC Testnet");
  console.log("Chain ID:", chainId);
  console.log("USDT:", usdtAddress);
  console.log("FlashUSDT:", flashUSDTAddress);
  console.log("FlashLoanExample:", exampleAddress);
  console.log("\nUpdate these addresses in desktop/src/app.js CONTRACT_ADDRESSES");
  
  // Verification instructions
  console.log("\n=== Verify on BscScan ===");
  const explorerUrl = chainId === 56 ? "https://bscscan.com" : "https://testnet.bscscan.com";
  console.log(`FlashUSDT: ${explorerUrl}/address/${flashUSDTAddress}#code`);
  console.log("\nVerification command:");
  console.log(`npx hardhat verify --network ${network.name} ${flashUSDTAddress} ${usdtAddress}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
