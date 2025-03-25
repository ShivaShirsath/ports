#!/usr/bin/env python3

import os
import json
import glob
import sys

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define absolute paths
    ports_dir = os.path.join(script_dir, 'ports')
    modified_ports_dir = os.path.join(script_dir, 'modified_ports')
    
    # Create modified_ports directory if it doesn't exist
    if not os.path.exists(modified_ports_dir):
        os.makedirs(modified_ports_dir)
        print(f"Created directory: {modified_ports_dir}")
    
    # Get all JSON files in the ports directory
    port_files = glob.glob(os.path.join(ports_dir, '*.json'))
    
    print(f"Found {len(port_files)} country files to process")
    
    for port_file in port_files:
        country_code = os.path.basename(port_file).split('.')[0]
        print(f"Processing country: {country_code}")
        
        try:
            # Read the original file
            with open(port_file, 'r', encoding='utf-8') as f:
                airports = json.load(f)
            
            # Transform the data
            transformed_airports = []
            for airport in airports:
                try:
                    transformed_airport = {
                        "name": airport.get("name"),
                        "code": airport.get("id"),
                        "type": airport.get("type"),
                        "location": airport.get("municipality"),
                        "country_id": airport.get("countryRef"),
                        "country_code": airport.get("country_code"),
                        "IATA": airport.get("iata_code"),
                        "ICAO": airport.get("icao_code"),
                        "Latitude": airport.get("latitude_deg"),
                        "Longitude": airport.get("longitude_deg"),
                        "Altitude": airport.get("elevation_ft"),
                        "EDI": None  # EDI field wasn't in the original data
                    }
                    transformed_airports.append(transformed_airport)
                except Exception as e:
                    print(f"Error processing airport in {country_code}: {e}")
            
            # Write the transformed data to a new file
            output_file = os.path.join(modified_ports_dir, f"{country_code}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(transformed_airports, f, indent=2, ensure_ascii=False)
            
            print(f"Successfully processed {len(transformed_airports)} airports for {country_code}")
            
        except Exception as e:
            print(f"Error processing file {port_file}: {e}")
    
    print("All files have been processed.")

if __name__ == "__main__":
    main() 