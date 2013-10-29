#!/bin/bash
pip install -e .
cd otest && pip install . ; cd -

# cd into dir that is unlikely to contain the current tests, just to be sure
# that we're really doing what we think we are.
cd /tmp

echo "testing everything (5 tests)"
set -x
run-tests otest.atest project.testing project.test2

echo "testing just otest (1 test)"
run-tests otest.atest

echo "testing project.test2 (2 tests)"
run-tests project.test2

set +x
cd -
