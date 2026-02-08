#!/usr/bin/env python3
"""
Example 2: Transfer USDT on Ethereum Network
"""

import os
import sys
from flash_usdt import FlashUSDT


def main():
    # Check if recipient address is provided
    if len(sys.argv) < 3:
        print("Usage: python example_transfer.py <recipient_address> <amount>")
        print("Example: python example_transfer.py 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb 10.5")
        sys.exit(1)
    
    recipient = sys.argv[1]
    amount = float(sys.argv[2])
    
    # Initialize
    flash = FlashUSDT()
    
    # Get private key from environment variable (RECOMMENDED)
    private_key = os.getenv('ETH_PRIVATE_KEY')
    
    if not private_key:
        print("ERROR: ETH_PRIVATE_KEY environment variable not set")
        print("Please set it using: export ETH_PRIVATE_KEY='your_private_key'")
        sys.exit(1)
    
    # Add wallet
    flash.add_wallet('sender', private_key, 'ethereum')
    wallet = flash.get_wallet('sender')
    
    # Display wallet info
    print("=" * 70)
    print("USDT Transfer - Ethereum Network (ERC20)")
    print("=" * 70)
    print(f"\nFrom Address: {wallet.get_address()}")
    print(f"To Address:   {recipient}")
    print(f"Amount:       {amount} USDT")
    
    # Check balance
    current_balance = wallet.get_balance()
    print(f"\nCurrent USDT Balance: {current_balance} USDT")
    
    if float(current_balance) < amount:
        print("\nERROR: Insufficient USDT balance!")
        sys.exit(1)
    
    # Check ETH balance for gas
    eth_balance = wallet.get_native_balance()
    print(f"Current ETH Balance:  {eth_balance} ETH")
    
    if float(eth_balance) < 0.001:
        print("\nWARNING: Low ETH balance. You may not have enough for gas fees.")
    
    # Confirm transaction
    print("\n" + "-" * 70)
    response = input("Proceed with transaction? (yes/no): ")
    
    if response.lower() != 'yes':
        print("Transaction cancelled.")
        sys.exit(0)
    
    # Execute transfer
    print("\nSending transaction...")
    
    try:
        tx_details = wallet.transfer_usdt(recipient, amount)
        
        print("\n" + "=" * 70)
        print("Transaction Submitted Successfully!")
        print("=" * 70)
        print(f"Transaction Hash: {tx_details['tx_hash']}")
        print(f"Network:          {tx_details['network'].upper()}")
        print(f"Amount:           {tx_details['amount']} USDT")
        print(f"Status:           {tx_details['status']}")
        print(f"\nView on Etherscan:")
        print(f"https://etherscan.io/tx/{tx_details['tx_hash']}")
        print("=" * 70)
        
    except Exception as e:
        print(f"\nERROR: Transaction failed - {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
