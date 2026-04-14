#!/bin/bash
# Run Verilog tests
echo "Running Verilog tests..."
python3 ../common/test_runner.py tests.md
# Also syntax check the verilog file
iverilog -t null ../../tt_verilog_interface.v
