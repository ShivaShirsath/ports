#!/bin/bash

# Change to the air directory
cd $(dirname "$0")

# Make the Python script executable
chmod +x process_airports.py

# Run the Python script
python3 process_airports.py

echo "Airport data processing completed!" 