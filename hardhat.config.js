require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.20",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    hardhat: {
      chainId: 1337
    },
    // Add your network configurations here
    // mainnet: {
    //   url: process.env.MAINNET_RPC_URL,
    //   accounts: [process.env.PRIVATE_KEY]
    // }
  }
};
