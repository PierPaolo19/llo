#!/usr/bin/env python3
"""
Multi-Network USDT Token Interaction Script
Supports: ERC20 (Ethereum), TRC20 (TRON), BEP20 (Binance Smart Chain)

EDUCATIONAL PURPOSE ONLY
This script demonstrates how to interact with USDT tokens across different blockchain networks.
"""

import json
import sys
from typing import Dict, Optional
from decimal import Decimal

try:
    from web3 import Web3
    try:
        # Try newer import path (web3.py 6.0+)
        from web3.middleware import ExtraDataToPOAMiddleware as poa_middleware
    except ImportError:
        try:
            # Try older import path (web3.py < 6.0)
            from web3.middleware import geth_poa_middleware as poa_middleware
        except ImportError:
            # No PoA middleware available
            poa_middleware = None
    WEB3_AVAILABLE = True
except ImportError:
    Web3 = None
    poa_middleware = None
    WEB3_AVAILABLE = False

try:
    from tronpy import Tron
    from tronpy.keys import PrivateKey
    TRONPY_AVAILABLE = True
except ImportError:
    Tron = None
    TRONPY_AVAILABLE = False


class NetworkConfig:
    """Network configurations for different blockchains"""
    
    # Ethereum Mainnet (ERC20)
    ETHEREUM = {
        'name': 'Ethereum',
        'rpc': 'https://eth.llamarpc.com',
        'chain_id': 1,
        'usdt_contract': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
        'explorer': 'https://etherscan.io',
        'type': 'ERC20'
    }
    
    # Binance Smart Chain (BEP20)
    BSC = {
        'name': 'Binance Smart Chain',
        'rpc': 'https://bsc-dataseed.binance.org/',
        'chain_id': 56,
        'usdt_contract': '0x55d398326f99059fF775485246999027B3197955',
        'explorer': 'https://bscscan.com',
        'type': 'BEP20'
    }
    
    # TRON Network (TRC20)
    TRON = {
        'name': 'TRON',
        'rpc': 'https://api.trongrid.io',
        'usdt_contract': 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t',
        'explorer': 'https://tronscan.org',
        'type': 'TRC20'
    }
    
    @classmethod
    def get_all_networks(cls):
        """Get all available networks"""
        return {
            'ethereum': cls.ETHEREUM,
            'bsc': cls.BSC,
            'tron': cls.TRON
        }


