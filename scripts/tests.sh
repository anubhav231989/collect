#!/bin/bash
. /app_env/bin/activate
pip3 install -r requirements_test.txt

# RUN TESTS.SH WITH ARGUMENTS PASSED AS PROCESS ID 1.
exec $@