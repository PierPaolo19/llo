#!/usr/bin/env python3
"""
Unit tests for Flash USDT script.
"""

import unittest
from flash_usdt import FlashUSDT


class TestFlashUSDT(unittest.TestCase):
    """Test cases for FlashUSDT class."""
    
    def test_initial_balance(self):
        """Test initial balance is set correctly."""
        flash_usdt = FlashUSDT(initial_balance=100.0)
        self.assertEqual(flash_usdt.check_balance(), 100.0)
    
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
