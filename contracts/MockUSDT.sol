// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/**
 * @title MockUSDT
 * @notice A mock USDT token for testing purposes
 * @dev This is a simple ERC20 token that mimics USDT
 */
contract MockUSDT is ERC20 {
    uint8 private _decimals;
    
    constructor() ERC20("Mock USDT", "USDT") {
        _decimals = 6; // USDT uses 6 decimals
        // Mint 1 million USDT to the deployer for testing
        _mint(msg.sender, 1_000_000 * 10**_decimals);
    }
    
    function decimals() public view virtual override returns (uint8) {
        return _decimals;
    }
    
    /**
     * @notice Mint tokens for testing
     * @param to Address to mint tokens to
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external {
        _mint(to, amount);
    }
}
