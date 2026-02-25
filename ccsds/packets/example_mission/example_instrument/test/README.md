# Test Data

This directory contains test data for validating CCSDS packet parsing.

## Files

- **`in.bin`**: Binary CCSDS packet data used as input for testing
- **`out.pickle`**: Expected parsed output (auto-generated on first successful test run)
- **`test_example.py`**: Unit test that validates packet parsing

## How Testing Works

The test uses the `spac_kit.parser.compare()` function which:

1. Reads binary packet data from `in.bin`
2. Uses your packet definitions to parse the data
3. Compares the parsed output with the reference data in `out.pickle`
4. Fails if the outputs don't match

## Creating Test Data

### Option 1: Use Real Data

If you have actual downlink files:

```bash
cp /path/to/your/downlink.bin in.bin
```

### Option 2: Create Synthetic Data

Use Python's `struct` module to create binary packets:

```python
import struct

# Define your packet fields
packet = struct.pack(
    '>HHH...',  # Format string (> = big-endian, H = uint16, etc.)
    field1_value,
    field2_value,
    ...
)

with open('in.bin', 'wb') as f:
    f.write(packet)
```

## Running Tests

```bash
# Run from the project root
pytest

# Run with verbose output
pytest -v

# Run only this test
pytest ccsds/packets/example_mission/example_instrument/test/test_example.py
```

## First Run

On the first successful run with `create_output=True`, the test will:
1. Parse `in.bin`
2. Create `out.pickle` with the parsed output
3. This becomes your reference for future tests

After the reference is created, set `create_output=False` in the test to enable validation.

## Updating Reference Data

If you modify packet definitions, you may need to regenerate the reference:

1. Delete `out.pickle`
2. Temporarily set `create_output=True` in the test
3. Run the test to regenerate the reference
4. Set `create_output=False` again
5. Commit the updated `out.pickle`
