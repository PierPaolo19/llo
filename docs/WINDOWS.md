# Flash USDT - Windows 10 Pro Installation & Usage Guide

This guide provides detailed instructions for installing and using Flash USDT on Windows 10 Pro.

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10 Pro (Version 1903 or later)
- **Processor**: Intel Core i3 or equivalent (64-bit)
- **RAM**: 4 GB
- **Storage**: 500 MB free space
- **Internet**: Broadband connection
- **Browser Extension**: MetaMask or compatible Web3 wallet

### Recommended Requirements
- **Operating System**: Windows 10 Pro (Latest version with all updates)
- **Processor**: Intel Core i5 or equivalent (64-bit)
- **RAM**: 8 GB or more
- **Storage**: 1 GB free space
- **Internet**: High-speed broadband

## Installation Methods

### Method 1: Installer (NSIS) - Recommended

1. **Download the Installer**
   - Go to the [Releases page](https://github.com/PierPaolo19/llo/releases)
   - Download `Flash-USDT-Setup-1.0.0.exe`

2. **Run the Installer**
   - Double-click the downloaded file
   - If Windows Defender SmartScreen appears:
     - Click "More info"
     - Click "Run anyway"
   - Choose installation directory (default: `C:\Program Files\Flash USDT`)
   - Select additional options:
     - ✅ Create Desktop Shortcut
     - ✅ Add to Start Menu
   - Click "Install"

3. **Launch the Application**
   - Double-click the Desktop shortcut, or
   - Start Menu → Flash USDT

### Method 2: Portable Version

1. **Download Portable**
   - Download `FlashUSDT-1.0.0-portable.exe`
   - No installation required

2. **Run Directly**
   - Place the file in any folder
   - Double-click to run
   - Perfect for USB drives or running without admin rights

### Method 3: Build from Source

#### Prerequisites

1. **Install Node.js**
   - Download Node.js LTS from https://nodejs.org (v18 or higher)
   - Run installer with default options
   - Verify installation:
     ```powershell
     node --version
     npm --version
     ```

2. **Install Git** (if not already installed)
   - Download from https://git-scm.com/download/win
   - Install with default options

3. **Install Visual Studio Build Tools** (for native modules)
   - Download from https://visualstudio.microsoft.com/downloads/
   - Select "Desktop development with C++"
   - Or install via PowerShell (as Administrator):
     ```powershell
     npm install --global --production windows-build-tools
     ```

#### Build Steps

1. **Open PowerShell or Command Prompt**
   ```powershell
   # Enable script execution (if needed)
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. **Clone the Repository**
   ```powershell
   git clone https://github.com/PierPaolo19/llo.git
   cd llo
   ```

3. **Install Dependencies**
   ```powershell
   npm install
   ```

4. **Run in Development Mode**
   ```powershell
   npm run desktop
   ```

5. **Build for Windows** (optional)
   ```powershell
   # Build installer and portable
   npm run desktop:build
   ```
   
   Output files will be in `dist\` folder:
   - `Flash USDT Setup 1.0.0.exe` - Installer
   - `FlashUSDT-1.0.0-portable.exe` - Portable version

## First-Time Setup

### 1. Configure Windows Defender

Flash USDT may be flagged by Windows Defender as it's an unsigned application:

1. **Add Exclusion** (Optional)
   - Open Windows Security
   - Virus & threat protection → Manage settings
   - Exclusions → Add or remove exclusions
   - Add folder: `C:\Program Files\Flash USDT`

2. **Allow Through Firewall**
   - Windows Defender Firewall → Allow an app
   - Click "Allow another app"
   - Browse to Flash USDT executable
   - Check both Private and Public networks

### 2. Install MetaMask

1. **Download Browser Extension**
   - Chrome: https://chrome.google.com/webstore
   - Firefox: https://addons.mozilla.org
   - Edge: https://microsoftedge.microsoft.com/addons

2. **Create or Import Wallet**
   - Follow MetaMask setup wizard
   - **Save your seed phrase securely!**

### 3. Configure Network Settings

Flash USDT works with multiple networks. See [Network Documentation](NETWORKS.md) for details.

## Using Flash USDT on Windows 10 Pro

### Launching the Application

**Method 1: Desktop Shortcut**
- Double-click the Flash USDT icon on your desktop

**Method 2: Start Menu**
- Press Windows key
- Type "Flash USDT"
- Press Enter

**Method 3: File Explorer**
- Navigate to installation folder
- Double-click `Flash USDT.exe`

### Connecting MetaMask

1. Launch Flash USDT
2. Click "Connect Wallet" button
3. MetaMask popup will appear
4. Click "Connect"
5. Approve the connection

### Keyboard Shortcuts (Windows)

| Shortcut | Action |
|----------|--------|
| `Ctrl + R` | Reload application |
| `Ctrl + Shift + I` | Open Developer Tools |
| `Ctrl + W` | Close window |
| `Ctrl + Q` | Quit application |
| `F11` | Toggle fullscreen |
| `Alt + F4` | Close application |

## Troubleshooting

### Application Won't Start

**Issue**: Double-clicking does nothing or shows error

**Solutions**:
1. **Check Windows version**
   ```powershell
   winver
   ```
   Must be Windows 10 version 1903 or later

2. **Run as Administrator**
   - Right-click Flash USDT
   - Select "Run as administrator"

3. **Install Visual C++ Redistributable**
   - Download from https://aka.ms/vs/17/release/vc_redist.x64.exe
   - Install and restart

4. **Check Event Viewer**
   - Press `Win + X` → Event Viewer
   - Windows Logs → Application
   - Look for Flash USDT errors

### Windows Defender SmartScreen

**Issue**: "Windows protected your PC" message

**Solution**:
1. Click "More info"
2. Click "Run anyway"
3. This is normal for unsigned applications

To prevent this:
- Disable SmartScreen temporarily:
  - Windows Security → App & browser control
  - Check app and file reputation → Off

### MetaMask Not Connecting

**Issue**: Wallet connection fails

**Solutions**:
1. **Check MetaMask Extension**
   - Ensure MetaMask is installed and unlocked
   - Try refreshing the page (Ctrl + R)

2. **Reset Connection**
   - MetaMask → Settings → Connected sites
   - Disconnect Flash USDT
   - Reconnect from the app

3. **Browser Cache**
   - Clear browser cache and cookies
   - Restart browser

### High CPU/Memory Usage

**Issue**: Application uses too much resources

**Solutions**:
1. **Close DevTools** (if open)
   - Press `Ctrl + Shift + I` to toggle

2. **Check Background Processes**
   - Task Manager (`Ctrl + Shift + Esc`)
   - Look for multiple Flash USDT processes
   - End unnecessary processes

3. **Update Graphics Drivers**
   - Use Windows Update or manufacturer website

### Installation Blocked by Admin

**Issue**: "Administrator privileges required"

**Solutions**:
1. **Use Portable Version**
   - Download portable .exe
   - No admin rights needed

2. **Request Admin Access**
   - Contact IT administrator
   - Or use from source (npm run desktop)

### Port Already in Use

**Issue**: Error when running from source

**Solution**:
```powershell
# Find process using port
netstat -ano | findstr :8545

# Kill process by PID
taskkill /PID <PID> /F
```

### Can't Build from Source

**Issue**: npm install fails with errors

**Solutions**:
1. **Clear npm cache**
   ```powershell
   npm cache clean --force
   ```

2. **Delete node_modules**
   ```powershell
   Remove-Item -Recurse -Force node_modules
   npm install
   ```

3. **Check Python**
   ```powershell
   python --version
   ```
   Must have Python 2.7 or 3.x

4. **Install Windows Build Tools**
   ```powershell
   npm install --global --production windows-build-tools
   ```

## Windows 10 Pro Specific Features

### Windows Notifications

Flash USDT uses Windows 10 native notifications:
- Transaction confirmations
- Network changes
- Error alerts

Configure in: Windows Settings → System → Notifications

### Windows Taskbar Integration

- **Jump List**: Right-click taskbar icon for quick actions
- **Progress**: Transaction progress shown in taskbar
- **Badge**: Notification count on icon

### PowerShell Integration

Run Flash USDT from PowerShell:

```powershell
# Navigate to installation
cd "C:\Program Files\Flash USDT"

# Run application
.\Flash USDT.exe

# Or add to PATH
$env:Path += ";C:\Program Files\Flash USDT"
```

### Windows Task Scheduler

Automate Flash USDT tasks:

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., At startup)
4. Action: Start a program
5. Program: `C:\Program Files\Flash USDT\Flash USDT.exe`

## Security Best Practices

### Windows Security

1. **Keep Windows Updated**
   - Settings → Update & Security
   - Check for updates regularly

2. **Use Windows Defender**
   - Built-in protection is sufficient
   - Enable real-time protection

3. **Secure Your Wallet**
   - Never share seed phrase
   - Use hardware wallet for large amounts
   - Enable 2FA where possible

4. **Firewall Rules**
   - Keep Windows Firewall enabled
   - Only allow Flash USDT through trusted networks

### User Account Control (UAC)

Keep UAC enabled for security:
- Alerts you when apps make changes
- Prevents unauthorized software installation

## Performance Optimization

### Windows 10 Pro Tips

1. **Disable Background Apps**
   - Settings → Privacy → Background apps
   - Disable unnecessary apps

2. **Power Plan**
   - Control Panel → Power Options
   - Use "High performance" plan

3. **Visual Effects**
   - System → Advanced → Performance Settings
   - Adjust for best performance

4. **SSD Optimization**
   - Install on SSD for faster loading
   - Enable TRIM (enabled by default)

## Uninstallation

### Method 1: Control Panel

1. Open Control Panel
2. Programs → Uninstall a program
3. Find "Flash USDT"
4. Click Uninstall
5. Follow wizard

### Method 2: Settings

1. Settings → Apps
2. Search "Flash USDT"
3. Click → Uninstall

### Method 3: Installer

1. Navigate to installation folder
2. Run `Uninstall Flash USDT.exe`

### Clean Uninstall

Remove all data:

```powershell
# Remove application data
Remove-Item -Recurse -Force "$env:APPDATA\Flash USDT"
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Flash USDT"

# Remove desktop shortcut
Remove-Item "$env:USERPROFILE\Desktop\Flash USDT.lnk"
```

## Development on Windows 10 Pro

### IDE Recommendations

- **Visual Studio Code**: https://code.visualstudio.com
- **WebStorm**: https://www.jetbrains.com/webstorm

### Useful Extensions (VS Code)

- Solidity
- ESLint
- Prettier
- Hardhat Solidity

### Debug Configuration

`.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Electron Main",
      "type": "node",
      "request": "launch",
      "cwd": "${workspaceFolder}",
      "runtimeExecutable": "${workspaceFolder}/node_modules/.bin/electron.cmd",
      "windows": {
        "runtimeExecutable": "${workspaceFolder}/node_modules/.bin/electron.cmd"
      },
      "args": ["."],
      "outputCapture": "std"
    }
  ]
}
```

## FAQ - Windows 10 Pro Specific

### Q: Does Flash USDT work on Windows 10 Home?
**A**: Yes, but this guide focuses on Pro features. Basic functionality works on all Windows 10 editions.

### Q: Can I run multiple instances?
**A**: Yes, but not recommended. May cause connection conflicts.

### Q: Does it work with Windows 11?
**A**: Yes, fully compatible with Windows 11.

### Q: Antivirus blocks installation?
**A**: Add exclusion in antivirus settings or temporarily disable during install.

### Q: Can I install on company laptop?
**A**: Check with IT policy. May require admin approval.

### Q: Supports ARM64 processors?
**A**: Not officially. Use x64 build with emulation.

### Q: Works in Virtual Machine?
**A**: Yes, but hardware wallet support may be limited.

### Q: Portable vs Installer?
**A**: 
- **Installer**: Better integration, Start Menu, auto-updates
- **Portable**: No install, run from USB, no admin needed

## Support

### Getting Help

1. **Documentation**: Check `/docs` folder
2. **GitHub Issues**: https://github.com/PierPaolo19/llo/issues
3. **Community**: GitHub Discussions

### Reporting Windows Issues

Include this information:
- Windows version (`winver`)
- Flash USDT version
- Error messages
- Event Viewer logs
- Steps to reproduce

### System Information

To get system info for support:

```powershell
# Windows version
winver

# System info
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"

# Node version
node --version

# npm version
npm --version
```

## Additional Resources

- [Desktop User Guide](DESKTOP.md)
- [Network Configuration](NETWORKS.md)
- [Tron Support](TRON.md)
- [Quick Start Guide](DESKTOP_QUICKSTART.md)

## License

Flash USDT is licensed under the MIT License. See [LICENSE](LICENSE) file.

---

**Last Updated**: February 2026  
**Windows 10 Pro Version**: Tested on 20H2, 21H1, 21H2, 22H2  
**Flash USDT Version**: 1.0.0

For general Flash USDT documentation, see [README.md](README.md)
