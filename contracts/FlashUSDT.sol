// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import "./IFlashLoanReceiver.sol";

/**
 * @title FlashUSDT
 * @notice A flash loan provider for USDT tokens
 * @dev Allows users to borrow USDT with no collateral, as long as the loan is repaid within the same transaction
 */
contract FlashUSDT is Ownable, ReentrancyGuard {
    IERC20 public immutable usdt;
    
    // Fee percentage in basis points (1 basis point = 0.01%)
    // Default: 9 basis points = 0.09%
    uint256 public flashLoanFee = 9;
    uint256 public constant MAX_FLASH_LOAN_FEE = 100; // 1%
    uint256 public constant FEE_PRECISION = 10000;
    
    // Events
    event FlashLoan(
        address indexed receiver,
        address indexed initiator,
        uint256 amount,
        uint256 fee
    );
    
    event FlashLoanFeeUpdated(uint256 oldFee, uint256 newFee);
    
    event Deposit(address indexed depositor, uint256 amount);
    
    event Withdraw(address indexed recipient, uint256 amount);
    
    /**
     * @notice Constructor
     * @param _usdt Address of the USDT token contract
     */
    constructor(address _usdt) Ownable(msg.sender) {
        require(_usdt != address(0), "FlashUSDT: Invalid USDT address");
        usdt = IERC20(_usdt);
    }
    
    /**
     * @notice Get the available liquidity for flash loans
     * @return The amount of USDT available for flash loans
     */
    function availableLiquidity() public view returns (uint256) {
        return usdt.balanceOf(address(this));
    }
    
    /**
     * @notice Calculate the fee for a given flash loan amount
     * @param amount The amount of USDT to borrow
     * @return The fee amount in USDT
     */
    function calculateFee(uint256 amount) public view returns (uint256) {
        return (amount * flashLoanFee) / FEE_PRECISION;
    }
    
    /**
     * @notice Execute a flash loan
     * @param receiver The contract that will receive the flash loan
     * @param amount The amount of USDT to borrow
     * @param params Additional parameters to pass to the receiver
     */
    function flashLoan(
        address receiver,
        uint256 amount,
        bytes calldata params
    ) external nonReentrant {
        require(receiver != address(0), "FlashUSDT: Invalid receiver");
        require(amount > 0, "FlashUSDT: Amount must be greater than 0");
        
        uint256 availableBalance = availableLiquidity();
        require(amount <= availableBalance, "FlashUSDT: Insufficient liquidity");
        
        uint256 fee = calculateFee(amount);
        uint256 balanceBefore = availableBalance;
        
        // Transfer the loan amount to the receiver
        require(
            usdt.transfer(receiver, amount),
            "FlashUSDT: Transfer failed"
        );
        
        // Execute the operation on the receiver contract
        require(
            IFlashLoanReceiver(receiver).executeOperation(
                amount,
                fee,
                msg.sender,
                params
            ),
            "FlashUSDT: Operation execution failed"
        );
        
        // Ensure the loan + fee has been repaid
        uint256 balanceAfter = usdt.balanceOf(address(this));
        require(
            balanceAfter >= balanceBefore + fee,
            "FlashUSDT: Flash loan not repaid"
        );
        
        emit FlashLoan(receiver, msg.sender, amount, fee);
    }
    
    /**
     * @notice Update the flash loan fee (only owner)
     * @param newFee The new fee in basis points
     */
    function setFlashLoanFee(uint256 newFee) external onlyOwner {
        require(
            newFee <= MAX_FLASH_LOAN_FEE,
            "FlashUSDT: Fee exceeds maximum"
        );
        
        uint256 oldFee = flashLoanFee;
        flashLoanFee = newFee;
        
        emit FlashLoanFeeUpdated(oldFee, newFee);
    }
    
    /**
     * @notice Deposit USDT to provide liquidity
     * @param amount The amount of USDT to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "FlashUSDT: Amount must be greater than 0");
        require(
            usdt.transferFrom(msg.sender, address(this), amount),
            "FlashUSDT: Transfer failed"
        );
        
        emit Deposit(msg.sender, amount);
    }
    
    /**
     * @notice Withdraw USDT liquidity (only owner)
     * @param amount The amount of USDT to withdraw
     * @param recipient The address to receive the USDT
     */
    function withdraw(uint256 amount, address recipient) external onlyOwner {
        require(recipient != address(0), "FlashUSDT: Invalid recipient");
        require(amount > 0, "FlashUSDT: Amount must be greater than 0");
        require(
            amount <= availableLiquidity(),
            "FlashUSDT: Insufficient balance"
        );
        require(
            usdt.transfer(recipient, amount),
            "FlashUSDT: Transfer failed"
        );
        
        emit Withdraw(recipient, amount);
    }
}
