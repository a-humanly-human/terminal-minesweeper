#!/bin/bash

# 1. Start all three processes in the background simultaneously
echo "Starting tasks in parallel..."

hatch build &
PID_BUILD=$!

hatch publish &
PID_PASS=$!

# Replace 'pip install --upgrade ...' with your actual upgrade command if different
pip install --upgrade tmscli&
PID_PUBLISH=$!

# 2. Wait for all background processes to complete
wait $PID_BUILD $PID_PUBLISH $PID_UPGRADE

echo "All tasks finished!"
