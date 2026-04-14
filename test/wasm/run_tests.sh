#!/bin/bash
# Run WASM tests
echo "Running WASM tests..."
python3 ../common/test_runner.py tests.md
# Also validate the TypeScript interface
tsc --noEmit ../../tt_wasm_interface.ts
