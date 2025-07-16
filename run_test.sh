#!/bin/bash

echo "Running all tests..."
"$PWD/python3-virtualenv/bin/python" -m unittest discover -v tests/
