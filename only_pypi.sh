#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Building the package with Hatch..."
hatch build

echo "Publishing the package to PyPI..."
hatch publish

echo "Updating current installed module"
pip install --upgrade tmscli
