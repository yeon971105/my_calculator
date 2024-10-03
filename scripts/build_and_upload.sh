#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting the build process..."

# Clean any previous builds
echo "Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info

# Build the package
echo "Building the package..."
python3 setup.py sdist bdist_wheel

# Set the PYTHONPATH to include the project directory
export PYTHONPATH=$(pwd)

# Run all test files
echo "Running test files..."
for test_file in tests/*.py; do
    echo "Testing $test_file..."
    python3 "$test_file"
done

echo "All tests passed successfully!"

# Optional: Upload to PyPI (you can remove/comment out this section if not needed)
# Ensure you have installed twine: `pip install twine`
# echo "Uploading to PyPI..."
# twine upload dist/*

echo "Build process completed!"

