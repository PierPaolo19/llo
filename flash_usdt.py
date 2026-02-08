#!/usr/bin/env python3
"""
Flash USDT Multi-Network Script
Supports: ERC20 (Ethereum), BEP20 (BSC), TRC20 (TRON)
Compatible with: MetaMask, Trust Wallet, Binance Wallet, Web3
"""

import json
import time
from decimal import Decimal
from typing import Dict, Optional, Union
from web3 import Web3
try:
    from web3.middleware import geth_poa_middleware
except ImportError:
    # For newer versions of web3.py
    from web3.middleware import ExtraDataToPOAMiddleware as geth_poa_middleware
from tronpy import Tron
from tronpy.keys import PrivateKey


class NetworkConfig:
    """Network configuration for different chains"""
    
    ETHEREUM_MAINNET = {
        'name': 'Ethereum',
        'chain_id': 1,
        'rpc_url': 'https://eth.llamarpc.com',
        'usdt_contract': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
        'decimals': 6,
        'network_type': 'ERC20'
    }
    
    BSC_MAINNET = {
        'name': 'Binance Smart Chain',
        'chain_id': 56,
        'rpc_url': 'https://bsc-dataseed.binance.org',
        'usdt_contract': '0x55d398326f99059fF775485246999027B3197955',
        'decimals': 18,
        'network_type': 'BEP20'
    }
    
    TRON_MAINNET = {
        'name': 'TRON',
        'usdt_contract': 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t',
        'decimals': 6,
        'network_type': 'TRC20'
    }


