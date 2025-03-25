# Air Port Data Processing

This directory contains scripts and data for processing and transforming air port information from around the world.

## Directory Contents

- `ports/` - Original air port data organized by country code (e.g., AG.json for Antigua and Barbuda)
- `modified_ports/` - Transformed air port data with standardized format, organized by country code
- `air_ports_all_data.json` - Combined data from all countries with added status field
- `process_airports.py` - Python script to transform individual country files
- `process_airports.sh` - Shell script to run the transformation process
- `combine_airports.py` - Python script to combine all country files and add status
- `combine_airports.sh` - Shell script to run the combination process

## Data Processing Workflow

### Step 1: Country-wise Data Transformation

The first step involves extracting relevant fields from each country's airport data and transforming them into a standardized format.

1. Read each JSON file in the `ports/` directory
2. Extract specific fields from each airport entry
3. Transform the data into the standardized format
4. Save the transformed data to corresponding files in the `modified_ports/` directory

**Script**: `process_airports.py`
**Run command**: `./process_airports.sh`

### Step 2: Data Combination

The second step combines all the transformed country files into a single file and adds a status field to each airport entry.

1. Read all JSON files in the `modified_ports/` directory
2. Add "status": "published" to each airport entry
3. Combine all airports into a single array
4. Save the combined data to `air_ports_all_data.json`

**Script**: `combine_airports.py`
**Run command**: `./combine_airports.sh`

## Data Structure

### Original Format Fields (Sample)

```
- contentType
- datatype
- id
- ident
- type
- name
- regionRef
- continentRef
- municipality
- latitude_deg
- longitude_deg
- elevation_ft
- magnetic_variation_deg
- icao_code
- iata_code
- gps_code
- local_code
- has_scheduled_service
- ... (other fields)
```

### Transformed Format Fields

```
- name         - Airport name
- code         - Unique identifier (from id)
- type         - Airport type (e.g., medium_airport, small_airport)
- location     - City or location (from municipality)
- country_id   - Country reference ID (from countryRef)
- country_code - ISO country code
- IATA         - IATA airport code (from iata_code)
- ICAO         - ICAO airport code (from icao_code)
- Latitude     - Latitude in decimal degrees (from latitude_deg)
- Longitude    - Longitude in decimal degrees (from longitude_deg)
- Altitude     - Altitude in feet (from elevation_ft)
- EDI          - Set to null (placeholder for future data)
- status       - Publication status (always "published", added in combination step)
```

## Statistics

After processing, the combined file contains data for 3,505 airports from 105 countries.

## Usage Example

To extract all airports from India:

```python
import json

# Load the combined data
with open('air_ports_all_data.json', 'r') as f:
    airports = json.load(f)

# Filter for airports in India
india_airports = [airport for airport in airports if airport['country_code'] == 'IN']

# Print count and first airport
print(f"Found {len(india_airports)} airports in India")
print(json.dumps(india_airports[0], indent=2))
```
