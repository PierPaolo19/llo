const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);
  console.log("Account balance:", (await hre.ethers.provider.getBalance(deployer.address)).toString());

  // Deploy FlashLoanProvider
  const FlashLoanProvider = await hre.ethers.getContractFactory("FlashLoanProvider");
  const flashLoanProvider = await FlashLoanProvider.deploy(deployer.address);
  await flashLoanProvider.waitForDeployment();

  const providerAddress = await flashLoanProvider.getAddress();
  console.log("FlashLoanProvider deployed to:", providerAddress);

  // Deploy FlashLoanReceiverExample
  const FlashLoanReceiverExample = await hre.ethers.getContractFactory("FlashLoanReceiverExample");
  const flashLoanReceiver = await FlashLoanReceiverExample.deploy(providerAddress);
  await flashLoanReceiver.waitForDeployment();

  const receiverAddress = await flashLoanReceiver.getAddress();
  console.log("FlashLoanReceiverExample deployed to:", receiverAddress);

  console.log("\nDeployment Summary:");
  console.log("==================");
  console.log("FlashLoanProvider:", providerAddress);
  console.log("FlashLoanReceiverExample:", receiverAddress);
  console.log("\nNext steps:");
  console.log("1. Add token support: call setSupportedToken(tokenAddress, true)");
  console.log("2. Deposit tokens to the provider contract");
  console.log("3. Request flash loans using the flashLoan function");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
