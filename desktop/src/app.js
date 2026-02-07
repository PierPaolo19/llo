const { ethers } = require('ethers');

// Contract ABIs - These would be loaded from compiled artifacts
const FLASH_USDT_ABI = [
    "function availableLiquidity() view returns (uint256)",
    "function flashLoanFee() view returns (uint256)",
    "function calculateFee(uint256 amount) view returns (uint256)",
    "function flashLoan(address receiver, uint256 amount, bytes calldata params) external",
    "function deposit(uint256 amount) external",
    "function withdraw(uint256 amount, address recipient) external",
    "event FlashLoan(address indexed receiver, address indexed initiator, uint256 amount, uint256 fee)"
];

const USDT_ABI = [
    "function balanceOf(address account) view returns (uint256)",
    "function approve(address spender, uint256 amount) external returns (bool)",
    "function allowance(address owner, address spender) view returns (uint256)"
];

// State
let provider = null;
let signer = null;
let walletAddress = null;
let flashUSDTContract = null;
let usdtContract = null;
let currentNetwork = null;

// Contract addresses (update these for your deployment)
const CONTRACT_ADDRESSES = {
    1: { // Mainnet
        flashUSDT: '0x0000000000000000000000000000000000000000', // Update after deployment
        usdt: '0xdac17f958d2ee523a2206206994597c13d831ec7'
    },
    11155111: { // Sepolia
        flashUSDT: '0x0000000000000000000000000000000000000000', // Update after deployment
        usdt: '0x0000000000000000000000000000000000000000'
    },
    31337: { // Hardhat local
        flashUSDT: '0x0000000000000000000000000000000000000000',
        usdt: '0x0000000000000000000000000000000000000000'
    }
};

// Initialize on load
window.addEventListener('DOMContentLoaded', () => {
    initializeApp();
    setupEventListeners();
});

function initializeApp() {
    console.log('Flash USDT Desktop App initialized');
    updateUI();
}

function setupEventListeners() {
    // Wallet connection
    document.getElementById('connectWallet').addEventListener('click', connectWallet);

    // Flash loan form
    document.getElementById('flashLoanForm').addEventListener('submit', handleFlashLoan);
    document.getElementById('loanAmount').addEventListener('input', updateFeeEstimate);

    // Liquidity management
    document.getElementById('depositBtn').addEventListener('click', handleDeposit);
    document.getElementById('withdrawBtn').addEventListener('click', handleWithdraw);
}

async function connectWallet() {
    try {
        if (typeof window.ethereum === 'undefined') {
            alert('Please install MetaMask or another Web3 wallet!');
            return;
        }

        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create provider and signer
        provider = new ethers.BrowserProvider(window.ethereum);
        signer = await provider.getSigner();
        walletAddress = await signer.getAddress();

        // Get network
        const network = await provider.getNetwork();
        currentNetwork = Number(network.chainId);

        // Initialize contracts
        const addresses = CONTRACT_ADDRESSES[currentNetwork];
        if (addresses && addresses.flashUSDT !== '0x0000000000000000000000000000000000000000') {
            flashUSDTContract = new ethers.Contract(addresses.flashUSDT, FLASH_USDT_ABI, signer);
            usdtContract = new ethers.Contract(addresses.usdt, USDT_ABI, signer);
        }

        // Update UI
        updateUI();
        await loadContractData();

        // Listen for account changes
        window.ethereum.on('accountsChanged', handleAccountsChanged);
        window.ethereum.on('chainChanged', () => window.location.reload());

        showNotification('Wallet connected successfully!', 'success');
    } catch (error) {
        console.error('Error connecting wallet:', error);
        showNotification('Failed to connect wallet: ' + error.message, 'error');
    }
}

function handleAccountsChanged(accounts) {
    if (accounts.length === 0) {
        // User disconnected
        walletAddress = null;
        provider = null;
        signer = null;
        updateUI();
    } else {
        // Account changed
        connectWallet();
    }
}

async function loadContractData() {
    if (!flashUSDTContract) {
        showNotification('Contract not deployed on this network', 'warning');
        return;
    }

    try {
        // Load contract data
        const liquidity = await flashUSDTContract.availableLiquidity();
        const fee = await flashUSDTContract.flashLoanFee();

        // Update UI
        document.getElementById('availableLiquidity').textContent = 
            ethers.formatUnits(liquidity, 6) + ' USDT';
        document.getElementById('flashLoanFee').textContent = 
            (Number(fee) / 100).toFixed(2) + '%';

        const addresses = CONTRACT_ADDRESSES[currentNetwork];
        document.getElementById('contractAddress').textContent = 
            addresses.flashUSDT.substring(0, 10) + '...';
    } catch (error) {
        console.error('Error loading contract data:', error);
    }
}

function updateUI() {
    const connectBtn = document.getElementById('connectWallet');
    const walletInfo = document.getElementById('walletInfo');
    const walletAddressSpan = document.getElementById('walletAddress');
    const networkNameSpan = document.getElementById('networkName');
    const currentNetworkSpan = document.getElementById('currentNetwork');

    if (walletAddress) {
        connectBtn.style.display = 'none';
        walletInfo.style.display = 'block';
        walletAddressSpan.textContent = walletAddress.substring(0, 6) + '...' + walletAddress.substring(38);
        
        const networkNames = {
            1: 'Ethereum Mainnet',
            11155111: 'Sepolia Testnet',
            31337: 'Hardhat Local'
        };
        const networkName = networkNames[currentNetwork] || `Network ${currentNetwork}`;
        networkNameSpan.textContent = networkName;
        currentNetworkSpan.textContent = networkName;
    } else {
        connectBtn.style.display = 'block';
        walletInfo.style.display = 'none';
        currentNetworkSpan.textContent = 'Not Connected';
    }
}

