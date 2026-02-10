# Contributing to Multi-Network USDT Tool

Thank you for your interest in contributing! We welcome contributions from the community.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)

### Submitting Changes

1. **Fork the repository**
   ```bash
   git clone https://github.com/PierPaolo19/llo.git
   cd llo
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clear, documented code
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation

4. **Test your changes**
   ```bash
   python3 test_tool.py
   python3 -m py_compile *.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style Guidelines

### Python Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Use type hints where appropriate

### Example:

```python
def get_balance(self, network: str, address: str) -> Optional[Decimal]:
    """
    Get USDT balance for an address on a specific network
    
    Args:
        network: Network name ('ethereum', 'bsc', 'tron')
        address: Wallet address
        
    Returns:
        Decimal: Balance in USDT, or None if error
    """
    # Implementation
```

### Documentation

- Update README.md if adding features
- Add examples for new functionality
- Keep SECURITY.md updated with warnings
- Document breaking changes clearly

## Testing

Before submitting:

1. Run the test suite: `python3 test_tool.py`
2. Test with different networks
3. Verify error handling
4. Check for security issues

## Areas for Contribution

We welcome contributions in:

### Features
- Support for additional networks (Polygon, Avalanche, etc.)
- Support for other stablecoins
- Batch operations
- GUI interface
- API endpoint
- Better error handling

### Documentation
- More examples
- Video tutorials
- Translations
- Better inline comments

### Testing
- Unit tests
- Integration tests
- Network simulation tests
- Error case testing

### Security
- Security audits
- Vulnerability reports
- Best practices documentation
- Input validation improvements

## Security Issues

**DO NOT** open public issues for security vulnerabilities.

Instead:
1. Contact maintainers privately
2. Provide detailed information
3. Wait for acknowledgment
4. Allow time for fixes

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive criticism
- Accept feedback gracefully
- Prioritize community well-being

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## Questions?

Feel free to:
- Open a discussion on GitHub
- Ask in issue comments
- Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make this project better! 🚀
