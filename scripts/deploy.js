const hre = require("hardhat");

async function main() {
  console.log("Deploying Flash USDT contracts...");

  // Deploy MockUSDT (for testing)
  const MockUSDT = await hre.ethers.getContractFactory("MockUSDT");
  const usdt = await MockUSDT.deploy();
  await usdt.waitForDeployment();
  const usdtAddress = await usdt.getAddress();
  console.log("MockUSDT deployed to:", usdtAddress);

  // Deploy FlashUSDT
  const FlashUSDT = await hre.ethers.getContractFactory("FlashUSDT");
  const flashUSDT = await FlashUSDT.deploy(usdtAddress);
  await flashUSDT.waitForDeployment();
  const flashUSDTAddress = await flashUSDT.getAddress();
  console.log("FlashUSDT deployed to:", flashUSDTAddress);

  // Deploy FlashLoanExample
  const FlashLoanExample = await hre.ethers.getContractFactory("FlashLoanExample");
  const example = await FlashLoanExample.deploy(flashUSDTAddress, usdtAddress);
  await example.waitForDeployment();
  const exampleAddress = await example.getAddress();
  console.log("FlashLoanExample deployed to:", exampleAddress);

  console.log("\nDeployment completed!");
  console.log("==================");
  console.log("MockUSDT:", usdtAddress);
  console.log("FlashUSDT:", flashUSDTAddress);
  console.log("FlashLoanExample:", exampleAddress);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