async function updateFeeEstimate() {
    const amount = document.getElementById('loanAmount').value;
    if (!amount || !flashUSDTContract) {
        document.getElementById('estimatedFee').textContent = '0';
        return;
    }

    try {
        const amountWei = ethers.parseUnits(amount, 6);
        const fee = await flashUSDTContract.calculateFee(amountWei);
        document.getElementById('estimatedFee').textContent = ethers.formatUnits(fee, 6);
    } catch (error) {
        console.error('Error calculating fee:', error);
    }
}

async function handleFlashLoan(event) {
    event.preventDefault();

    if (!flashUSDTContract) {
        showNotification('Please connect wallet and ensure contract is deployed', 'error');
        return;
    }

    const receiverAddress = document.getElementById('receiverAddress').value;
    const amount = document.getElementById('loanAmount').value;
    const params = document.getElementById('customParams').value || '0x';

    const executeBtn = document.getElementById('executeBtn');
    executeBtn.disabled = true;
    executeBtn.textContent = 'Executing...';

    try {
        const amountWei = ethers.parseUnits(amount, 6);
        
        // Execute flash loan
        const tx = await flashUSDTContract.flashLoan(receiverAddress, amountWei, params);
        
        showNotification('Transaction sent! Waiting for confirmation...', 'info');
        
        // Wait for confirmation
        const receipt = await tx.wait();
        
        showNotification('Flash loan executed successfully!', 'success');
        addTransactionToHistory(receipt, 'Flash Loan', amount + ' USDT');
        
        // Reload contract data
        await loadContractData();
    } catch (error) {
        console.error('Error executing flash loan:', error);
        showNotification('Flash loan failed: ' + error.message, 'error');
    } finally {
        executeBtn.disabled = false;
        executeBtn.textContent = 'Execute Flash Loan';
    }
}

async function handleDeposit() {
    if (!flashUSDTContract || !usdtContract) {
        showNotification('Please connect wallet', 'error');
        return;
    }

    const amount = document.getElementById('depositAmount').value;
    if (!amount || amount <= 0) {
        showNotification('Please enter a valid amount', 'error');
        return;
    }

    try {
        const amountWei = ethers.parseUnits(amount, 6);
        
        // Check allowance
        const allowance = await usdtContract.allowance(walletAddress, CONTRACT_ADDRESSES[currentNetwork].flashUSDT);
        
        if (allowance < amountWei) {
            showNotification('Approving USDT...', 'info');
            const approveTx = await usdtContract.approve(CONTRACT_ADDRESSES[currentNetwork].flashUSDT, amountWei);
            await approveTx.wait();
        }

        showNotification('Depositing...', 'info');
        const tx = await flashUSDTContract.deposit(amountWei);
        await tx.wait();

        showNotification('Deposit successful!', 'success');
        document.getElementById('depositAmount').value = '';
        await loadContractData();
    } catch (error) {
        console.error('Error depositing:', error);
        showNotification('Deposit failed: ' + error.message, 'error');
    }
}

async function handleWithdraw() {
    if (!flashUSDTContract) {
        showNotification('Please connect wallet', 'error');
        return;
    }

    const amount = document.getElementById('withdrawAmount').value;
    if (!amount || amount <= 0) {
        showNotification('Please enter a valid amount', 'error');
        return;
    }

    try {
        const amountWei = ethers.parseUnits(amount, 6);
        
        showNotification('Withdrawing...', 'info');
        const tx = await flashUSDTContract.withdraw(amountWei, walletAddress);
        await tx.wait();

        showNotification('Withdrawal successful!', 'success');
        document.getElementById('withdrawAmount').value = '';
        await loadContractData();
    } catch (error) {
        console.error('Error withdrawing:', error);
        showNotification('Withdrawal failed: ' + error.message, 'error');
    }
}

function addTransactionToHistory(receipt, type, details) {
    const historyDiv = document.getElementById('transactionHistory');
    
    // Remove empty state message
    const emptyState = historyDiv.querySelector('.empty-state');
    if (emptyState) {
        emptyState.remove();
    }

    const txItem = document.createElement('div');
    txItem.className = 'transaction-item success';
    txItem.innerHTML = `
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
            <strong>${type}</strong>
            <span>${details}</span>
        </div>
        <div class="tx-hash">
            <strong>TX:</strong> ${receipt.hash}
        </div>
        <div style="font-size: 12px; color: var(--text-secondary); margin-top: 5px;">
            Block: ${receipt.blockNumber} | Gas Used: ${receipt.gasUsed.toString()}
        </div>
    `;
    
    historyDiv.insertBefore(txItem, historyDiv.firstChild);
}

function showNotification(message, type = 'info') {
    // Simple notification - could be enhanced with a toast library
    console.log(`[${type.toUpperCase()}]`, message);
    
    // Create notification element
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        background: ${type === 'success' ? 'var(--secondary-color)' : 
                     type === 'error' ? 'var(--danger-color)' : 
                     type === 'warning' ? 'var(--warning-color)' : 
                     'var(--primary-color)'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
