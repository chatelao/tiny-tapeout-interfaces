#!/bin/bash
# Run REST API tests
echo "Running REST API tests..."

# Start mock server
python3 mock_server.py > mock_server.log 2>&1 &
SERVER_PID=$!
sleep 2

# Run tests
python3 ../common/test_runner.py tests.md
RESULT=$?

# Kill mock server
kill $SERVER_PID

# Also validate the OpenAPI spec
openapi-spec-validator ../../rest_api.yaml

exit $RESULT
