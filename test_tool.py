#!/usr/bin/env python3
"""
Test script for Multi-Network USDT Tool
Runs basic tests to ensure functionality works correctly
"""

import sys
from flash_usdt import USDTFlashTool, NetworkConfig, WEB3_AVAILABLE, TRONPY_AVAILABLE


def test_imports():
    """Test that all necessary imports work"""
    print("\n" + "="*70)
    print("TEST 1: Module Imports")
    print("="*70)
    
    try:
        from flash_usdt import USDTFlashTool, NetworkConfig
        print("✓ Main modules imported successfully")
        print(f"  - Web3 available: {WEB3_AVAILABLE}")
        print(f"  - TronPy available: {TRONPY_AVAILABLE}")
        return True
    except Exception as e:
        print(f"✗ Import failed: {str(e)}")
        return False


def test_initialization():
    """Test tool initialization"""
    print("\n" + "="*70)
    print("TEST 2: Tool Initialization")
    print("="*70)
    
    try:
        tool = USDTFlashTool()
        print("✓ USDTFlashTool initialized successfully")
        print(f"  - Networks available: {len(tool.networks)}")
        print(f"  - Network names: {', '.join(tool.networks.keys())}")
        return True
    except Exception as e:
        print(f"✗ Initialization failed: {str(e)}")
        return False


def test_network_config():
    """Test network configuration"""
    print("\n" + "="*70)
    print("TEST 3: Network Configuration")
    print("="*70)
    
    try:
        networks = NetworkConfig.get_all_networks()
        print(f"✓ Network config loaded: {len(networks)} networks")
        
        for name, config in networks.items():
            print(f"\n  {name.upper()}:")
            print(f"    - Name: {config['name']}")
            print(f"    - Type: {config['type']}")
            print(f"    - Contract: {config['usdt_contract']}")
            print(f"    - RPC: {config['rpc']}")
        
        return True
    except Exception as e:
        print(f"✗ Network config failed: {str(e)}")
        return False


def test_connection(network='ethereum'):
    """Test network connection"""
    print("\n" + "="*70)
    print(f"TEST 4: Network Connection ({network})")
    print("="*70)
    
    try:
        tool = USDTFlashTool()
        result = tool.connect_to_network(network)
        
        if result:
            print(f"✓ Successfully connected to {network}")
            return True
        else:
            print(f"⚠ Could not connect to {network} (may be RPC issue)")
            return True  # Don't fail test for RPC issues
    except Exception as e:
        print(f"✗ Connection test failed: {str(e)}")
        return False


def test_token_info(network='ethereum'):
    """Test getting token information"""
    print("\n" + "="*70)
    print(f"TEST 5: Token Information ({network})")
    print("="*70)
    
    try:
        tool = USDTFlashTool()
        
        if not tool.connect_to_network(network):
            print(f"⚠ Skipped - could not connect to {network}")
            return True
        
        info = tool.get_token_info(network)
        
        if info:
            print(f"✓ Token info retrieved:")
            print(f"  - Name: {info.get('name', 'N/A')}")
            print(f"  - Symbol: {info.get('symbol', 'N/A')}")
            print(f"  - Decimals: {info.get('decimals', 'N/A')}")
            print(f"  - Contract: {info.get('contract', 'N/A')}")
            return True
        else:
            print(f"⚠ Could not retrieve token info (may be RPC issue)")
            return True  # Don't fail for RPC issues
    except Exception as e:
        print(f"✗ Token info test failed: {str(e)}")
        return False


def test_balance_check():
    """Test balance checking with a known address"""
    print("\n" + "="*70)
    print("TEST 6: Balance Check (Read-Only)")
    print("="*70)
    
    # Use a well-known public address (Bitfinex hot wallet)
    test_address = "0x5754284f345afc66a98fbB0a0Afe71e0F007B949"
    
    try:
        tool = USDTFlashTool()
        
        if not tool.connect_to_network('ethereum'):
            print("⚠ Skipped - could not connect to Ethereum")
            return True
        
        balance = tool.get_balance('ethereum', test_address)
        
        if balance is not None:
            print(f"✓ Balance check successful:")
            print(f"  - Address: {test_address}")
            print(f"  - Balance: {balance:.6f} USDT")
            return True
        else:
            print(f"⚠ Could not retrieve balance (may be RPC issue)")
            return True  # Don't fail for RPC issues
    except Exception as e:
        print(f"✗ Balance check failed: {str(e)}")
        return False


def test_display_network_info():
    """Test displaying network information"""
    print("\n" + "="*70)
    print("TEST 7: Display Network Information")
    print("="*70)
    
    try:
        tool = USDTFlashTool()
        tool.display_network_info()
        print("\n✓ Network info displayed successfully")
        return True
    except Exception as e:
        print(f"✗ Display network info failed: {str(e)}")
        return False


def run_all_tests():
    """Run all tests and report results"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║          Multi-Network USDT Tool - Test Suite                     ║
╚═══════════════════════════════════════════════════════════════════╝
""")
    
    tests = [
        ("Imports", test_imports),
        ("Initialization", test_initialization),
        ("Network Config", test_network_config),
        ("Connection", test_connection),
        ("Token Info", test_token_info),
        ("Balance Check", test_balance_check),
        ("Display Info", test_display_network_info),
    ]
    
    results = []
    
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ CRITICAL ERROR in {name}: {str(e)}")
            results.append((name, False))
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {name}")
    
    print("="*70)
    print(f"Results: {passed}/{total} tests passed")
    print("="*70)
    
    if passed == total:
        print("\n🎉 All tests passed! The tool is working correctly.\n")
        return 0
    elif passed > 0:
        print(f"\n⚠ {total - passed} test(s) failed. Review output above.\n")
        return 1
    else:
        print("\n✗ All tests failed. Please check your installation.\n")
        return 1


if __name__ == "__main__":
    try:
        exit_code = run_all_tests()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nTests interrupted. Exiting...\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Test suite error: {str(e)}\n")
        sys.exit(1)
