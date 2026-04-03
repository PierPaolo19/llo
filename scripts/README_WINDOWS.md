# Windows Setup Scripts

These scripts help set up Flash USDT on Windows 10 Pro.

## Files

### setup-windows.ps1
PowerShell setup script with comprehensive checks.

**Usage:**
```powershell
# Run in PowerShell (may require admin)
.\setup-windows.ps1
```

**Features:**
- Checks system requirements
- Verifies Node.js and npm installation
- Checks for Git and Python
- Validates Visual Studio Build Tools
- Installs npm dependencies

### setup-windows.bat
Simple batch script for basic setup.

**Usage:**
```cmd
# Run in Command Prompt
.\setup-windows.bat
```

**Features:**
- Checks for Node.js and npm
- Validates project structure
- Installs dependencies

## Requirements

Before running these scripts:

1. **Node.js 18+**: https://nodejs.org
2. **npm** (comes with Node.js)
3. **Git** (optional): https://git-scm.com

For building native modules:
- Visual Studio Build Tools or Visual Studio 2019+
- Python 2.7 or 3.x

## Troubleshooting

### PowerShell Execution Policy

If you get "script cannot be loaded" error:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Admin Rights

Some checks require administrator privileges. If running without admin:
- Some warnings are expected
- Core functionality still works

### Build Tools

If npm install fails with native module errors:

```powershell
# Option 1: Install Windows Build Tools
npm install --global --production windows-build-tools

# Option 2: Install Visual Studio 2019+
# With "Desktop development with C++" workload
```

## More Information

See [Windows 10 Pro Guide](../docs/WINDOWS.md) for complete documentation.
