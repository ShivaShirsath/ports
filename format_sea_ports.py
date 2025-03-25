#!/usr/bin/env python3
import json
import os
import glob
from pathlib import Path
from collections import defaultdict

# Ensure the output directories exist
output_dir = Path("sea/modified_ports")
output_dir.mkdir(exist_ok=True, parents=True)

# Create all_ports directory for combined file
all_ports_dir = Path("all_ports")
all_ports_dir.mkdir(exist_ok=True, parents=True)

# Read the format template
with open("sea/format.json", "r") as f:
    format_template = json.load(f)

# Get list of all country files
country_files = glob.glob("sea/ports/*.json")

# Create a dictionary to store ports by country code
country_ports = defaultdict(list)

# Create a list to store all ports
all_ports_list = []

# Process each country file
for country_file in country_files:
    country_code = os.path.basename(country_file).split('.')[0]  # Extract country code from filename
    
    try:
        # Read the country data
        with open(country_file, "r") as f:
            country_data = json.load(f)
        
        country_name = country_data.get("title", "Unknown")
        ports = country_data.get("cports", [])
        
        # Process each port in the country
        for port in ports:
            # Create a formatted port object
            formatted_port = {
                "id": port.get("ckey", ""),  # Use ckey as the unique identifier
                "name": port.get("name", ""),
                "location": f"{port.get('lat', '')}, {port.get('lng', '')}",
                "land_region": "",  # Not available in the original data
                "country": country_name,
                "country_code": country_code,
                "functional_area": "",  # Not available in the original data
                "body_of_water": "",  # Not available in the original data
                "code": port.get("ckey", ""),  # Using ckey as the port code
                "isTerminal": port.get("t", False)  # Terminal flag
            }
            
            # Add the formatted port to the country's list
            country_ports[country_code].append(formatted_port)
            
            # Also add to the all ports list
            all_ports_list.append(formatted_port)
                
        print(f"Processed {len(ports)} ports from {country_name} ({country_code})")
            
    except Exception as e:
        print(f"Error processing {country_file}: {e}")

# Save country-wise port files
total_ports = 0
for country_code, ports in country_ports.items():
    total_ports += len(ports)
    output_file = output_dir / f"{country_code}.json"
    with open(output_file, "w") as f:
        json.dump(ports, f, indent=2)
    print(f"Saved {len(ports)} ports to {output_file}")

# Save all ports to a single file in all_ports directory
all_ports_file = all_ports_dir / "ports.json"
with open(all_ports_file, "w") as f:
    json.dump(all_ports_list, f, indent=2)

print(f"Done! All {total_ports} sea ports saved to country-wise files in {output_dir}")
print(f"Additionally, all ports combined are saved to {all_ports_file}") 