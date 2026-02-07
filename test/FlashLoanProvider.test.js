const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("FlashLoanProvider", function () {
  let flashLoanProvider;
  let mockToken;
  let flashLoanReceiver;
  let owner;
  let user1;

  beforeEach(async function () {
    [owner, user1] = await ethers.getSigners();

    // Deploy a mock ERC20 token
    const MockToken = await ethers.getContractFactory("MockERC20");
    mockToken = await MockToken.deploy("Mock USDT", "USDT", 6);
    await mockToken.waitForDeployment();

    // Deploy FlashLoanProvider
    const FlashLoanProvider = await ethers.getContractFactory("FlashLoanProvider");
    flashLoanProvider = await FlashLoanProvider.deploy(owner.address);
    await flashLoanProvider.waitForDeployment();

    // Deploy FlashLoanReceiverExample
    const FlashLoanReceiverExample = await ethers.getContractFactory("FlashLoanReceiverExample");
    flashLoanReceiver = await FlashLoanReceiverExample.deploy(await flashLoanProvider.getAddress());
    await flashLoanReceiver.waitForDeployment();

    // Setup: mint tokens and add support
    const mintAmount = ethers.parseUnits("1000000", 6); // 1M USDT
    await mockToken.mint(await flashLoanProvider.getAddress(), mintAmount);
    await flashLoanProvider.setSupportedToken(await mockToken.getAddress(), true);
  });

  describe("Deployment", function () {
    it("Should set the right owner", async function () {
      expect(await flashLoanProvider.owner()).to.equal(owner.address);
    });

    it("Should set default fee to 9 basis points", async function () {
      expect(await flashLoanProvider.flashLoanFee()).to.equal(9);
    });
  });

  describe("Token Support", function () {
    it("Should allow owner to add token support", async function () {
      const newToken = await mockToken.getAddress();
      await expect(flashLoanProvider.setSupportedToken(newToken, true))
        .to.emit(flashLoanProvider, "TokenSupported")
        .withArgs(newToken, true);
      
      expect(await flashLoanProvider.supportedTokens(newToken)).to.be.true;
    });

    it("Should not allow non-owner to add token support", async function () {
      const newToken = await mockToken.getAddress();
      await expect(
        flashLoanProvider.connect(user1).setSupportedToken(newToken, true)
      ).to.be.reverted;
    });
  });

  describe("Flash Loans", function () {
    it("Should execute a successful flash loan", async function () {
      const loanAmount = ethers.parseUnits("100000", 6); // 100k USDT
      const fee = await flashLoanProvider.flashFee(loanAmount);
      
      // Fund the receiver with enough to pay the fee
      await mockToken.mint(await flashLoanReceiver.getAddress(), fee);

      const tokenAddress = await mockToken.getAddress();
      const receiverAddress = await flashLoanReceiver.getAddress();

      await expect(
        flashLoanProvider.flashLoan(
          receiverAddress,
          tokenAddress,
          loanAmount,
          "0x"
        )
      ).to.emit(flashLoanProvider, "FlashLoan");
    });

    it("Should fail for unsupported token", async function () {
      const MockToken = await ethers.getContractFactory("MockERC20");
      const unsupportedToken = await MockToken.deploy("Unsupported", "UNS", 18);
      await unsupportedToken.waitForDeployment();

      const loanAmount = ethers.parseUnits("1000", 18);
      
      await expect(
        flashLoanProvider.flashLoan(
          await flashLoanReceiver.getAddress(),
          await unsupportedToken.getAddress(),
          loanAmount,
          "0x"
        )
      ).to.be.revertedWith("Token not supported");
    });

    it("Should fail if amount is 0", async function () {
      await expect(
        flashLoanProvider.flashLoan(
          await flashLoanReceiver.getAddress(),
          await mockToken.getAddress(),
          0,
          "0x"
        )
      ).to.be.revertedWith("Amount must be greater than 0");
    });

    it("Should fail if insufficient liquidity", async function () {
      const loanAmount = ethers.parseUnits("2000000", 6); // 2M USDT (more than available)
      
      await expect(
        flashLoanProvider.flashLoan(
          await flashLoanReceiver.getAddress(),
          await mockToken.getAddress(),
          loanAmount,
          "0x"
        )
      ).to.be.revertedWith("Insufficient liquidity");
    });
  });

  describe("Fee Management", function () {
    it("Should allow owner to update fee", async function () {
      const newFee = 15;
      await expect(flashLoanProvider.setFlashLoanFee(newFee))
        .to.emit(flashLoanProvider, "FeeUpdated")
        .withArgs(9, newFee);
      
      expect(await flashLoanProvider.flashLoanFee()).to.equal(newFee);
    });

    it("Should not allow fee above 1%", async function () {
      await expect(
        flashLoanProvider.setFlashLoanFee(101)
      ).to.be.revertedWith("Fee too high");
    });

    it("Should calculate fee correctly", async function () {
      const amount = ethers.parseUnits("100000", 6);
      const expectedFee = (amount * 9n) / 10000n;
      expect(await flashLoanProvider.flashFee(amount)).to.equal(expectedFee);
    });
  });

  describe("Withdrawal", function () {
    it("Should allow owner to withdraw tokens", async function () {
      const withdrawAmount = ethers.parseUnits("50000", 6);
      const tokenAddress = await mockToken.getAddress();
      
      await expect(
        flashLoanProvider.withdraw(tokenAddress, withdrawAmount, user1.address)
      ).to.emit(flashLoanProvider, "Withdrawal");

      expect(await mockToken.balanceOf(user1.address)).to.equal(withdrawAmount);
    });

    it("Should not allow non-owner to withdraw", async function () {
      const withdrawAmount = ethers.parseUnits("50000", 6);
      const tokenAddress = await mockToken.getAddress();
      
      await expect(
        flashLoanProvider.connect(user1).withdraw(tokenAddress, withdrawAmount, user1.address)
      ).to.be.reverted;
    });
  });

  describe("View Functions", function () {
    it("Should return correct max flash loan amount", async function () {
      const tokenAddress = await mockToken.getAddress();
      const providerBalance = await mockToken.balanceOf(await flashLoanProvider.getAddress());
      
      expect(await flashLoanProvider.maxFlashLoan(tokenAddress)).to.equal(providerBalance);
    });

    it("Should return 0 for unsupported token", async function () {
      const MockToken = await ethers.getContractFactory("MockERC20");
      const unsupportedToken = await MockToken.deploy("Unsupported", "UNS", 18);
      await unsupportedToken.waitForDeployment();
      
      expect(await flashLoanProvider.maxFlashLoan(await unsupportedToken.getAddress())).to.equal(0);
    });
  });
});
