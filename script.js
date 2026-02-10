let flashEnabled = true;

async function fetchUSDTPrice() {
    const statusEl = document.getElementById('status');
    statusEl.textContent = 'Fetching USDT data...';
    statusEl.className = 'status';

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
            
            document.getElementById('marketCapValue').textContent = `$${(marketCap / 1000000000).toFixed(2)}B`;

            statusEl.textContent = 'Data updated successfully!';
            statusEl.className = 'status success';
        } else {
            throw new Error('Invalid data format');
        }
    } catch (error) {
        console.error('Error fetching USDT data:', error);
        
        const demoPrice = 1.0000 + (Math.random() - 0.5) * 0.0001;
        const demoChange = (Math.random() - 0.5) * 0.2;
        const demoMarketCap = 95.5 + (Math.random() - 0.5) * 2;
        
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
