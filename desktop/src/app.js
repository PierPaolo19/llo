// Flash USDT Desktop Application
// Uses ethers.js from CDN for security with Electron context isolation

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
    // Ethereum Mainnet (ERC20)
    1: {
        flashUSDT: '0x0000000000000000000000000000000000000000', // Update after deployment
        usdt: '0xdac17f958d2ee523a2206206994597c13d831ec7',
        name: 'Ethereum Mainnet',
        type: 'ERC20',
        explorer: 'https://etherscan.io'
    },
    // Sepolia Testnet (ERC20)
    11155111: {
        flashUSDT: '0x0000000000000000000000000000000000000000', // Update after deployment
        usdt: '0x0000000000000000000000000000000000000000',
        name: 'Sepolia Testnet',
        type: 'ERC20',
        explorer: 'https://sepolia.etherscan.io'
    },
    // Binance Smart Chain Mainnet (BEP20)
    56: {
        flashUSDT: '0x0000000000000000000000000000000000000000', // Update after deployment
        usdt: '0x55d398326f99059fF775485246999027B3197955', // BSC-USD (USDT on BSC)
        name: 'BSC Mainnet',
        type: 'BEP20',
        explorer: 'https://bscscan.com'
    },
    // BSC Testnet (BEP20)
    97: {
        flashUSDT: '0x0000000000000000000000000000000000000000', // Update after deployment
        usdt: '0x0000000000000000000000000000000000000000', // Update with testnet USDT
        name: 'BSC Testnet',
        type: 'BEP20',
        explorer: 'https://testnet.bscscan.com'
    },
    // Polygon Mainnet (ERC20 compatible)
    137: {
        flashUSDT: '0x0000000000000000000000000000000000000000', // Update after deployment
        usdt: '0xc2132D05D31c914a87C6611C10748AEb04B58e8F', // USDT on Polygon
        name: 'Polygon Mainnet',
        type: 'ERC20',
        explorer: 'https://polygonscan.com'
    },
    // Mumbai Testnet (Polygon)
    80001: {
        flashUSDT: '0x0000000000000000000000000000000000000000', // Update after deployment
        usdt: '0x0000000000000000000000000000000000000000',
        name: 'Mumbai Testnet',
        type: 'ERC20',
        explorer: 'https://mumbai.polygonscan.com'
    },
    // Hardhat local
    31337: {
        flashUSDT: '0x0000000000000000000000000000000000000000',
        usdt: '0x0000000000000000000000000000000000000000',
        name: 'Hardhat Local',
        type: 'ERC20',
        explorer: 'http://localhost:8545'
    }
};

// Network RPC endpoints for adding to MetaMask
const NETWORK_RPCS = {
    56: {
        rpcUrls: ['https://bsc-dataseed.binance.org'],
        chainName: 'Binance Smart Chain',
        nativeCurrency: { name: 'BNB', symbol: 'BNB', decimals: 18 },
        blockExplorerUrls: ['https://bscscan.com']
    },
    97: {
        rpcUrls: ['https://data-seed-prebsc-1-s1.binance.org:8545'],
        chainName: 'BSC Testnet',
        nativeCurrency: { name: 'BNB', symbol: 'BNB', decimals: 18 },
        blockExplorerUrls: ['https://testnet.bscscan.com']
    },
    137: {
        rpcUrls: ['https://polygon-rpc.com'],
        chainName: 'Polygon Mainnet',
        nativeCurrency: { name: 'MATIC', symbol: 'MATIC', decimals: 18 },
        blockExplorerUrls: ['https://polygonscan.com']
    },
    80001: {
        rpcUrls: ['https://rpc-mumbai.maticvigil.com'],
        chainName: 'Mumbai Testnet',
        nativeCurrency: { name: 'MATIC', symbol: 'MATIC', decimals: 18 },
        blockExplorerUrls: ['https://mumbai.polygonscan.com']
    }
};

