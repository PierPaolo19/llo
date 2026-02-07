const hre = require("hardhat");

/**
 * This script demonstrates a complete flash loan flow:
 * 1. Deploy contracts
 * 2. Setup liquidity
 * 3. Execute flash loan
 * 4. Display results
 */
async function main() {
  console.log("=== Flash USDT Demo ===\n");

  const [owner, liquidityProvider, borrower] = await hre.ethers.getSigners();
  console.log("Accounts:");
  console.log("- Owner:", owner.address);
  console.log("- Liquidity Provider:", liquidityProvider.address);
  console.log("- Borrower:", borrower.address);
  console.log("");

  // Step 1: Deploy MockUSDT
  console.log("📝 Deploying MockUSDT...");
  const MockUSDT = await hre.ethers.getContractFactory("MockUSDT");
  const usdt = await MockUSDT.deploy();
  await usdt.waitForDeployment();
  const usdtAddress = await usdt.getAddress();
  console.log("✅ MockUSDT deployed:", usdtAddress);
  console.log("");

  // Step 2: Deploy FlashUSDT
  console.log("📝 Deploying FlashUSDT...");
  const FlashUSDT = await hre.ethers.getContractFactory("FlashUSDT");
  const flashUSDT = await FlashUSDT.deploy(usdtAddress);
  await flashUSDT.waitForDeployment();
  const flashUSDTAddress = await flashUSDT.getAddress();
  console.log("✅ FlashUSDT deployed:", flashUSDTAddress);
  console.log("");

  // Step 3: Deploy FlashLoanExample
  console.log("📝 Deploying FlashLoanExample...");
  const FlashLoanExample = await hre.ethers.getContractFactory("FlashLoanExample");
  const example = await FlashLoanExample.deploy(flashUSDTAddress, usdtAddress);
  await example.waitForDeployment();
  const exampleAddress = await example.getAddress();
  console.log("✅ FlashLoanExample deployed:", exampleAddress);
  console.log("");

  // Step 4: Distribute USDT
  console.log("💰 Distributing USDT to accounts...");
  const distributionAmount = hre.ethers.parseUnits("50000", 6); // 50K USDT
  await usdt.transfer(liquidityProvider.address, distributionAmount);
  await usdt.transfer(borrower.address, distributionAmount);
  console.log("✅ Distributed 50K USDT to liquidity provider");
  console.log("✅ Distributed 50K USDT to borrower");
  console.log("");

  // Step 5: Add liquidity
  console.log("💧 Adding liquidity to FlashUSDT pool...");
  const liquidityAmount = hre.ethers.parseUnits("30000", 6); // 30K USDT
  await usdt.connect(liquidityProvider).approve(flashUSDTAddress, liquidityAmount);
  await flashUSDT.connect(liquidityProvider).deposit(liquidityAmount);
  console.log("✅ Added 30K USDT liquidity");
  console.log("Available liquidity:", hre.ethers.formatUnits(await flashUSDT.availableLiquidity(), 6), "USDT");
  console.log("");

  // Step 6: Execute Flash Loan
  console.log("⚡ Executing flash loan...");
  const loanAmount = hre.ethers.parseUnits("10000", 6); // 10K USDT
  const fee = await flashUSDT.calculateFee(loanAmount);
  
  console.log("Loan amount:", hre.ethers.formatUnits(loanAmount, 6), "USDT");
  console.log("Fee:", hre.ethers.formatUnits(fee, 6), "USDT");
  console.log("Total to repay:", hre.ethers.formatUnits(loanAmount + fee, 6), "USDT");
  console.log("");

  // Fund the example contract with fee
  await usdt.connect(borrower).approve(exampleAddress, fee);
  await example.connect(borrower).deposit(fee);
  console.log("✅ Example contract funded with fee");

  // Execute the flash loan
  const poolBalanceBefore = await flashUSDT.availableLiquidity();
  console.log("Pool balance before:", hre.ethers.formatUnits(poolBalanceBefore, 6), "USDT");
  
  const tx = await example.connect(borrower).executeFlashLoan(loanAmount);
  await tx.wait();
  
  const poolBalanceAfter = await flashUSDT.availableLiquidity();
  console.log("Pool balance after:", hre.ethers.formatUnits(poolBalanceAfter, 6), "USDT");
  console.log("Pool profit:", hre.ethers.formatUnits(poolBalanceAfter - poolBalanceBefore, 6), "USDT");
  console.log("");

  // Step 7: Display Summary
  console.log("=== Summary ===");
  console.log("✅ Flash loan executed successfully!");
  console.log("📊 Statistics:");
  console.log("  - Flash Loan Fee: 0.09%");
  console.log("  - Loan Amount:", hre.ethers.formatUnits(loanAmount, 6), "USDT");
  console.log("  - Fee Paid:", hre.ethers.formatUnits(fee, 6), "USDT");
  console.log("  - Pool Liquidity:", hre.ethers.formatUnits(await flashUSDT.availableLiquidity(), 6), "USDT");
  console.log("");
  console.log("📍 Contract Addresses:");
  console.log("  - MockUSDT:", usdtAddress);
  console.log("  - FlashUSDT:", flashUSDTAddress);
  console.log("  - FlashLoanExample:", exampleAddress);
  console.log("");
  console.log("🎉 Demo completed successfully!");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
