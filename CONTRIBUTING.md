# Contributing

Thank you for your interest in contributing to this CCSDS packet definitions project!

## How to Contribute

1. **Fork the repository** and create a new branch for your changes
2. **Make your changes** following the project structure and coding standards
3. **Test your changes** by running `pytest`
4. **Ensure code quality** by running the linters:
   - `flake8 ccsds`
   - `pylint ccsds`
5. **Submit a Pull Request** with a clear description of your changes

## Code Standards

- Follow PEP 8 style guidelines (enforced by flake8)
- Maximum line length: 120 characters
- Use meaningful variable and function names
- Add docstrings to modules, classes, and functions
- Write unit tests for new packet definitions

## Testing

All packet definitions must include:
- Binary test data (`test/in.bin`)
- Unit test that validates parsing (`test/test_*.py`)
- Reference output will be auto-generated on first successful test run

## Pre-commit Hooks

Install pre-commit hooks before making changes:

```bash
pre-commit install && pre-commit install -t pre-push
```

These hooks will automatically:
- Remove trailing whitespace
- Fix end-of-file issues
- Reorder Python imports
- Run linters
- Run tests on push

## Questions?

If you have questions about contributing, please open an issue in the repository.
