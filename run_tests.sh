#!/bin/bash

echo "=== Starting Quantium Test Suite ==="

pytest test_app.py -v

TEST_RESULT=$?

echo "=== Test Suite Complete ==="

exit $TEST_RESULT