// Helper to check if address is placeholder
function isPlaceholderAddress(address) {
    return !address || address === '0x0000000000000000000000000000000000000000';
}

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
    
    // Network switching buttons (if they exist)
    const addBscBtn = document.getElementById('addBscNetwork');
    const addPolygonBtn = document.getElementById('addPolygonNetwork');
    if (addBscBtn) addBscBtn.addEventListener('click', () => addNetworkToMetaMask(56));
    if (addPolygonBtn) addPolygonBtn.addEventListener('click', () => addNetworkToMetaMask(137));
}

// Function to add network to MetaMask
async function addNetworkToMetaMask(chainId) {
    if (typeof window.ethereum === 'undefined') {
        showNotification('Please install MetaMask', 'error');
        return;
    }
    
    const networkConfig = NETWORK_RPCS[chainId];
    if (!networkConfig) {
        showNotification('Network configuration not found', 'error');
        return;
    }
    
    try {
        await window.ethereum.request({
            method: 'wallet_addEthereumChain',
            params: [{
                chainId: '0x' + chainId.toString(16),
                chainName: networkConfig.chainName,
                nativeCurrency: networkConfig.nativeCurrency,
                rpcUrls: networkConfig.rpcUrls,
                blockExplorerUrls: networkConfig.blockExplorerUrls
            }]
        });
        showNotification(`${networkConfig.chainName} added to MetaMask!`, 'success');
    } catch (error) {
        console.error('Error adding network:', error);
        showNotification('Failed to add network: ' + error.message, 'error');
    }
}

// Function to switch network
async function switchNetwork(chainId) {
    if (typeof window.ethereum === 'undefined') {
        showNotification('Please install MetaMask', 'error');
        return;
    }
    
    try {
        await window.ethereum.request({
            method: 'wallet_switchEthereumChain',
            params: [{ chainId: '0x' + chainId.toString(16) }],
        });
    } catch (switchError) {
        // This error code indicates that the chain has not been added to MetaMask
        if (switchError.code === 4902) {
            await addNetworkToMetaMask(chainId);
        } else {
            console.error('Error switching network:', switchError);
            showNotification('Failed to switch network: ' + switchError.message, 'error');
        }
    }
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
        if (addresses && !isPlaceholderAddress(addresses.flashUSDT)) {
            flashUSDTContract = new ethers.Contract(addresses.flashUSDT, FLASH_USDT_ABI, signer);
            usdtContract = new ethers.Contract(addresses.usdt, USDT_ABI, signer);
        } else {
            showNotification('⚠️ Contract addresses not configured for this network. Please update CONTRACT_ADDRESSES in app.js', 'warning');
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
        
        // Get network info from CONTRACT_ADDRESSES
        const networkInfo = CONTRACT_ADDRESSES[currentNetwork];
        let networkName = networkInfo ? networkInfo.name : `Unknown Network (${currentNetwork})`;
        let networkType = networkInfo ? networkInfo.type : 'Unknown';
        
        // Add network type badge
        const displayName = `${networkName} (${networkType})`;
        networkNameSpan.textContent = displayName;
        currentNetworkSpan.textContent = displayName;
        
        // Add network type indicator
        if (networkInfo) {
            const typeIndicator = document.createElement('span');
            typeIndicator.style.cssText = `
                display: inline-block;
                margin-left: 10px;
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 11px;
                font-weight: bold;
                background: ${networkType === 'BEP20' ? '#F3BA2F' : 
                             networkType === 'TRC20' ? '#FF0013' : 
                             '#627EEA'};
                color: white;
            `;
            typeIndicator.textContent = networkType;
            
            // Only add if not already present
            if (!currentNetworkSpan.querySelector('span')) {
                currentNetworkSpan.appendChild(typeIndicator);
            }
        }
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
        
        // Use BigInt for comparison
        if (BigInt(allowance.toString()) < BigInt(amountWei.toString())) {
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
            Block: ${receipt.blockNumber} | Gas Used: ${receipt.gasUsed.toLocaleString()}
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
