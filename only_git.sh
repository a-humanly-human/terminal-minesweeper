#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Pulling latest changes from remote Git repository..."
# Use || true so the script continues even if there is no tracking upstream configured yet
git pull || echo "Pull skipped or failed, continuing..."

echo "Staging changes..."
git add .

echo "Committing changes..."
read reason
git commit -m "$reason"

echo "Pushing changes to remote..."
git push
