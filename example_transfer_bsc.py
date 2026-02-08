#!/usr/bin/env python3
"""
Example 3: Transfer USDT on BSC Network
"""

import os
import sys
from flash_usdt import FlashUSDT


def main():
    # Check arguments
    if len(sys.argv) < 3:
        print("Usage: python example_transfer_bsc.py <recipient_address> <amount>")
        print("Example: python example_transfer_bsc.py 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb 10.5")
        sys.exit(1)
    
    recipient = sys.argv[1]
    amount = float(sys.argv[2])
    
    # Initialize
    flash = FlashUSDT()
    
    # Get private key from environment variable
    private_key = os.getenv('BSC_PRIVATE_KEY')
    
    if not private_key:
        print("ERROR: BSC_PRIVATE_KEY environment variable not set")
        sys.exit(1)
    
    # Add BSC wallet
    flash.add_wallet('sender', private_key, 'bsc')
    wallet = flash.get_wallet('sender')
    
    # Display info
    print("=" * 70)
    print("USDT Transfer - Binance Smart Chain (BEP20)")
    print("=" * 70)
    print(f"\nFrom Address: {wallet.get_address()}")
    print(f"To Address:   {recipient}")
    print(f"Amount:       {amount} USDT")
    
    # Check balances
    usdt_balance = wallet.get_balance()
    bnb_balance = wallet.get_native_balance()
    
    print(f"\nCurrent USDT Balance: {usdt_balance} USDT")
    print(f"Current BNB Balance:  {bnb_balance} BNB")
    
    if float(usdt_balance) < amount:
        print("\nERROR: Insufficient USDT balance!")
        sys.exit(1)
    
    if float(bnb_balance) < 0.001:
        print("\nWARNING: Low BNB balance for gas fees.")
    
    # Confirm
    response = input("\nProceed with transaction? (yes/no): ")
    if response.lower() != 'yes':
        print("Transaction cancelled.")
        sys.exit(0)
    
    # Execute
    print("\nSending transaction...")
    
    try:
        tx_details = wallet.transfer_usdt(recipient, amount)
        
        print("\n" + "=" * 70)
        print("Transaction Submitted Successfully!")
        print("=" * 70)
        print(f"Transaction Hash: {tx_details['tx_hash']}")
        print(f"View on BSCScan:")
        print(f"https://bscscan.com/tx/{tx_details['tx_hash']}")
        print("=" * 70)
        
    except Exception as e:
        print(f"\nERROR: Transaction failed - {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
