#!/bin/bash

# Exit immediately if any command fails
set -e

read commit
read pypi
if [ "$pypi" == "yes" ]; then

    echo "   Building the package with Hatch..."
    hatch build

    echo "   Publishing the package to PyPI..."
    hatch publish

fi
if [ "$commit" == "yes" ]; then
    echo "   Pulling latest changes from remote Git repository..."
    git pull || echo "   Pull skipped or failed, continuing..."

    echo "   Staging changes..."
    git add .

    echo "   Committing changes..."
    read reason
    git commit -m "$reason"

    echo "   Pushing changes to remote..."
    git push
fi

echo "   Updating current installed module"
pip install --upgrade tmscli
echo "   All steps completed successfully!"
