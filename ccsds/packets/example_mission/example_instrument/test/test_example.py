"""Unit tests for example instrument packets.

This test uses the spac_kit.parser.compare function which:
1. Reads binary test data from 'in.bin'
2. Parses it using your packet definitions
3. Compares the output with reference data in 'out.pickle'
4. If out.pickle doesn't exist, it will be created on first successful run
"""
import os
import unittest

from spac_kit.parser import compare


class TestExampleCase:
    """Unit test class for example instrument packets."""

    def test_parse(self):
        """Test example packet parsing and reference comparison."""
        local_dir = os.path.dirname(__file__)
        # Parameters: directory, compare_output, verbose, debug, create_output
        # Set create_output=True on first run to generate the reference file
        compare(local_dir, create_output=False)


if __name__ == "__main__":
    unittest.main()