class USDTFlashTool:
    """Multi-network USDT interaction tool"""
    
    # ERC20/BEP20 Standard ABI (simplified)
    ERC20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
    
    def __init__(self):
        """Initialize the USDT Flash Tool"""
        self.networks = NetworkConfig.get_all_networks()
        self.web3_instances = {}
        self.tron_instance = None
        
    def connect_to_network(self, network: str) -> bool:
        """
        Connect to a specific blockchain network
        
        Args:
            network: Network name ('ethereum', 'bsc', 'tron')
            
        Returns:
            bool: True if connection successful
        """
        if network not in self.networks:
            print(f"Error: Unknown network '{network}'")
            return False
            
        config = self.networks[network]
        
        try:
            if config['type'] in ['ERC20', 'BEP20']:
                # Check if web3 is available
                if not WEB3_AVAILABLE or Web3 is None:
                    print(f"✗ {config['type']} support not available (web3 not installed)")
                    return False
                
                # Connect to EVM-compatible networks
                w3 = Web3(Web3.HTTPProvider(config['rpc']))
                
                # Add PoA middleware for BSC if available
                if network == 'bsc' and poa_middleware is not None:
                    try:
                        w3.middleware_onion.inject(poa_middleware, layer=0)
                    except Exception as e:
                        print(f"Warning: Could not inject PoA middleware: {str(e)}")
                
                if w3.is_connected():
                    self.web3_instances[network] = w3
                    print(f"✓ Connected to {config['name']}")
                    return True
                else:
                    print(f"✗ Failed to connect to {config['name']}")
                    return False
                    
            elif config['type'] == 'TRC20':
                # Connect to TRON network
                if not TRONPY_AVAILABLE or Tron is None:
                    print("✗ TRC20 support not available (tronpy not installed)")
                    return False
                    
                self.tron_instance = Tron()
                print(f"✓ Connected to {config['name']}")
                return True
                
        except Exception as e:
            print(f"✗ Error connecting to {config['name']}: {str(e)}")
            return False
            
    def get_balance(self, network: str, address: str) -> Optional[Decimal]:
        """
        Get USDT balance for an address on a specific network
        
        Args:
            network: Network name
            address: Wallet address
            
        Returns:
            Decimal: Balance in USDT, or None if error
        """
        if network not in self.networks:
            print(f"Error: Unknown network '{network}'")
            return None
            
        config = self.networks[network]
        
        try:
            if config['type'] in ['ERC20', 'BEP20']:
                if network not in self.web3_instances:
                    print(f"Error: Not connected to {config['name']}")
                    return None
                
                w3 = self.web3_instances[network]
                
                # Validate address
                if not w3.is_address(address):
                    print(f"Error: Invalid address format for {config['name']}")
                    return None
                
                # Get contract
                contract = w3.eth.contract(
                    address=w3.to_checksum_address(config['usdt_contract']),
                    abi=self.ERC20_ABI
                )
                
                # Get balance
                balance_wei = contract.functions.balanceOf(
                    w3.to_checksum_address(address)
                ).call()
                
                # Get decimals (USDT uses 6 decimals on most networks)
                decimals = contract.functions.decimals().call()
                balance = Decimal(balance_wei) / Decimal(10 ** decimals)
                
                return balance
                
            elif config['type'] == 'TRC20':
                if self.tron_instance is None:
                    print("Error: Not connected to TRON")
                    return None
                
                # Get TRC20 contract
                contract = self.tron_instance.get_contract(config['usdt_contract'])
                
                # Get balance
                balance_raw = contract.functions.balanceOf(address)
                decimals = contract.functions.decimals()
                balance = Decimal(balance_raw) / Decimal(10 ** decimals)
                
                return balance
                
        except Exception as e:
            print(f"Error getting balance: {str(e)}")
            return None
            
    def get_token_info(self, network: str) -> Optional[Dict]:
        """
        Get USDT token information on a specific network
        
        Args:
            network: Network name
            
        Returns:
            Dict: Token info (name, symbol, decimals, total supply)
        """
        if network not in self.networks:
            print(f"Error: Unknown network '{network}'")
            return None
            
        config = self.networks[network]
        
        try:
            if config['type'] in ['ERC20', 'BEP20']:
                if network not in self.web3_instances:
                    print(f"Error: Not connected to {config['name']}")
                    return None
                
                w3 = self.web3_instances[network]
                contract = w3.eth.contract(
                    address=w3.to_checksum_address(config['usdt_contract']),
                    abi=self.ERC20_ABI
                )
                
                info = {
                    'name': contract.functions.name().call(),
                    'symbol': contract.functions.symbol().call(),
                    'decimals': contract.functions.decimals().call(),
                    'contract': config['usdt_contract'],
                    'network': config['name'],
                    'type': config['type']
                }
                
                return info
                
            elif config['type'] == 'TRC20':
                if self.tron_instance is None:
                    print("Error: Not connected to TRON")
                    return None
                
                contract = self.tron_instance.get_contract(config['usdt_contract'])
                
                info = {
                    'name': contract.functions.name(),
                    'symbol': contract.functions.symbol(),
                    'decimals': contract.functions.decimals(),
                    'contract': config['usdt_contract'],
                    'network': config['name'],
                    'type': config['type']
                }
                
                return info
                
        except Exception as e:
            print(f"Error getting token info: {str(e)}")
            return None
            
    def display_network_info(self):
        """Display information about all supported networks"""
        print("\n" + "="*70)
        print("SUPPORTED NETWORKS AND USDT CONTRACTS")
        print("="*70)
        
        for network_key, config in self.networks.items():
            print(f"\n{config['name']} ({config['type']}):")
            print(f"  Contract: {config['usdt_contract']}")
            print(f"  Explorer: {config['explorer']}/address/{config['usdt_contract']}")
            print(f"  RPC: {config['rpc']}")


