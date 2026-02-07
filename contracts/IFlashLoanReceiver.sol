// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title IFlashLoanReceiver
 * @notice Interface for flash loan receivers
 * @dev Contracts receiving flash loans must implement this interface
 */
interface IFlashLoanReceiver {
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
    ) external returns (bool);
}
