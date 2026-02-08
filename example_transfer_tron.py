#!/usr/bin/env python3
"""
Example 4: Transfer USDT on TRON Network
"""

import os
import sys
from flash_usdt import FlashUSDT


def main():
    # Check arguments
    if len(sys.argv) < 3:
        print("Usage: python example_transfer_tron.py <recipient_address> <amount>")
        print("Example: python example_transfer_tron.py TLPcjEz5Zsrzpxr3jJvBHZYBU9VLYVJfPw 10.5")
        sys.exit(1)
    
    recipient = sys.argv[1]
    amount = float(sys.argv[2])
    
    # Initialize
    flash = FlashUSDT()
    
    # Get private key from environment variable
    private_key = os.getenv('TRON_PRIVATE_KEY')
    
    if not private_key:
        print("ERROR: TRON_PRIVATE_KEY environment variable not set")
        sys.exit(1)
    
    # Add TRON wallet
    flash.add_wallet('sender', private_key, 'tron')
    wallet = flash.get_wallet('sender')
    
    # Display info
    print("=" * 70)
    print("USDT Transfer - TRON Network (TRC20)")
    print("=" * 70)
    print(f"\nFrom Address: {wallet.get_address()}")
    print(f"To Address:   {recipient}")
    print(f"Amount:       {amount} USDT")
    
    # Check balances
    usdt_balance = wallet.get_balance()
    trx_balance = wallet.get_native_balance()
    
    print(f"\nCurrent USDT Balance: {usdt_balance} USDT")
    print(f"Current TRX Balance:  {trx_balance} TRX")
    
    if float(usdt_balance) < amount:
        print("\nERROR: Insufficient USDT balance!")
        sys.exit(1)
    
    if float(trx_balance) < 10:
        print("\nWARNING: Low TRX balance for transaction fees.")
    
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
        print(f"View on TronScan:")
        print(f"https://tronscan.org/#/transaction/{tx_details['tx_hash']}")
        print("=" * 70)
        
    except Exception as e:
        print(f"\nERROR: Transaction failed - {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
