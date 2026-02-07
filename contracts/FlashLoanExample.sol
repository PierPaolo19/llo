// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "./IFlashLoanReceiver.sol";

/**
 * @title FlashLoanExample
 * @notice Example contract demonstrating how to use FlashUSDT flash loans
 * @dev This is a simple example that borrows USDT and immediately repays it
 */
contract FlashLoanExample is IFlashLoanReceiver {
    address public immutable flashUSDT;
    IERC20 public immutable usdt;
    
    event FlashLoanExecuted(uint256 amount, uint256 fee);
    
    constructor(address _flashUSDT, address _usdt) {
        flashUSDT = _flashUSDT;
        usdt = IERC20(_usdt);
    }
    
    /**
     * @notice Execute a flash loan
     * @dev This function is called by the user to initiate a flash loan
     * @param amount The amount to borrow
     */
    function executeFlashLoan(uint256 amount) external {
        // Call the flash loan function on FlashUSDT contract
        bytes memory data = abi.encode(msg.sender);
        (bool success, ) = flashUSDT.call(
            abi.encodeWithSignature(
                "flashLoan(address,uint256,bytes)",
                address(this),
                amount,
                data
            )
        );
        require(success, "Flash loan call failed");
    }
    
    /**
     * @notice This function is called by FlashUSDT after receiving the loan
     * @param amount The amount borrowed
     * @param fee The fee to be paid
     * @param initiator The address that initiated the flash loan
     * @param params Additional parameters
     */
    function executeOperation(
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        require(msg.sender == flashUSDT, "Unauthorized caller");
        
        // Here you would implement your custom logic
        // For example: arbitrage, liquidations, etc.
        
        // In this example, we just verify we received the funds
        require(
            usdt.balanceOf(address(this)) >= amount,
            "Did not receive flash loan"
        );
        
        // Calculate total amount to repay (loan + fee)
        uint256 totalDebt = amount + fee;
        
        // Approve FlashUSDT to take back the loan + fee
        require(
            usdt.approve(flashUSDT, totalDebt),
            "Approval failed"
        );
        
        // Transfer the loan + fee back to FlashUSDT
        require(
            usdt.transfer(flashUSDT, totalDebt),
            "Repayment failed"
        );
        
        emit FlashLoanExecuted(amount, fee);
        
        return true;
    }
    
    /**
     * @notice Fund this contract with USDT to pay fees
     * @param amount Amount of USDT to deposit
     */
    function deposit(uint256 amount) external {
        require(
            usdt.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
    }
    
    /**
     * @notice Withdraw USDT from this contract
     * @param amount Amount to withdraw
     */
    function withdraw(uint256 amount) external {
        require(
            usdt.transfer(msg.sender, amount),
            "Transfer failed"
        );
    }
}
