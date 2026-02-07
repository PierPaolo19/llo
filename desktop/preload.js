const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld(
  'electronAPI', {
    getContractData: (contractAddress) => ipcRenderer.invoke('get-contract-data', contractAddress),
    executeFlashLoan: (params) => ipcRenderer.invoke('execute-flash-loan', params),
    getAppVersion: () => process.env.npm_package_version || '1.0.0'
  }
);

// Expose a safe subset of Node.js functionality if needed
contextBridge.exposeInMainWorld(
  'versions', {
    node: () => process.versions.node,
    chrome: () => process.versions.chrome,
    electron: () => process.versions.electron
  }
);
