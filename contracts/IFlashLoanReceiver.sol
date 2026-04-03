// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title IFlashLoanReceiver
 * @notice Interface for contracts that want to receive flash loans
 * @dev Implement this interface in your contract to receive flash loans from FlashUSDT
 */
interface IFlashLoanReceiver {
    /**
     * @notice Execute operation after receiving flash loan
     * @param amount The amount of USDT borrowed
     * @param fee The fee to be paid
     * @param initiator The address that initiated the flash loan
     * @param params Additional parameters passed to the flash loan
     * @return True if the operation was successful
     */
    function executeOperation(
        uint256 amount,
        uint256 fee,
        address initiator,
        bytes calldata params
    ) external returns (bool);
}
