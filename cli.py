#!/usr/bin/env python3
"""
Simple command-line interface for quick balance checks
Usage: python3 cli.py <network> <address>
Example: python3 cli.py ethereum 0x5754284f345afc66a98fbB0a0Afe71e0F007B949
"""

import sys
from flash_usdt import USDTFlashTool, WEB3_AVAILABLE, TRONPY_AVAILABLE


def print_usage():
    """Print usage information"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║           USDT Balance Checker - Command Line Tool               ║
╚═══════════════════════════════════════════════════════════════════╝

Usage:
    python3 cli.py <network> <address>

Networks:
    ethereum    - Ethereum network (ERC20)
    bsc         - Binance Smart Chain (BEP20)
    tron        - TRON network (TRC20)

Examples:
    python3 cli.py ethereum 0x5754284f345afc66a98fbB0a0Afe71e0F007B949
    python3 cli.py bsc 0x8894E0a0c962CB723c1976a4421c95949bE2D4E3
    python3 cli.py tron TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE

Options:
    --help, -h  Show this help message
    --info      Show token information instead of balance
""")


def main():
    """Main CLI entry point"""
    # Check for help flag
    if len(sys.argv) == 1 or '--help' in sys.argv or '-h' in sys.argv:
        print_usage()
        return
    
    # Check dependencies
    if not WEB3_AVAILABLE and not TRONPY_AVAILABLE:
        print("ERROR: No blockchain libraries installed!")
        print("Please run: pip install web3 tronpy")
        sys.exit(1)
    
    # Parse arguments
    if len(sys.argv) < 3:
        print("ERROR: Missing arguments")
        print_usage()
        sys.exit(1)
    
    network = sys.argv[1].lower()
    
    # Check for --info flag
    show_info = '--info' in sys.argv
    
    if show_info:
        # Show token info
        tool = USDTFlashTool()
        
        print(f"\n{'='*60}")
        print(f"Connecting to {network}...")
        print(f"{'='*60}\n")
        
        if tool.connect_to_network(network):
            info = tool.get_token_info(network)
            if info:
                print(f"Network: {info['network']}")
                print(f"Token Name: {info['name']}")
                print(f"Symbol: {info['symbol']}")
                print(f"Decimals: {info['decimals']}")
                print(f"Type: {info['type']}")
                print(f"Contract: {info['contract']}")
                print(f"\n{'='*60}\n")
            else:
                print("Failed to retrieve token information")
                sys.exit(1)
        else:
            print(f"Failed to connect to {network}")
            sys.exit(1)
    else:
        # Check balance
        address = sys.argv[2]
        
        tool = USDTFlashTool()
        
        print(f"\n{'='*60}")
        print(f"Checking USDT Balance")
        print(f"{'='*60}")
        print(f"Network: {network}")
        print(f"Address: {address}")
        print(f"{'='*60}\n")
        
        # Connect to network
        if not tool.connect_to_network(network):
            print(f"\n✗ Failed to connect to {network}")
            sys.exit(1)
        
        # Get balance
        balance = tool.get_balance(network, address)
        
        if balance is not None:
            print(f"\n{'='*60}")
            print(f"💰 Balance: {balance:.6f} USDT")
            print(f"{'='*60}\n")
        else:
            print("\n✗ Failed to retrieve balance")
            sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Exiting...\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error: {str(e)}\n")
        sys.exit(1)