class USDTWallet:
    """USDT Wallet Manager for multiple networks"""
    
    def __init__(self, private_key: str, network: str = 'ethereum'):
        """
        Initialize wallet with private key
        
        Args:
            private_key: Private key for the wallet
            network: Network to use ('ethereum', 'bsc', 'tron')
        """
        self.private_key = private_key
        self.network = network.lower()
        self.web3 = None
        self.tron = None
        self.account = None
        
        if self.network in ['ethereum', 'bsc']:
            self._init_web3()
        elif self.network == 'tron':
            self._init_tron()
        else:
            raise ValueError(f"Unsupported network: {network}")
    
    def _init_web3(self):
        """Initialize Web3 connection"""
        if self.network == 'ethereum':
            config = NetworkConfig.ETHEREUM_MAINNET
        elif self.network == 'bsc':
            config = NetworkConfig.BSC_MAINNET
        else:
            raise ValueError(f"Invalid network for Web3: {self.network}")
        
        self.web3 = Web3(Web3.HTTPProvider(config['rpc_url']))
        
        # Add PoA middleware for BSC
        if self.network == 'bsc':
            self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Create account from private key
        if self.private_key.startswith('0x'):
            self.account = self.web3.eth.account.from_key(self.private_key)
        else:
            self.account = self.web3.eth.account.from_key('0x' + self.private_key)
        
        self.config = config
        
        # ERC20/BEP20 ABI (simplified)
        self.usdt_abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {"name": "_to", "type": "address"},
                    {"name": "_value", "type": "uint256"}
                ],
                "name": "transfer",
                "outputs": [{"name": "", "type": "bool"}],
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [{"name": "", "type": "uint8"}],
                "type": "function"
            }
        ]
        
        self.usdt_contract = self.web3.eth.contract(
            address=Web3.to_checksum_address(config['usdt_contract']),
            abi=self.usdt_abi
        )
    
    def _init_tron(self):
        """Initialize TRON connection"""
        self.tron = Tron(network='mainnet')
        self.config = NetworkConfig.TRON_MAINNET
        
        # Initialize account from private key
        if self.private_key.startswith('0x'):
            self.private_key = self.private_key[2:]
        
        self.tron_key = PrivateKey(bytes.fromhex(self.private_key))
        self.account = self.tron_key.public_key.to_base58check_address()
    
    def get_balance(self) -> Decimal:
        """
        Get USDT balance for the wallet
        
        Returns:
            Balance in USDT
        """
        if self.network in ['ethereum', 'bsc']:
            balance_wei = self.usdt_contract.functions.balanceOf(
                self.account.address
            ).call()
            balance = Decimal(balance_wei) / Decimal(10 ** self.config['decimals'])
            return balance
        
        elif self.network == 'tron':
            contract = self.tron.get_contract(self.config['usdt_contract'])
            balance_raw = contract.functions.balanceOf(self.account)
            balance = Decimal(balance_raw) / Decimal(10 ** self.config['decimals'])
            return balance
        
        return Decimal(0)
    
    def get_native_balance(self) -> Decimal:
        """
        Get native token balance (ETH, BNB, or TRX)
        
        Returns:
            Balance in native token
        """
        if self.network in ['ethereum', 'bsc']:
            balance_wei = self.web3.eth.get_balance(self.account.address)
            balance = Decimal(balance_wei) / Decimal(10 ** 18)
            return balance
        
        elif self.network == 'tron':
            account_info = self.tron.get_account(self.account)
            balance_sun = account_info.get('balance', 0)
            balance = Decimal(balance_sun) / Decimal(10 ** 6)
            return balance
        
        return Decimal(0)
    
    def transfer_usdt(self, to_address: str, amount: Union[int, float, Decimal]) -> Dict:
        """
        Transfer USDT to another address
        
        Args:
            to_address: Recipient address
            amount: Amount in USDT
            
        Returns:
            Transaction details
        """
        amount = Decimal(str(amount))
        
        if self.network in ['ethereum', 'bsc']:
            return self._transfer_erc20(to_address, amount)
        elif self.network == 'tron':
            return self._transfer_trc20(to_address, amount)
    
    def _transfer_erc20(self, to_address: str, amount: Decimal) -> Dict:
        """Transfer ERC20/BEP20 USDT"""
        amount_wei = int(amount * Decimal(10 ** self.config['decimals']))
        
        # Build transaction
        transaction = self.usdt_contract.functions.transfer(
            Web3.to_checksum_address(to_address),
            amount_wei
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': 100000,
            'gasPrice': self.web3.eth.gas_price,
        })
        
        # Sign transaction
        signed_txn = self.web3.eth.account.sign_transaction(
            transaction, 
            private_key=self.private_key
        )
        
        # Send transaction
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        return {
            'tx_hash': tx_hash.hex(),
            'network': self.network,
            'amount': str(amount),
            'to': to_address,
            'status': 'pending'
        }
    
    def _transfer_trc20(self, to_address: str, amount: Decimal) -> Dict:
        """Transfer TRC20 USDT"""
        amount_sun = int(amount * Decimal(10 ** self.config['decimals']))
        
        contract = self.tron.get_contract(self.config['usdt_contract'])
        
        # Build and sign transaction
        txn = (
            contract.functions.transfer(to_address, amount_sun)
            .with_owner(self.account)
            .fee_limit(50_000_000)
            .build()
            .sign(self.tron_key)
        )
        
        # Broadcast transaction
        result = txn.broadcast()
        
        return {
            'tx_hash': result.get('txid', ''),
            'network': self.network,
            'amount': str(amount),
            'to': to_address,
            'status': 'pending'
        }
    
    def get_transaction_status(self, tx_hash: str) -> str:
        """
        Check transaction status
        
        Args:
            tx_hash: Transaction hash
            
        Returns:
            Status string
        """
        if self.network in ['ethereum', 'bsc']:
            try:
                receipt = self.web3.eth.get_transaction_receipt(tx_hash)
                return 'success' if receipt['status'] == 1 else 'failed'
            except Exception:
                return 'pending'
        
        elif self.network == 'tron':
            try:
                tx_info = self.tron.get_transaction(tx_hash)
                return tx_info.get('ret', [{}])[0].get('contractRet', 'PENDING')
            except Exception:
                return 'pending'
        
        return 'unknown'
    
    def get_address(self) -> str:
        """Get wallet address"""
        if self.network in ['ethereum', 'bsc']:
            return self.account.address
        elif self.network == 'tron':
            return self.account
        return ''


