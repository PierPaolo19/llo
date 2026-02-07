# Flash USDT - Windows 10 Pro Development Setup Script
# Run this script in PowerShell as Administrator

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Flash USDT - Windows Setup Script" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "WARNING: Not running as Administrator" -ForegroundColor Yellow
    Write-Host "Some features may require admin privileges" -ForegroundColor Yellow
    Write-Host ""
}

# Check Windows version
$osVersion = [System.Environment]::OSVersion.Version
Write-Host "Checking Windows version..." -ForegroundColor Green
Write-Host "Windows Version: $($osVersion.Major).$($osVersion.Minor) Build $($osVersion.Build)"

if ($osVersion.Major -lt 10) {
    Write-Host "ERROR: Windows 10 or higher is required" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Windows version compatible" -ForegroundColor Green
Write-Host ""

# Check Node.js
Write-Host "Checking Node.js installation..." -ForegroundColor Green
try {
    $nodeVersion = node --version
    Write-Host "Node.js: $nodeVersion"
    
    $majorVersion = [int]($nodeVersion.Substring(1).Split('.')[0])
    if ($majorVersion -lt 18) {
        Write-Host "WARNING: Node.js 18+ recommended (you have v$majorVersion)" -ForegroundColor Yellow
        Write-Host "Download from: https://nodejs.org" -ForegroundColor Yellow
    } else {
        Write-Host "✓ Node.js version compatible" -ForegroundColor Green
    }
} catch {
    Write-Host "ERROR: Node.js not found" -ForegroundColor Red
    Write-Host "Please install Node.js from https://nodejs.org" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Check npm
Write-Host "Checking npm..." -ForegroundColor Green
try {
    $npmVersion = npm --version
    Write-Host "npm: v$npmVersion"
    Write-Host "✓ npm installed" -ForegroundColor Green
} catch {
    Write-Host "ERROR: npm not found" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Check Git
Write-Host "Checking Git installation..." -ForegroundColor Green
try {
    $gitVersion = git --version
    Write-Host "$gitVersion"
    Write-Host "✓ Git installed" -ForegroundColor Green
} catch {
    Write-Host "WARNING: Git not found" -ForegroundColor Yellow
    Write-Host "Download from: https://git-scm.com/download/win" -ForegroundColor Yellow
}
Write-Host ""

# Check Python (required for some native modules)
Write-Host "Checking Python..." -ForegroundColor Green
try {
    $pythonVersion = python --version
    Write-Host "$pythonVersion"
    Write-Host "✓ Python installed" -ForegroundColor Green
} catch {
    Write-Host "WARNING: Python not found" -ForegroundColor Yellow
    Write-Host "Python may be needed for native module compilation" -ForegroundColor Yellow
    Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
}
Write-Host ""

# Check Visual Studio Build Tools
Write-Host "Checking for Visual Studio Build Tools..." -ForegroundColor Green
$vsWhere = "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe"
if (Test-Path $vsWhere) {
    $vsInstall = & $vsWhere -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath
    if ($vsInstall) {
        Write-Host "✓ Visual Studio Build Tools found" -ForegroundColor Green
    } else {
        Write-Host "WARNING: Visual Studio C++ Build Tools not found" -ForegroundColor Yellow
    }
} else {
    Write-Host "WARNING: Visual Studio Build Tools may not be installed" -ForegroundColor Yellow
    Write-Host "May be required for native module compilation" -ForegroundColor Yellow
}
Write-Host ""

# Check current directory
Write-Host "Checking current directory..." -ForegroundColor Green
$currentPath = Get-Location
Write-Host "Current path: $currentPath"

if (Test-Path "package.json") {
    Write-Host "✓ Found package.json" -ForegroundColor Green
    $packageJson = Get-Content "package.json" | ConvertFrom-Json
    Write-Host "Project: $($packageJson.name) v$($packageJson.version)"
} else {
    Write-Host "WARNING: package.json not found in current directory" -ForegroundColor Yellow
    Write-Host "Please navigate to the Flash USDT project directory" -ForegroundColor Yellow
}
Write-Host ""

# Offer to install dependencies
if (Test-Path "package.json") {
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host "Ready to install dependencies?" -ForegroundColor Cyan
    Write-Host "===================================" -ForegroundColor Cyan
    $install = Read-Host "Install npm dependencies? (Y/N)"
    
    if ($install -eq "Y" -or $install -eq "y") {
        Write-Host ""
        Write-Host "Installing dependencies..." -ForegroundColor Green
        Write-Host "This may take several minutes..." -ForegroundColor Yellow
        
        npm install
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
        } else {
            Write-Host ""
            Write-Host "ERROR: Failed to install dependencies" -ForegroundColor Red
            Write-Host "Check the error messages above" -ForegroundColor Red
        }
    }
}

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Setup Check Complete" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Display next steps
Write-Host "Next Steps:" -ForegroundColor Green
Write-Host "1. To run in development mode:" -ForegroundColor White
Write-Host "   npm run desktop" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. To build for Windows:" -ForegroundColor White
Write-Host "   npm run desktop:build" -ForegroundColor Cyan
Write-Host ""
Write-Host "3. For more information, see:" -ForegroundColor White
Write-Host "   docs/WINDOWS.md" -ForegroundColor Cyan
Write-Host ""

# Offer to set execution policy
if (-not $isAdmin) {
    Write-Host "Tip: To run PowerShell scripts, you may need to set execution policy:" -ForegroundColor Yellow
    Write-Host "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Cyan
    Write-Host ""
}

Write-Host "Setup script completed!" -ForegroundColor Green
Write-Host ""

# Pause if running in PowerShell ISE or as a script
if ($host.Name -eq 'ConsoleHost') {
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
}
