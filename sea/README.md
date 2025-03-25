# Sea Port Data Processing

This directory contains scripts and data for processing and transforming sea port information from around the world.

## Directory Contents

- `ports/` - Original sea port data organized by country code (e.g., AG.json for Antigua and Barbuda)
- `modified_ports/` - Transformed sea port data with standardized format, organized by country code
- `modified_ports/all_sea_ports_combined.json` - Combined data from all countries
- `format.json` - Sample format for the transformed data
- `getPorts` - Script to fetch ports for a specific country
- `getAllPorts` - Script to fetch ports for all countries

## Data Processing Workflow

The sea port data processing involves transforming the original port data into a standardized format that's easier to work with:

1. Original data is collected for each country and stored in the `ports/` directory
2. Data is transformed to extract relevant fields and standardize the format
3. Transformed data is saved to corresponding files in the `modified_ports/` directory
4. All transformed data is combined into a single file `all_sea_ports_combined.json`

## Data Structure

### Original Format (Sample)

```json
{
  "title": "Antigua and Barbuda",
  "ckey": "antigua_and_barbuda",
  "cports": [
    {
      "name": "St. Johns",
      "t": true,
      "ckey": "st_johns_ag",
      "lat": "17.1166666667",
      "lng": "-61.8666666667"
    }
  ],
  "ccountries": []
}
```

### Transformed Format

```json
[
  {
    "id": "st_johns_ag",
    "name": "St. Johns",
    "location": "17.1166666667, -61.8666666667",
    "land_region": "",
    "country": "Antigua and Barbuda",
    "country_code": "AG",
    "functional_area": "",
    "body_of_water": "",
    "code": "st_johns_ag",
    "isTerminal": true
  }
]
```

The transformed data includes the following fields:

- `id` - Unique identifier for the port (from ckey)
- `name` - Port name
- `location` - Latitude and longitude, combined as a string
- `land_region` - Geographic region (if available)
- `country` - Full country name
- `country_code` - ISO country code
- `functional_area` - Specific area within the port (if available)
- `body_of_water` - Associated sea or ocean (if available)
- `code` - Same as id
- `isTerminal` - Whether the port is a terminal (from t field)

## Combined Data

The `all_sea_ports_combined.json` file contains all sea ports from all countries in the standardized format, making it easy to work with the complete dataset.

## Usage Example

To fetch ports for a specific country:

```bash
./getPorts
# When prompted, enter the country code (e.g., US)
```

To fetch ports for all countries:

```bash
./getAllPorts
```

To extract all sea ports for a specific country from the combined file:

```python
import json

# Load the combined data
with open('modified_ports/all_sea_ports_combined.json', 'r') as f:
    ports = json.load(f)

# Filter for ports in Canada
canada_ports = [port for port in ports if port['country_code'] == 'CA']

# Print count and first port
print(f"Found {len(canada_ports)} ports in Canada")
print(json.dumps(canada_ports[0], indent=2))
```
