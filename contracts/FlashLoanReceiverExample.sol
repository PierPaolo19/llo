// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./IFlashLoanReceiver.sol";

/**
 * @title FlashLoanReceiverExample
 * @notice Example implementation of a flash loan receiver
 * @dev This is a basic example showing how to receive and repay a flash loan
 */
contract FlashLoanReceiverExample is IFlashLoanReceiver, Ownable {
    using SafeERC20 for IERC20;

    address public immutable flashLoanProvider;
    
    event OperationExecuted(
        address token,
        uint256 amount,
        uint256 fee,
        address initiator
    );

    /**
     * @notice Constructor
     * @param _flashLoanProvider The address of the flash loan provider
     */
    constructor(address _flashLoanProvider) Ownable(msg.sender) {
        require(_flashLoanProvider != address(0), "Invalid provider address");
        flashLoanProvider = _flashLoanProvider;
    }

    /**
     * @notice Execute operation after receiving flash loan
     * @param token The address of the token being borrowed
     * @param amount The amount of tokens borrowed
     * @param fee The fee amount that must be paid back
     * @param initiator The address that initiated the flash loan
     * @param params Additional parameters for the operation
     * @return success True if the operation was successful
     */
    function executeOperation(
        address token,
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        require(msg.sender == flashLoanProvider, "Caller must be flash loan provider");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Did not receive tokens");

        // Decode params if needed
        // (uint256 someParam) = abi.decode(params, (uint256));

        // ========================================
        // YOUR CUSTOM LOGIC GOES HERE
        // ========================================
        // Example: Arbitrage, liquidation, collateral swap, etc.
        // For this example, we just hold the tokens temporarily
        
        // In a real scenario, you would:
        // 1. Use the borrowed tokens for your operation
        // 2. Generate profit to cover the fee
        // 3. Repay the loan + fee
        
        // ========================================

        // Calculate total amount to repay (loan + fee)
        uint256 totalDebt = amount + fee;
        
        // Approve the flash loan provider to pull back the tokens
        IERC20(token).safeApprove(flashLoanProvider, totalDebt);

        emit OperationExecuted(token, amount, fee, initiator);

        return true;
    }

    /**
     * @notice Allow owner to withdraw tokens
     * @param token The token address
     * @param amount The amount to withdraw
     */
    function withdrawToken(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(msg.sender, amount);
    }

    /**
     * @notice Receive function to accept ETH
     */
    receive() external payable {}
}