class FlashUSDT:
    """Main Flash USDT interface supporting multiple wallets and networks"""
    
    def __init__(self):
        self.wallets: Dict[str, USDTWallet] = {}
    
    def add_wallet(self, name: str, private_key: str, network: str):
        """
        Add a wallet to manage
        
        Args:
            name: Wallet identifier
            private_key: Private key
            network: Network ('ethereum', 'bsc', 'tron')
        """
        self.wallets[name] = USDTWallet(private_key, network)
    
    def get_wallet(self, name: str) -> Optional[USDTWallet]:
        """Get wallet by name"""
        return self.wallets.get(name)
    
    def get_all_balances(self) -> Dict:
        """Get balances for all wallets"""
        balances = {}
        for name, wallet in self.wallets.items():
            balances[name] = {
                'address': wallet.get_address(),
                'network': wallet.network,
                'usdt_balance': str(wallet.get_balance()),
                'native_balance': str(wallet.get_native_balance())
            }
        return balances
    
    def cross_chain_info(self) -> Dict:
        """Get information about supported networks"""
        return {
            'ethereum': {
                'network': NetworkConfig.ETHEREUM_MAINNET['name'],
                'type': NetworkConfig.ETHEREUM_MAINNET['network_type'],
                'contract': NetworkConfig.ETHEREUM_MAINNET['usdt_contract'],
                'compatible_wallets': ['MetaMask', 'Trust Wallet', 'Binance Wallet']
            },
            'bsc': {
                'network': NetworkConfig.BSC_MAINNET['name'],
                'type': NetworkConfig.BSC_MAINNET['network_type'],
                'contract': NetworkConfig.BSC_MAINNET['usdt_contract'],
                'compatible_wallets': ['MetaMask', 'Trust Wallet', 'Binance Wallet']
            },
            'tron': {
                'network': NetworkConfig.TRON_MAINNET['name'],
                'type': NetworkConfig.TRON_MAINNET['network_type'],
                'contract': NetworkConfig.TRON_MAINNET['usdt_contract'],
                'compatible_wallets': ['TronLink', 'Trust Wallet', 'Binance Wallet']
            }
        }


def main():
    """Example usage"""
    print("=" * 60)
    print("Flash USDT Multi-Network Script")
    print("Supports: ERC20, BEP20, TRC20")
    print("=" * 60)
    print()
    
    # Initialize Flash USDT manager
    flash_usdt = FlashUSDT()
    
    # Display supported networks
    print("Supported Networks:")
    print("-" * 60)
    networks = flash_usdt.cross_chain_info()
    for key, info in networks.items():
        print(f"\n{info['network']} ({info['type']}):")
        print(f"  Contract: {info['contract']}")
        print(f"  Wallets: {', '.join(info['compatible_wallets'])}")
    
    print("\n" + "=" * 60)
    print("\nTo use this script programmatically:")
    print("-" * 60)
    print("""
# Example 1: Create wallet and check balance
from flash_usdt import FlashUSDT

flash = FlashUSDT()
flash.add_wallet('my_eth_wallet', 'YOUR_PRIVATE_KEY', 'ethereum')
wallet = flash.get_wallet('my_eth_wallet')
balance = wallet.get_balance()
print(f"USDT Balance: {balance}")

# Example 2: Transfer USDT
wallet.transfer_usdt('RECIPIENT_ADDRESS', 10.5)

# Example 3: Check all balances
balances = flash.get_all_balances()
print(balances)
    """)
    
    print("\n" + "=" * 60)
    print("SECURITY WARNING:")
    print("-" * 60)
    print("- NEVER share your private keys")
    print("- Store private keys securely (use environment variables)")
    print("- Test with small amounts first")
    print("- Verify recipient addresses carefully")
    print("=" * 60)


if __name__ == '__main__':
    main()
