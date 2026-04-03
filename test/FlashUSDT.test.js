const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("FlashUSDT", function () {
  let flashUSDT;
  let usdt;
  let owner;
  let user1;
  let user2;
  let flashLoanExample;

  const INITIAL_SUPPLY = ethers.parseUnits("1000000", 6); // 1M USDT
  const DEPOSIT_AMOUNT = ethers.parseUnits("10000", 6); // 10K USDT
  const LOAN_AMOUNT = ethers.parseUnits("5000", 6); // 5K USDT

  beforeEach(async function () {
    [owner, user1, user2] = await ethers.getSigners();

    // Deploy MockUSDT
    const MockUSDT = await ethers.getContractFactory("MockUSDT");
    usdt = await MockUSDT.deploy();
    await usdt.waitForDeployment();

    // Deploy FlashUSDT
    const FlashUSDT = await ethers.getContractFactory("FlashUSDT");
    flashUSDT = await FlashUSDT.deploy(await usdt.getAddress());
    await flashUSDT.waitForDeployment();

    // Deploy FlashLoanExample
    const FlashLoanExample = await ethers.getContractFactory("FlashLoanExample");
    flashLoanExample = await FlashLoanExample.deploy(
      await flashUSDT.getAddress(),
      await usdt.getAddress()
    );
    await flashLoanExample.waitForDeployment();

    // Transfer some USDT to users
    await usdt.transfer(user1.address, DEPOSIT_AMOUNT);
    await usdt.transfer(user2.address, DEPOSIT_AMOUNT);
  });

  describe("Deployment", function () {
    it("Should set the correct USDT address", async function () {
      expect(await flashUSDT.usdt()).to.equal(await usdt.getAddress());
    });

    it("Should set the correct owner", async function () {
      expect(await flashUSDT.owner()).to.equal(owner.address);
    });

    it("Should have default fee of 9 basis points", async function () {
      expect(await flashUSDT.flashLoanFee()).to.equal(9);
    });
  });

  describe("Deposit and Withdraw", function () {
    it("Should allow users to deposit USDT", async function () {
      await usdt.connect(user1).approve(await flashUSDT.getAddress(), DEPOSIT_AMOUNT);
      await expect(flashUSDT.connect(user1).deposit(DEPOSIT_AMOUNT))
        .to.emit(flashUSDT, "Deposit")
        .withArgs(user1.address, DEPOSIT_AMOUNT);

      expect(await flashUSDT.availableLiquidity()).to.equal(DEPOSIT_AMOUNT);
    });

    it("Should allow owner to withdraw USDT", async function () {
      await usdt.connect(user1).approve(await flashUSDT.getAddress(), DEPOSIT_AMOUNT);
      await flashUSDT.connect(user1).deposit(DEPOSIT_AMOUNT);

      await expect(flashUSDT.withdraw(DEPOSIT_AMOUNT, owner.address))
        .to.emit(flashUSDT, "Withdraw")
        .withArgs(owner.address, DEPOSIT_AMOUNT);

      expect(await flashUSDT.availableLiquidity()).to.equal(0);
    });

    it("Should not allow non-owner to withdraw", async function () {
      await usdt.connect(user1).approve(await flashUSDT.getAddress(), DEPOSIT_AMOUNT);
      await flashUSDT.connect(user1).deposit(DEPOSIT_AMOUNT);

      await expect(
        flashUSDT.connect(user1).withdraw(DEPOSIT_AMOUNT, user1.address)
      ).to.be.revertedWithCustomError(flashUSDT, "OwnableUnauthorizedAccount");
    });
  });

  describe("Flash Loan Fee", function () {
    it("Should calculate correct fee", async function () {
      const amount = ethers.parseUnits("1000", 6);
      const expectedFee = (amount * 9n) / 10000n;
      expect(await flashUSDT.calculateFee(amount)).to.equal(expectedFee);
    });

    it("Should allow owner to update fee", async function () {
      const newFee = 15;
      await expect(flashUSDT.setFlashLoanFee(newFee))
        .to.emit(flashUSDT, "FlashLoanFeeUpdated")
        .withArgs(9, newFee);

      expect(await flashUSDT.flashLoanFee()).to.equal(newFee);
    });

    it("Should not allow fee to exceed maximum", async function () {
      const maxFee = await flashUSDT.MAX_FLASH_LOAN_FEE();
      await expect(
        flashUSDT.setFlashLoanFee(maxFee + 1n)
      ).to.be.revertedWith("FlashUSDT: Fee exceeds maximum");
    });

    it("Should not allow non-owner to update fee", async function () {
      await expect(
        flashUSDT.connect(user1).setFlashLoanFee(15)
      ).to.be.revertedWithCustomError(flashUSDT, "OwnableUnauthorizedAccount");
    });
  });

  describe("Flash Loan", function () {
    beforeEach(async function () {
      // Deposit liquidity
      await usdt.connect(user1).approve(await flashUSDT.getAddress(), DEPOSIT_AMOUNT);
      await flashUSDT.connect(user1).deposit(DEPOSIT_AMOUNT);
    });

    it("Should execute a successful flash loan", async function () {
      // Fund the example contract with enough USDT to pay the fee
      const fee = await flashUSDT.calculateFee(LOAN_AMOUNT);
      await usdt.connect(user2).approve(await flashLoanExample.getAddress(), fee);
      await flashLoanExample.connect(user2).deposit(fee);

      const balanceBefore = await flashUSDT.availableLiquidity();
      
      await expect(flashLoanExample.connect(user2).executeFlashLoan(LOAN_AMOUNT))
        .to.emit(flashUSDT, "FlashLoan");

      const balanceAfter = await flashUSDT.availableLiquidity();
      expect(balanceAfter).to.equal(balanceBefore + fee);
    });

    it("Should fail if insufficient liquidity", async function () {
      const tooMuch = DEPOSIT_AMOUNT + 1n;
      await expect(
        flashUSDT.flashLoan(await flashLoanExample.getAddress(), tooMuch, "0x")
      ).to.be.revertedWith("FlashUSDT: Insufficient liquidity");
    });

    it("Should fail if amount is zero", async function () {
      await expect(
        flashUSDT.flashLoan(await flashLoanExample.getAddress(), 0, "0x")
      ).to.be.revertedWith("FlashUSDT: Amount must be greater than 0");
    });

    it("Should fail if receiver is zero address", async function () {
      await expect(
        flashUSDT.flashLoan(ethers.ZeroAddress, LOAN_AMOUNT, "0x")
      ).to.be.revertedWith("FlashUSDT: Invalid receiver");
    });
  });

  describe("Available Liquidity", function () {
    it("Should return correct available liquidity", async function () {
      expect(await flashUSDT.availableLiquidity()).to.equal(0);

      await usdt.connect(user1).approve(await flashUSDT.getAddress(), DEPOSIT_AMOUNT);
      await flashUSDT.connect(user1).deposit(DEPOSIT_AMOUNT);

      expect(await flashUSDT.availableLiquidity()).to.equal(DEPOSIT_AMOUNT);
    });
  });
});