def print_banner():
    """Print application banner"""
    banner = """
╔═══════════════════════════════════════════════════════════════════╗
║                   MULTI-NETWORK USDT TOOL                         ║
║                   Educational Purpose Only                         ║
╚═══════════════════════════════════════════════════════════════════╝

Supported Networks:
  • Ethereum (ERC20)
  • Binance Smart Chain (BEP20)
  • TRON (TRC20)

Supported Wallets:
  • MetaMask
  • Trust Wallet
  • Web3 Compatible Wallets
  • Any wallet supporting the respective network

⚠️  DISCLAIMER:
This tool is for educational purposes only. Always verify transactions
and never share your private keys. Use at your own risk.
"""
    print(banner)


def print_menu():
    """Print main menu"""
    print("\n" + "="*70)
    print("MAIN MENU")
    print("="*70)
    print("1. Check USDT Balance")
    print("2. View Token Information")
    print("3. Display Network Information")
    print("4. Connect to All Networks")
    print("5. Exit")
    print("="*70)


def main():
    """Main application entry point"""
    # Check if dependencies are available
    if not WEB3_AVAILABLE and not TRONPY_AVAILABLE:
        print("ERROR: No blockchain libraries installed!")
        print("\nPlease install the required dependencies:")
        print("  pip install web3 tronpy python-dotenv")
        print("\nOr install from requirements.txt:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    
    if not WEB3_AVAILABLE:
        print("WARNING: web3 not installed. ERC20/BEP20 support disabled.")
        print("To enable: pip install web3\n")
    
    if not TRONPY_AVAILABLE:
        print("WARNING: tronpy not installed. TRC20 support disabled.")
        print("To enable: pip install tronpy\n")
    
    print_banner()
    
    tool = USDTFlashTool()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            # Check balance
            print("\nAvailable networks: ethereum, bsc, tron")
            network = input("Enter network: ").strip().lower()
            address = input("Enter wallet address: ").strip()
            
            if network not in tool.networks:
                print(f"Error: Invalid network '{network}'")
                continue
            
            # Connect if not already connected
            if network not in tool.web3_instances and network != 'tron':
                print(f"\nConnecting to {network}...")
                tool.connect_to_network(network)
            elif network == 'tron' and tool.tron_instance is None:
                print(f"\nConnecting to {network}...")
                tool.connect_to_network(network)
            
            print(f"\nFetching balance...")
            balance = tool.get_balance(network, address)
            
            if balance is not None:
                print(f"\n{'='*50}")
                print(f"Network: {tool.networks[network]['name']}")
                print(f"Address: {address}")
                print(f"USDT Balance: {balance:.6f} USDT")
                print(f"{'='*50}")
                
        elif choice == '2':
            # View token info
            print("\nAvailable networks: ethereum, bsc, tron")
            network = input("Enter network: ").strip().lower()
            
            if network not in tool.networks:
                print(f"Error: Invalid network '{network}'")
                continue
            
            # Connect if not already connected
            if network not in tool.web3_instances and network != 'tron':
                print(f"\nConnecting to {network}...")
                tool.connect_to_network(network)
            elif network == 'tron' and tool.tron_instance is None:
                print(f"\nConnecting to {network}...")
                tool.connect_to_network(network)
            
            print(f"\nFetching token information...")
            info = tool.get_token_info(network)
            
            if info:
                print(f"\n{'='*50}")
                print(f"Token Information - {info['network']}")
                print(f"{'='*50}")
                print(f"Name: {info['name']}")
                print(f"Symbol: {info['symbol']}")
                print(f"Decimals: {info['decimals']}")
                print(f"Type: {info['type']}")
                print(f"Contract: {info['contract']}")
                print(f"{'='*50}")
                
        elif choice == '3':
            # Display network info
            tool.display_network_info()
            
        elif choice == '4':
            # Connect to all networks
            print("\nConnecting to all networks...\n")
            for network in tool.networks.keys():
                tool.connect_to_network(network)
            print("\nConnection attempts completed.")
            
        elif choice == '5':
            # Exit
            print("\nThank you for using Multi-Network USDT Tool!")
            print("Stay safe and verify all transactions! 🔒\n")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting... Goodbye! 👋\n")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        sys.exit(1)
