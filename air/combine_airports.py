#!/usr/bin/env python3

import os
import json
import glob

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths
    modified_ports_dir = os.path.join(script_dir, 'modified_ports')
    combined_file = os.path.join(script_dir, 'air_ports_all_data.json')
    
    # Check if modified_ports directory exists
    if not os.path.exists(modified_ports_dir):
        print(f"Error: Directory {modified_ports_dir} does not exist")
        return
    
    # Get all JSON files in the modified_ports directory
    port_files = glob.glob(os.path.join(modified_ports_dir, '*.json'))
    
    print(f"Found {len(port_files)} country files to combine")
    
    # Initialize an empty list to store all airports
    all_airports = []
    
    # Process each file
    for port_file in port_files:
        country_code = os.path.basename(port_file).split('.')[0]
        print(f"Processing country: {country_code}")
        
        try:
            # Read the file
            with open(port_file, 'r', encoding='utf-8') as f:
                airports = json.load(f)
            
            # Add status field to each airport and add to the combined list
            for airport in airports:
                airport["status"] = "published"
                all_airports.append(airport)
            
            print(f"Added {len(airports)} airports from {country_code}")
            
        except Exception as e:
            print(f"Error processing file {port_file}: {e}")
    
    # Write the combined data to a new file
    try:
        with open(combined_file, 'w', encoding='utf-8') as f:
            json.dump(all_airports, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully combined {len(all_airports)} airports into {combined_file}")
    except Exception as e:
        print(f"Error writing combined file: {e}")
    
    print("Combination completed.")

if __name__ == "__main__":
    main() 