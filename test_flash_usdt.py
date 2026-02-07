#!/usr/bin/env python3
"""
Unit tests for Flash USDT script.
"""

import unittest
from flash_usdt import FlashUSDT, SUPPORTED_NETWORKS, SUPPORTED_WALLETS


class TestFlashUSDT(unittest.TestCase):
    """Test cases for FlashUSDT class."""
    
    def test_initial_balance(self):
        """Test initial balance is set correctly."""
        flash_usdt = FlashUSDT(initial_balance=100.0)
        self.assertEqual(flash_usdt.check_balance(), 100.0)
    
    def test_default_network(self):
        """Test that default network is ERC20."""
        flash_usdt = FlashUSDT(initial_balance=0.0)
        self.assertEqual(flash_usdt.network, "ERC20")
    
    def test_default_wallet_is_none(self):
        """Test that default wallet is None."""
        flash_usdt = FlashUSDT(initial_balance=0.0)
        self.assertIsNone(flash_usdt.wallet)
    
    def test_network_selection(self):
        """Test network selection for all supported networks."""
        for network in SUPPORTED_NETWORKS.keys():
            flash_usdt = FlashUSDT(initial_balance=0.0, network=network)
            self.assertEqual(flash_usdt.network, network)
    
    def test_wallet_selection(self):
        """Test wallet selection for all supported wallets."""
        for wallet in SUPPORTED_WALLETS.keys():
            # Get a compatible network for the wallet
            network = SUPPORTED_WALLETS[wallet]["supported_networks"][0]
            flash_usdt = FlashUSDT(initial_balance=0.0, network=network, wallet=wallet)
            self.assertEqual(flash_usdt.wallet, wallet)
    
    def test_invalid_network_raises_error(self):
        """Test that invalid network raises ValueError."""
        with self.assertRaises(ValueError):
            FlashUSDT(initial_balance=0.0, network="INVALID")
    
    def test_invalid_wallet_raises_error(self):
        """Test that invalid wallet raises ValueError."""
        with self.assertRaises(ValueError):
            FlashUSDT(initial_balance=0.0, network="ERC20", wallet="invalid_wallet")
    
    def test_wallet_network_compatibility_metamask_trc20(self):
        """Test that MetaMask cannot be used with TRC20."""
        with self.assertRaises(ValueError) as context:
            FlashUSDT(initial_balance=0.0, network="TRC20", wallet="metamask")
        self.assertIn("does not support TRC20", str(context.exception))
    
    def test_wallet_network_compatibility_binance_all_networks(self):
        """Test that Binance Wallet supports all networks."""
        for network in ["TRC20", "ERC20", "BEP20"]:
            flash_usdt = FlashUSDT(initial_balance=0.0, network=network, wallet="binance")
            self.assertEqual(flash_usdt.network, network)
            self.assertEqual(flash_usdt.wallet, "binance")
    
    def test_wallet_network_compatibility_trust_all_networks(self):
        """Test that Trust Wallet supports all networks."""
        for network in ["TRC20", "ERC20", "BEP20"]:
            flash_usdt = FlashUSDT(initial_balance=0.0, network=network, wallet="trust")
            self.assertEqual(flash_usdt.network, network)
            self.assertEqual(flash_usdt.wallet, "trust")
    
    def test_wallet_network_compatibility_metamask_erc20_bep20(self):
        """Test that MetaMask supports ERC20 and BEP20 only."""
        for network in ["ERC20", "BEP20"]:
            flash_usdt = FlashUSDT(initial_balance=0.0, network=network, wallet="metamask")
            self.assertEqual(flash_usdt.network, network)
            self.assertEqual(flash_usdt.wallet, "metamask")
    
    def test_get_network_info(self):
        """Test network info retrieval."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="TRC20")
        network_info = flash_usdt.get_network_info()
        self.assertEqual(network_info['network'], "TRC20")
        self.assertEqual(network_info['name'], "TRON (TRC20)")
        self.assertIn('explorer', network_info)
    
    def test_get_network_info_with_wallet(self):
        """Test network info includes wallet when set."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="ERC20", wallet="metamask")
        network_info = flash_usdt.get_network_info()
        self.assertEqual(network_info['wallet'], "MetaMask")
    
    def test_get_wallet_info(self):
        """Test wallet info retrieval."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="ERC20", wallet="trust")
        wallet_info = flash_usdt.get_wallet_info()
        self.assertIsNotNone(wallet_info)
        self.assertEqual(wallet_info['wallet'], "trust")
        self.assertEqual(wallet_info['name'], "Trust Wallet")
        self.assertIn('description', wallet_info)
        self.assertIn('supported_networks', wallet_info)
    
    def test_get_wallet_info_when_none(self):
        """Test wallet info returns None when no wallet set."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="ERC20")
        wallet_info = flash_usdt.get_wallet_info()
        self.assertIsNone(wallet_info)
    
    def test_transaction_includes_network(self):
        """Test that transactions include network information."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="BEP20")
        tx = flash_usdt.flash(100.0)
        self.assertEqual(tx['network'], "BEP20")
        
        tx2 = flash_usdt.transfer(50.0, "0xRecipient")
        self.assertEqual(tx2['network'], "BEP20")
    
    def test_transaction_includes_wallet(self):
        """Test that transactions include wallet information."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="ERC20", wallet="binance")
        tx = flash_usdt.flash(100.0)
        self.assertEqual(tx['wallet'], "binance")
        
        tx2 = flash_usdt.transfer(50.0, "0xRecipient")
        self.assertEqual(tx2['wallet'], "binance")
    
    def test_transaction_wallet_is_none_when_not_set(self):
        """Test that wallet is None in transactions when not set."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="ERC20")
        tx = flash_usdt.flash(100.0)
        self.assertIsNone(tx['wallet'])
    
    def test_trc20_tx_hash_format(self):
        """Test that TRC20 transaction hashes don't have 0x prefix."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="TRC20")
        tx = flash_usdt.flash(100.0)
        self.assertIn('tx_hash', tx)
        self.assertFalse(tx['tx_hash'].startswith('0x'))
        self.assertEqual(len(tx['tx_hash']), 64)  # 64 hex chars without 0x
    
    def test_erc20_tx_hash_format(self):
        """Test that ERC20 transaction hashes have 0x prefix."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="ERC20")
        tx = flash_usdt.flash(100.0)
        self.assertIn('tx_hash', tx)
        self.assertTrue(tx['tx_hash'].startswith('0x'))
        self.assertEqual(len(tx['tx_hash']), 66)  # 0x + 64 hex chars
    
    def test_bep20_tx_hash_format(self):
        """Test that BEP20 transaction hashes have 0x prefix."""
        flash_usdt = FlashUSDT(initial_balance=0.0, network="BEP20")
        tx = flash_usdt.flash(100.0)
        self.assertIn('tx_hash', tx)
        self.assertTrue(tx['tx_hash'].startswith('0x'))
        self.assertEqual(len(tx['tx_hash']), 66)  # 0x + 64 hex chars
    
    def test_flash_adds_balance(self):
        """Test that flash adds to balance."""
        flash_usdt = FlashUSDT(initial_balance=0.0)
        tx = flash_usdt.flash(100.0)
        self.assertEqual(flash_usdt.check_balance(), 100.0)
        self.assertEqual(tx['amount'], 100.0)
        self.assertEqual(tx['type'], 'flash')
    
    def test_flash_negative_amount_raises_error(self):
        """Test that flashing negative amount raises ValueError."""
        flash_usdt = FlashUSDT(initial_balance=0.0)
        with self.assertRaises(ValueError):
            flash_usdt.flash(-10.0)
    
    def test_flash_zero_amount_raises_error(self):
        """Test that flashing zero amount raises ValueError."""
        flash_usdt = FlashUSDT(initial_balance=0.0)
        with self.assertRaises(ValueError):
            flash_usdt.flash(0.0)
    
    def test_transfer_reduces_balance(self):
        """Test that transfer reduces balance."""
        flash_usdt = FlashUSDT(initial_balance=100.0)
        tx = flash_usdt.transfer(30.0, "0xRecipient")
        self.assertEqual(flash_usdt.check_balance(), 70.0)
        self.assertEqual(tx['amount'], 30.0)
        self.assertEqual(tx['type'], 'transfer')
        self.assertEqual(tx['recipient'], "0xRecipient")
    
    def test_transfer_insufficient_balance_raises_error(self):
        """Test that transfer with insufficient balance raises ValueError."""
        flash_usdt = FlashUSDT(initial_balance=50.0)
        with self.assertRaises(ValueError):
            flash_usdt.transfer(100.0, "0xRecipient")
    
    def test_transfer_negative_amount_raises_error(self):
        """Test that transferring negative amount raises ValueError."""
        flash_usdt = FlashUSDT(initial_balance=100.0)
        with self.assertRaises(ValueError):
            flash_usdt.transfer(-10.0, "0xRecipient")
    
    def test_transaction_history(self):
        """Test that transaction history is recorded correctly."""
        flash_usdt = FlashUSDT(initial_balance=0.0)
        flash_usdt.flash(100.0)
        flash_usdt.transfer(30.0, "0xRecipient")
        
        transactions = flash_usdt.get_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]['type'], 'flash')
        self.assertEqual(transactions[1]['type'], 'transfer')
    
    def test_tx_hash_generation(self):
        """Test that transaction hashes are generated."""
        flash_usdt = FlashUSDT(initial_balance=0.0)
        tx = flash_usdt.flash(100.0)
        self.assertIn('tx_hash', tx)
        self.assertTrue(tx['tx_hash'].startswith('0x'))
        self.assertEqual(len(tx['tx_hash']), 66)  # 0x + 64 hex chars
    
    def test_multiple_operations(self):
        """Test multiple operations in sequence."""
        flash_usdt = FlashUSDT(initial_balance=10.0)
        flash_usdt.flash(100.0)
        self.assertEqual(flash_usdt.check_balance(), 110.0)
        
        flash_usdt.transfer(20.0, "0xAddr1")
        self.assertEqual(flash_usdt.check_balance(), 90.0)
        
        flash_usdt.flash(50.0)
        self.assertEqual(flash_usdt.check_balance(), 140.0)
        
        flash_usdt.transfer(40.0, "0xAddr2")
        self.assertEqual(flash_usdt.check_balance(), 100.0)
        
        transactions = flash_usdt.get_transactions()
        self.assertEqual(len(transactions), 4)


if __name__ == '__main__':
    unittest.main()
