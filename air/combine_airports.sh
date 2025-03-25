#!/bin/bash

# Change to the air directory
cd $(dirname "$0")

# Make the Python script executable
chmod +x combine_airports.py

# Run the Python script
python3 combine_airports.py

echo "Airport data combination completed!" 