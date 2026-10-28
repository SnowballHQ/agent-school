#!/bin/sh
# Run the check.py test-suite: clean fixtures must pass, mutated fixtures must fail the named check.
# Usage: sh run_tests.sh [mission ...]
cd "$(dirname "$0")" || exit 1
python3 test_checks.py "$@"
