#!/bin/bash
echo "Running UART Interface Tests..."
# Use the common test runner to validate the structure of the UART tests
python3 ../common/test_runner.py tests.md
