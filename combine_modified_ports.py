#!/usr/bin/env python3
import json
import glob
import os
from pathlib import Path

# Directory containing the modified port files
modified_ports_dir = Path("sea/modified_ports")

# Output file path
output_file = modified_ports_dir / "all_sea_ports_combined.json"

# List to store all ports
all_ports = []

# Get all country JSON files (excluding the combined file)
country_files = glob.glob(str(modified_ports_dir / "*.json"))
# Remove the combined file if it exists in the list
combined_file_path = str(output_file)
if combined_file_path in country_files:
    country_files.remove(combined_file_path)

print(f"Found {len(country_files)} country files to combine")

# Process each country file
for country_file in country_files:
    # Skip processing the combined file
    if os.path.basename(country_file) == "all_sea_ports_combined.json":
        continue
        
    try:
        with open(country_file, "r") as f:
            country_ports = json.load(f)
            
            # Process each port to remove id and add status
            for port in country_ports:
                # Remove 'id' field if it exists
                if 'id' in port:
                    del port['id']
                
                # Add 'status' field with value 'published'
                port['status'] = 'published'
            
            # Add all ports from this country to the combined list
            all_ports.extend(country_ports)
            
            country_code = Path(country_file).stem
            print(f"Added {len(country_ports)} ports from {country_code}")
            
    except Exception as e:
        print(f"Error processing {country_file}: {e}")

# Save the combined data
with open(output_file, "w") as f:
    json.dump(all_ports, f, indent=2)

print(f"Done! Combined {len(all_ports)} ports into {output_file} with 'id' field removed and 'status: published' added") 