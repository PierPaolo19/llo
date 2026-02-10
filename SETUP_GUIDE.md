# Step-by-Step Setup Guide

## Visual Guide: How to Run This Tool from GitHub

### Method 1: Download ZIP (No Git Required) ⭐ EASIEST

#### Step 1: Download the Repository

1. Go to: https://github.com/PierPaolo19/llo
2. Look for the green **"Code"** button (top right of file list)
3. Click on it
4. Click **"Download ZIP"**

```
GitHub Page
┌─────────────────────────────────────┐
│  PierPaolo19 / llo                  │
│                                      │
│  [<> Code ▼]  <- Click here         │
│   ├─ Clone                          │
│   ├─ Open with GitHub Desktop       │
│   └─ Download ZIP  <- Then click    │
└─────────────────────────────────────┘
```

#### Step 2: Extract the ZIP File

1. Locate the downloaded `llo-main.zip` file (usually in Downloads folder)
2. Right-click on it
3. Choose "Extract All..." (Windows) or double-click (Mac)
4. Remember where you extracted it!

#### Step 3: Install Python (if not already installed)

**Windows:**
1. Go to: https://www.python.org/downloads/
2. Download the latest Python 3
3. Run the installer
4. ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation!

**Mac:**
- Python 3 is usually pre-installed. Open Terminal and type: `python3 --version`

**Linux:**
- Python 3 is usually pre-installed. Open Terminal and type: `python3 --version`

#### Step 4: Open Terminal/Command Prompt

**Windows:**
1. Press `Windows Key + R`
2. Type: `cmd`
3. Press Enter

**Mac/Linux:**
1. Press `Cmd + Space` (Mac) or `Ctrl + Alt + T` (Linux)
2. Type: `terminal`
3. Press Enter

#### Step 5: Navigate to the Extracted Folder

```bash
# Windows example:
cd C:\Users\YourName\Downloads\llo-main

# Mac/Linux example:
cd ~/Downloads/llo-main
```

Tip: You can often drag and drop the folder into Terminal to auto-fill the path!

#### Step 6: Install Required Libraries

```bash
# Try this first:
pip install -r requirements.txt

# If that doesn't work, try:
pip3 install -r requirements.txt

# Or install individually:
pip install web3 tronpy python-dotenv
```

Wait for installation to complete (may take 1-2 minutes).

#### Step 7: Run the Tool! 🎉

```bash
# Try this first:
python flash_usdt.py

# If that doesn't work, try:
python3 flash_usdt.py
```

You should see a menu like this:

```
╔═══════════════════════════════════════════════════════════════════╗
║                   MULTI-NETWORK USDT TOOL                         ║
║                   Educational Purpose Only                         ║
╚═══════════════════════════════════════════════════════════════════╝

MAIN MENU
======================================================================
1. Check USDT Balance
2. View Token Information
3. Display Network Information
4. Connect to All Networks
5. Exit
======================================================================

Enter your choice (1-5):
```

### Method 2: Using Git (For Developers)

#### Step 1: Install Git

If you don't have Git:
- Windows: Download from https://git-scm.com/download/win
- Mac: Type `git --version` in Terminal (it will prompt to install if needed)
- Linux: `sudo apt-get install git` or `sudo yum install git`

#### Step 2: Clone the Repository

```bash
git clone https://github.com/PierPaolo19/llo.git
cd llo
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Run the Tool

```bash
python3 flash_usdt.py
```

## Usage Examples

### Example 1: Check Your Wallet Balance

1. Run the tool: `python3 flash_usdt.py`
2. Choose option **1** (Check USDT Balance)
3. Enter network: `ethereum` (or `bsc`, `tron`)
4. Enter your wallet address: `0xYourAddressHere`
5. See your balance! 💰

### Example 2: Quick Balance Check (Command Line)

```bash
# Check Ethereum balance
python3 cli.py ethereum 0x5754284f345afc66a98fbB0a0Afe71e0F007B949

# Check BSC balance
python3 cli.py bsc 0x8894E0a0c962CB723c1976a4421c95949bE2D4E3

# Check TRON balance
python3 cli.py tron TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE
```

### Example 3: View Token Information

```bash
python3 cli.py ethereum --info
```

## Troubleshooting

### ❌ Error: "python is not recognized"

**Solution:**
- Reinstall Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation
- Restart your terminal/command prompt after installation

### ❌ Error: "No module named 'web3'"

**Solution:**
```bash
pip install web3 tronpy python-dotenv
```

If that doesn't work:
```bash
pip3 install web3 tronpy python-dotenv
```

### ❌ Error: "Permission denied" (Mac/Linux)

**Solution:**
```bash
chmod +x flash_usdt.py cli.py examples.py
```

### ❌ Error: "Failed to connect to network"

**Solutions:**
1. Check your internet connection
2. The RPC server might be busy - try again in a few minutes
3. Try a different network

### ❌ The menu doesn't appear

**Solution:**
- Make sure you're in the correct folder (`cd` to the llo folder)
- Try: `python3 flash_usdt.py` instead of `python`

## Testing Your Setup

Run this to verify everything works:

```bash
python3 test_tool.py
```

This will run a comprehensive test suite and tell you if there are any issues.

## File Structure

```
llo/
├── flash_usdt.py       # Main program (run this!)
├── cli.py              # Command-line version
├── examples.py         # Usage examples
├── test_tool.py        # Test suite
├── requirements.txt    # Dependencies list
├── config.json         # Network configuration
├── README.md           # Documentation (English)
├── README.bn.md        # Documentation (Bengali)
├── QUICKSTART.md       # Quick start guide
├── EXAMPLES.md         # Detailed examples
├── SECURITY.md         # Security information
└── CONTRIBUTING.md     # Contribution guidelines
```

## Next Steps

1. ✅ Read [SECURITY.md](SECURITY.md) for important safety information
2. ✅ Check [EXAMPLES.md](EXAMPLES.md) for more usage examples
3. ✅ Review [README.bn.md](README.bn.md) for Bengali documentation

## Video Tutorial

Coming soon... (we'll add a video walkthrough!)

## Need More Help?

- 📖 Read the full [README.md](README.md)
- 🌐 For Bengali speakers: [README.bn.md](README.bn.md)
- 💬 Open an issue on GitHub if you're stuck
- 🔍 Check [EXAMPLES.md](EXAMPLES.md) for detailed code examples

## Summary - Quick Commands

```bash
# 1. Download from GitHub (or use git clone)
# 2. Extract and open terminal in that folder

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the tool
python3 flash_usdt.py

# Or quick check:
python3 cli.py ethereum 0xYourAddress
```

**You're all set! Happy checking! 🚀**

---

**Remember:**
- 🔐 Never share your private keys
- 📖 This tool is read-only (safe!)
- ✅ Always verify addresses on blockchain explorers
- 🎓 For educational purposes only
