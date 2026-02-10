let flashEnabled = true;
let lastFetchTime = 0;

const DEMO_BASE_PRICE = 1.0000;
const DEMO_PRICE_VARIANCE = 0.001;
const DEMO_BASE_CHANGE = 0;
const DEMO_CHANGE_VARIANCE = 0.2;
const DEMO_BASE_MARKET_CAP = 95.5;
const DEMO_MARKET_CAP_VARIANCE = 2;
const BILLION = 1e9;
const MIN_FETCH_INTERVAL_MS = 10000;

async function fetchUSDTPrice() {
    const statusEl = document.getElementById('status');
    
    const now = Date.now();
    const timeSinceLastFetch = now - lastFetchTime;
    
    if (timeSinceLastFetch < MIN_FETCH_INTERVAL_MS && lastFetchTime > 0) {
        const remainingSeconds = Math.ceil((MIN_FETCH_INTERVAL_MS - timeSinceLastFetch) / 1000);
        statusEl.textContent = `Please wait ${remainingSeconds} seconds before refreshing again`;
        statusEl.className = 'status';
        return;
    }
    
    statusEl.textContent = 'Fetching USDT data...';
    statusEl.className = 'status';
    lastFetchTime = now;

    try {
        const response = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd&include_24hr_change=true&include_market_cap=true');
        
        if (!response.ok) {
            throw new Error('Failed to fetch USDT data');
        }

        const data = await response.json();
        
        if (data && data.tether) {
            const price = data.tether.usd || 1.00;
            const change = data.tether.usd_24h_change || 0;
            const marketCap = data.tether.usd_market_cap || 0;

            document.getElementById('priceValue').textContent = `$${price.toFixed(4)}`;
            
            const changeEl = document.getElementById('changeValue');
            changeEl.textContent = `${change >= 0 ? '+' : ''}${change.toFixed(2)}%`;
            changeEl.style.color = change >= 0 ? '#27ae60' : '#e74c3c';
            
            document.getElementById('marketCapValue').textContent = `$${(marketCap / BILLION).toFixed(2)}B`;

            statusEl.textContent = 'Data updated successfully!';
            statusEl.className = 'status success';
        } else {
            throw new Error('Invalid data format');
        }
    } catch (error) {
        console.error('Error fetching USDT data:', error);
        
        const demoPrice = DEMO_BASE_PRICE + (Math.random() - 0.5) * DEMO_PRICE_VARIANCE;
        const demoChange = DEMO_BASE_CHANGE + (Math.random() - 0.5) * DEMO_CHANGE_VARIANCE;
        const demoMarketCap = DEMO_BASE_MARKET_CAP + (Math.random() - 0.5) * DEMO_MARKET_CAP_VARIANCE;
        
        document.getElementById('priceValue').textContent = `$${demoPrice.toFixed(4)}`;
        
        const changeEl = document.getElementById('changeValue');
        changeEl.textContent = `${demoChange >= 0 ? '+' : ''}${demoChange.toFixed(2)}%`;
        changeEl.style.color = demoChange >= 0 ? '#27ae60' : '#e74c3c';
        
        document.getElementById('marketCapValue').textContent = `$${demoMarketCap.toFixed(2)}B`;
        
        statusEl.textContent = 'Using demo data (API unavailable)';
        statusEl.className = 'status';
    }
}

function applyFlashState() {
    const priceEl = document.getElementById('usdtPrice');
    const btnEl = document.getElementById('toggleFlashBtn');
    
    if (flashEnabled) {
        priceEl.classList.add('flash');
        btnEl.textContent = 'Disable Flash';
    } else {
        priceEl.classList.remove('flash');
        btnEl.textContent = 'Enable Flash';
    }
}

function toggleFlash() {
    flashEnabled = !flashEnabled;
    applyFlashState();
}

document.getElementById('refreshBtn').addEventListener('click', fetchUSDTPrice);
document.getElementById('toggleFlashBtn').addEventListener('click', toggleFlash);

fetchUSDTPrice();
applyFlashState();
