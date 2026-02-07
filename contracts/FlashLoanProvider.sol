// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import "./IFlashLoanReceiver.sol";

/**
 * @title FlashLoanProvider
 * @notice A simple flash loan provider contract for USDT and other ERC20 tokens
 * @dev Allows users to borrow tokens for a single transaction with a small fee
 */
contract FlashLoanProvider is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Fee in basis points (e.g., 9 = 0.09%)
    uint256 public flashLoanFee = 9;
    uint256 public constant FEE_DENOMINATOR = 10000;

    // Mapping to track supported tokens
    mapping(address => bool) public supportedTokens;

    // Events
    event FlashLoan(
        address indexed receiver,
        address indexed token,
        uint256 amount,
        uint256 fee,
        address indexed initiator
    );
    event FeeUpdated(uint256 oldFee, uint256 newFee);
    event TokenSupported(address indexed token, bool supported);
    event Withdrawal(address indexed token, uint256 amount, address indexed to);

    /**
     * @notice Constructor
     * @param initialOwner The initial owner of the contract
     */
    constructor(address initialOwner) Ownable(initialOwner) {}

    /**
     * @notice Request a flash loan
     * @param receiverAddress The address of the contract receiving the tokens
     * @param token The address of the token to borrow
     * @param amount The amount of tokens to borrow
     * @param params Additional parameters to pass to the receiver
     */
    function flashLoan(
        address receiverAddress,
        address token,
        uint256 amount,
        bytes calldata params
    ) external nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 tokenContract = IERC20(token);
        uint256 availableBalance = tokenContract.balanceOf(address(this));
        require(availableBalance >= amount, "Insufficient liquidity");

        // Calculate fee
        uint256 fee = (amount * flashLoanFee) / FEE_DENOMINATOR;
        
        // Record balance before
        uint256 balanceBefore = tokenContract.balanceOf(address(this));

        // Transfer tokens to receiver
        tokenContract.safeTransfer(receiverAddress, amount);

        // Execute operation
        IFlashLoanReceiver receiver = IFlashLoanReceiver(receiverAddress);
        bool success = receiver.executeOperation(
            token,
            amount,
            fee,
            msg.sender,
            params
        );
        require(success, "Flash loan execution failed");

        // Check that we received the loan + fee back
        uint256 balanceAfter = tokenContract.balanceOf(address(this));
        require(
            balanceAfter >= balanceBefore + fee,
            "Flash loan not repaid with fee"
        );

        emit FlashLoan(receiverAddress, token, amount, fee, msg.sender);
    }

    /**
     * @notice Update the flash loan fee
     * @param newFee The new fee in basis points
     */
    function setFlashLoanFee(uint256 newFee) external onlyOwner {
        require(newFee <= 100, "Fee too high"); // Max 1%
        uint256 oldFee = flashLoanFee;
        flashLoanFee = newFee;
        emit FeeUpdated(oldFee, newFee);
    }

    /**
     * @notice Add or remove support for a token
     * @param token The token address
     * @param supported Whether the token should be supported
     */
    function setSupportedToken(address token, bool supported) external onlyOwner {
        supportedTokens[token] = supported;
        emit TokenSupported(token, supported);
    }

    /**
     * @notice Withdraw tokens from the contract
     * @param token The token address
     * @param amount The amount to withdraw
     * @param to The recipient address
     */
    function withdraw(address token, uint256 amount, address to) external onlyOwner {
        require(to != address(0), "Invalid recipient");
        IERC20(token).safeTransfer(to, amount);
        emit Withdrawal(token, amount, to);
    }

    /**
     * @notice Get the maximum flash loan amount for a token
     * @param token The token address
     * @return The maximum borrowable amount
     */
    function maxFlashLoan(address token) external view returns (uint256) {
        if (!supportedTokens[token]) {
            return 0;
        }
        return IERC20(token).balanceOf(address(this));
    }

    /**
     * @notice Calculate the flash loan fee for an amount
     * @param amount The loan amount
     * @return The fee amount
     */
    function flashFee(uint256 amount) external view returns (uint256) {
        return (amount * flashLoanFee) / FEE_DENOMINATOR;
    }
}
