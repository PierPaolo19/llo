# Flash Loan Examples

This directory contains practical examples of how to use the Flash USDT protocol.

## Example 1: Simple Arbitrage

This example shows how to use a flash loan for arbitrage between two DEXs.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../contracts/IFlashLoanReceiver.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ArbitrageExample is IFlashLoanReceiver {
    address public immutable flashLoanProvider;
    address public immutable dexA;
    address public immutable dexB;
    
    constructor(address _provider, address _dexA, address _dexB) {
        flashLoanProvider = _provider;
        dexA = _dexA;
        dexB = _dexB;
    }
    
    function executeOperation(
        address token,
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        require(msg.sender == flashLoanProvider, "Unauthorized");
        
        // 1. Sell tokens on DEX A
        // sellOnDexA(token, amount);
        
        // 2. Buy tokens on DEX B at lower price
        // buyOnDexB(token, amount);
        
        // 3. Calculate profit and ensure we can repay
        uint256 totalDebt = amount + fee;
        require(IERC20(token).balanceOf(address(this)) >= totalDebt, "Insufficient profit");
        
        // 4. Approve repayment
        IERC20(token).approve(flashLoanProvider, totalDebt);
        
        return true;
    }
}
```

## Example 2: Collateral Swap

Swap collateral in a lending protocol without closing your position.

```solidity
contract CollateralSwapExample is IFlashLoanReceiver {
    address public immutable flashLoanProvider;
    address public immutable lendingProtocol;
    
    function executeOperation(
        address token,
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        require(msg.sender == flashLoanProvider, "Unauthorized");
        
        // Decode the target collateral token
        (address newCollateralToken) = abi.decode(params, (address));
        
        // 1. Use flash loan to repay old debt
        // lendingProtocol.repay(token, amount);
        
        // 2. Withdraw old collateral
        // lendingProtocol.withdrawCollateral(oldCollateralToken);
        
        // 3. Swap old collateral for new collateral
        // swap(oldCollateralToken, newCollateralToken);
        
        // 4. Deposit new collateral
        // lendingProtocol.depositCollateral(newCollateralToken);
        
        // 5. Borrow same amount + fee
        // lendingProtocol.borrow(token, amount + fee);
        
        // 6. Approve repayment
        uint256 totalDebt = amount + fee;
        IERC20(token).approve(flashLoanProvider, totalDebt);
        
        return true;
    }
}
```

## Example 3: Liquidation

Liquidate undercollateralized positions for profit.

```solidity
contract LiquidationExample is IFlashLoanReceiver {
    address public immutable flashLoanProvider;
    address public immutable lendingProtocol;
    
    function executeOperation(
        address token,
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        require(msg.sender == flashLoanProvider, "Unauthorized");
        
        // Decode the user to liquidate
        (address userToLiquidate) = abi.decode(params, (address));
        
        // 1. Use flash loan to liquidate undercollateralized position
        // lendingProtocol.liquidate(userToLiquidate, token, amount);
        
        // 2. Receive collateral at discount
        // Collateral is now in this contract
        
        // 3. Swap collateral back to borrowed token
        // swap(collateralToken, token);
        
        // 4. Ensure profit covers fee
        uint256 totalDebt = amount + fee;
        require(IERC20(token).balanceOf(address(this)) >= totalDebt, "Liquidation not profitable");
        
        // 5. Approve repayment
        IERC20(token).approve(flashLoanProvider, totalDebt);
        
        return true;
    }
}
```

## Example 4: Testing with Hardhat

Here's how to test a flash loan in your Hardhat tests:

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Flash Loan Integration", function () {
  let flashLoanProvider;
  let mockToken;
  let myReceiver;
  let owner;

  beforeEach(async function () {
    [owner] = await ethers.getSigners();

    // Deploy mock token
    const MockToken = await ethers.getContractFactory("MockERC20");
    mockToken = await MockToken.deploy("Mock USDT", "USDT", 6);
    
    // Deploy flash loan provider
    const FlashLoanProvider = await ethers.getContractFactory("FlashLoanProvider");
    flashLoanProvider = await FlashLoanProvider.deploy(owner.address);
    
    // Deploy your custom receiver
    const MyReceiver = await ethers.getContractFactory("MyFlashLoanReceiver");
    myReceiver = await MyReceiver.deploy(await flashLoanProvider.getAddress());
    
    // Setup
    const mintAmount = ethers.parseUnits("1000000", 6);
    await mockToken.mint(await flashLoanProvider.getAddress(), mintAmount);
    await flashLoanProvider.setSupportedToken(await mockToken.getAddress(), true);
  });

  it("Should execute custom flash loan logic", async function () {
    const loanAmount = ethers.parseUnits("100000", 6);
    const fee = await flashLoanProvider.flashFee(loanAmount);
    
    // Ensure receiver can pay fee
    await mockToken.mint(await myReceiver.getAddress(), fee);
    
    // Execute flash loan
    await expect(
      flashLoanProvider.flashLoan(
        await myReceiver.getAddress(),
        await mockToken.getAddress(),
        loanAmount,
        "0x"
      )
    ).to.emit(flashLoanProvider, "FlashLoan");
  });
});
```

## Example 5: Deployment Script

Deploy the contracts to a network:

```javascript
const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  
  console.log("Deploying with account:", deployer.address);

  // Deploy provider
  const FlashLoanProvider = await hre.ethers.getContractFactory("FlashLoanProvider");
  const provider = await FlashLoanProvider.deploy(deployer.address);
  await provider.waitForDeployment();
  
  console.log("FlashLoanProvider:", await provider.getAddress());

  // Add USDT support (example address)
  const usdtAddress = "0xdAC17F958D2ee523a2206206994597C13D831ec7"; // Mainnet USDT
  await provider.setSupportedToken(usdtAddress, true);
  
  console.log("USDT support added");

  // Deploy your receiver
  const MyReceiver = await hre.ethers.getContractFactory("MyFlashLoanReceiver");
  const receiver = await MyReceiver.deploy(await provider.getAddress());
  await receiver.waitForDeployment();
  
  console.log("MyReceiver:", await receiver.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
```

## Tips for Successful Flash Loans

1. **Always Test on Testnet First**: Use Goerli or Sepolia before mainnet
2. **Calculate Profitability**: Ensure your operation will cover the fee + gas
3. **Handle Reverts Gracefully**: Your contract should handle failures
4. **Monitor Gas Prices**: High gas can eat into profits
5. **Use Events**: Emit events for debugging and monitoring
6. **Consider MEV**: Be aware of front-running and sandwich attacks

## Common Pitfalls

1. **Forgetting to Approve**: Always approve the provider to pull tokens back
2. **Insufficient Balance**: Ensure you have enough to repay loan + fee
3. **Gas Limit Issues**: Complex operations may hit block gas limits
4. **Slippage**: DEX trades may have different prices than expected
5. **Reentrancy**: Always use reentrancy guards in your receiver

## Resources

- [Flash Loans Documentation](../README.md)
- [Hardhat Documentation](https://hardhat.org/docs)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts)
