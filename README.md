# Multi-Network USDT Tool 🚀

A Python-based educational tool for interacting with USDT (Tether) tokens across multiple blockchain networks.

## 🌐 Supported Networks

- **Ethereum (ERC20)** - USDT on Ethereum Mainnet
- **Binance Smart Chain (BEP20)** - USDT on BSC
- **TRON (TRC20)** - USDT on TRON Network

## 💼 Compatible Wallets

This tool can check balances for addresses from:
- **MetaMask** - Popular browser extension wallet
- **Trust Wallet** - Mobile crypto wallet
- **Binance Wallet** - Binance's official wallet
- **Any Web3-compatible wallet** - Supporting the respective blockchain

## ⚡ Features

- ✅ Check USDT balances across multiple networks
- ✅ View token information (name, symbol, decimals, contract address)
- ✅ Display network and contract information
- ✅ Support for ERC20, BEP20, and TRC20 standards
- ✅ Easy-to-use interactive menu
- ✅ Read-only operations (no transaction signing)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Internet connection

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PierPaolo19/llo.git
   cd llo
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Basic Usage

Run the script:
```bash
python3 flash_usdt.py
```

### Interactive Menu

The tool provides an interactive menu with the following options:

1. **Check USDT Balance** - Query balance for any wallet address
2. **View Token Information** - Get details about USDT contract on each network
3. **Display Network Information** - Show all supported networks and their contracts
4. **Connect to All Networks** - Test connections to all blockchain networks
5. **Exit** - Close the application

### Example: Checking a Balance

```
1. Select option 1 (Check USDT Balance)
2. Choose network: ethereum, bsc, or tron
3. Enter wallet address
4. View the balance
```

### Example Wallet Addresses (for testing)

You can check any public wallet address. Here are some examples:

**Ethereum (ERC20):**
```
Network: ethereum
Address: 0x5754284f345afc66a98fbB0a0Afe71e0F007B949
```

**Binance Smart Chain (BEP20):**
```
Network: bsc
Address: 0x8894E0a0c962CB723c1976a4421c95949bE2D4E3
```

**TRON (TRC20):**
```
Network: tron
Address: TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE
```

## 📊 Network Details

### Ethereum (ERC20)
- **Chain ID:** 1
- **USDT Contract:** `0xdAC17F958D2ee523a2206206994597C13D831ec7`
- **Explorer:** https://etherscan.io
- **RPC:** Public Ethereum RPC endpoint

### Binance Smart Chain (BEP20)
- **Chain ID:** 56
- **USDT Contract:** `0x55d398326f99059fF775485246999027B3197955`
- **Explorer:** https://bscscan.com
- **RPC:** https://bsc-dataseed.binance.org/

### TRON (TRC20)
- **USDT Contract:** `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t`
- **Explorer:** https://tronscan.org
- **RPC:** https://api.trongrid.io

## 🔒 Security & Disclaimer

### ⚠️ IMPORTANT WARNINGS

- **Educational Purpose Only:** This tool is designed for learning and demonstration purposes
- **Read-Only Operations:** This script only reads blockchain data and does not perform transactions
- **No Private Keys Required:** Never enter private keys or seed phrases
- **Verify Addresses:** Always double-check wallet addresses before querying
- **No Guarantees:** Use at your own risk

### 🛡️ Best Practices

1. **Never share private keys** - This tool doesn't need them
2. **Verify contract addresses** - Always check on official explorers
3. **Use public addresses only** - Only query addresses you own or are publicly known
4. **Keep software updated** - Regularly update dependencies for security patches

## 🐛 Troubleshooting

### Connection Issues

If you can't connect to a network:
- Check your internet connection
- Try again later (RPC endpoints may be temporarily unavailable)
- Consider using a custom RPC endpoint in `.env` file

### Missing Dependencies

If you get import errors:
```bash
pip install --upgrade web3 tronpy python-dotenv
```

### TRC20 Support Disabled

If you see "TRC20 support disabled":
```bash
pip install tronpy
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is provided as-is for educational purposes. See the repository for any license information.

## 🔗 Useful Links

- [Web3.py Documentation](https://web3py.readthedocs.io/)
- [TronPy Documentation](https://tronpy.readthedocs.io/)
- [Ethereum Documentation](https://ethereum.org/en/developers/docs/)
- [BSC Documentation](https://docs.bnbchain.org/)
- [TRON Documentation](https://developers.tron.network/)

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Remember:** Always DYOR (Do Your Own Research) and never trust unverified sources with your private keys or funds. Stay safe! 🔒