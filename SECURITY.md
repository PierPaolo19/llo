# Security Policy

## Supported Versions

Currently supported versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of Flash USDT seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Reporting Process

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via:
1. Opening a private security advisory on GitHub
2. Emailing the repository maintainers directly

### What to Include

Please include the following information in your report:
- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Timeline

- We will acknowledge receipt of your vulnerability report within 48 hours
- We will send a more detailed response within 7 days indicating the next steps
- We will keep you informed about the progress toward fixing the vulnerability
- We will notify you when the vulnerability is fixed

## Security Best Practices

### For Users

1. **Audit Before Use**: Always audit the contracts before deploying to mainnet
2. **Test Thoroughly**: Test your flash loan receivers extensively on testnet
3. **Monitor Transactions**: Keep track of all flash loan transactions
4. **Use Multi-sig**: Consider using multi-sig wallets for contract ownership
5. **Set Reasonable Limits**: Configure appropriate fee limits

### For Developers

1. **Follow Checks-Effects-Interactions**: Always follow this pattern in your code
2. **Use Reentrancy Guards**: All external calls should be protected
3. **Validate Inputs**: Always validate all user inputs
4. **Handle Errors Properly**: Use require/revert with meaningful messages
5. **Keep Dependencies Updated**: Regularly update OpenZeppelin and other dependencies

## Known Issues and Limitations

### Current Limitations

1. **Single Token Per Transaction**: Each flash loan handles one token at a time
2. **Gas Costs**: Complex operations may approach block gas limits
3. **MEV Risks**: Flash loan transactions may be front-run or sandwiched

### Mitigations

- Use private RPC endpoints to reduce MEV exposure
- Implement deadline parameters in your receiver contracts
- Consider using Flashbots or similar MEV protection services

## Security Audits

This project has not yet undergone a formal security audit. We recommend:
- Conducting your own audit before production use
- Starting with small amounts on testnet
- Gradually increasing exposure as confidence grows

## Bug Bounty

Currently, there is no formal bug bounty program. However, we appreciate responsible disclosure and will acknowledge contributors who help improve security.

## Contact

For security concerns, please open a security advisory on GitHub or contact the repository maintainers.
