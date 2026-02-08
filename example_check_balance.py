#!/usr/bin/env python3
"""
Example 1: Check USDT Balance on Multiple Networks
"""

import os
from flash_usdt import FlashUSDT


def main():
    # Initialize Flash USDT
    flash = FlashUSDT()
    
    # Example: Add wallets (replace with your actual private keys)
    # You can use environment variables for security
    
    # Ethereum wallet
    eth_key = os.getenv('ETH_PRIVATE_KEY', 'your_eth_private_key_here')
    flash.add_wallet('ethereum_wallet', eth_key, 'ethereum')
    
    # BSC wallet
    bsc_key = os.getenv('BSC_PRIVATE_KEY', 'your_bsc_private_key_here')
    flash.add_wallet('bsc_wallet', bsc_key, 'bsc')
    
    # TRON wallet
    tron_key = os.getenv('TRON_PRIVATE_KEY', 'your_tron_private_key_here')
    flash.add_wallet('tron_wallet', tron_key, 'tron')
    
    # Get all balances
    print("=" * 70)
    print("USDT Balance Check - All Networks")
    print("=" * 70)
    
    balances = flash.get_all_balances()
    
    total_usdt = 0
    
    for wallet_name, info in balances.items():
        print(f"\n{wallet_name.upper()}")
        print("-" * 70)
        print(f"Network:        {info['network'].upper()}")
        print(f"Address:        {info['address']}")
        print(f"USDT Balance:   {info['usdt_balance']} USDT")
        print(f"Native Balance: {info['native_balance']} {'ETH' if info['network'] == 'ethereum' else 'BNB' if info['network'] == 'bsc' else 'TRX'}")
        
        try:
            total_usdt += float(info['usdt_balance'])
        except (ValueError, TypeError):
            pass
    
    print("\n" + "=" * 70)
    print(f"TOTAL USDT ACROSS ALL NETWORKS: {total_usdt:.2f} USDT")
    print("=" * 70)


if __name__ == '__main__':
    main()
