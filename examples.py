#!/usr/bin/env python3
"""
Example usage of the Multi-Network USDT Tool
This script demonstrates programmatic usage of the USDTFlashTool class
"""

from flash_usdt import USDTFlashTool, NetworkConfig

def example_check_balances():
    """Example: Check balances across multiple networks"""
    print("\n" + "="*70)
    print("Example 1: Checking Balances Across Networks")
    print("="*70)
    
    # Initialize the tool
    tool = USDTFlashTool()
    
    # Example addresses (public wallet addresses for demonstration only)
    # Note: These are real addresses on the blockchain. Balances may vary over time.
    test_addresses = {
        'ethereum': '0x5754284f345afc66a98fbB0a0Afe71e0F007B949',  # Bitfinex hot wallet
        'bsc': '0x8894E0a0c962CB723c1976a4421c95949bE2D4E3',       # Example BSC address
        'tron': 'TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE'              # Example TRON address
    }
    
    # Connect to networks and check balances
    for network, address in test_addresses.items():
        print(f"\n--- {network.upper()} ---")
        
        # Connect to network
        if tool.connect_to_network(network):
            # Get balance
            balance = tool.get_balance(network, address)
            if balance is not None:
                print(f"Address: {address}")
                print(f"Balance: {balance:.6f} USDT")
        
        print()


def example_get_token_info():
    """Example: Get token information for all networks"""
    print("\n" + "="*70)
    print("Example 2: Token Information Across Networks")
    print("="*70)
    
    tool = USDTFlashTool()
    
    networks = ['ethereum', 'bsc', 'tron']
    
    for network in networks:
        print(f"\n--- {network.upper()} ---")
        
        # Connect to network
        if tool.connect_to_network(network):
            # Get token info
            info = tool.get_token_info(network)
            if info:
                print(f"Name: {info['name']}")
                print(f"Symbol: {info['symbol']}")
                print(f"Decimals: {info['decimals']}")
                print(f"Type: {info['type']}")
                print(f"Contract: {info['contract']}")


def example_network_info():
    """Example: Display network configuration"""
    print("\n" + "="*70)
    print("Example 3: Network Configuration")
    print("="*70)
    
    tool = USDTFlashTool()
    tool.display_network_info()


def main():
    """Run all examples"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║            Multi-Network USDT Tool - Usage Examples               ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    # Run examples
    example_check_balances()
    input("\nPress Enter to continue to next example...")
    
    example_get_token_info()
    input("\nPress Enter to continue to next example...")
    
    example_network_info()
    
    print("\n" + "="*70)
    print("Examples completed!")
    print("="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting examples... Goodbye!\n")
    except Exception as e:
        print(f"\nError running examples: {str(e)}")
