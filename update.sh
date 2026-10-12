#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Building the package with Hatch..."
hatch build

echo "Publishing the package to PyPI..."
hatch publish

echo "Pulling latest changes from remote Git repository..."
# Use || true so the script continues even if there is no tracking upstream configured yet
git pull || echo "Pull skipped or failed, continuing..."

echo "Staging changes..."
git add .

echo "Committing changes..."
git commit -m "New version"

echo "Pushing changes to remote..."
git push

echo "Updating current installed module"
pip install --upgrade tmscli

echo "All steps completed successfully!"
