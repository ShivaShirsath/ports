# Port Data Processing

This repository contains scripts and data for processing and transforming sea and air port information from around the world. The scripts transform raw port data into a standardized format that's easier to work with.

## Directory Structure

```
.
├── air/
│   ├── ports/                  - Original air port data (by country code)
│   ├── modified_ports/         - Transformed air port data (by country code)
│   ├── air_ports_all_data.json - Combined data from all countries
│   ├── process_airports.py     - Script to transform individual country files
│   ├── process_airports.sh     - Shell script to run the transformation
│   ├── combine_airports.py     - Script to combine all country files
│   └── combine_airports.sh     - Shell script to run the combination
├── sea/
│   ├── ports/                  - Original sea port data (by country code)
│   ├── modified_ports/         - Transformed sea port data (by country code)
│   ├── modified_ports/all_sea_ports_combined.json - Combined sea port data
│   ├── format.json             - Format template for sea port data
│   ├── getPorts                - Script to fetch ports for a specific country
│   └── getAllPorts             - Script to fetch ports for all countries
└── README.md                   - This file
```

## Air Port Data Processing

### Data Transformation

The air port data processing consists of two main steps:

1. **Country-wise data transformation**: Each country file in `air/ports/` (e.g., `AG.json` for Antigua and Barbuda) is processed to extract relevant fields and transform them into a standardized format.

2. **Data combination**: All transformed country files are combined into a single file with added status information.

### Fields Extracted

For each airport, the following fields are extracted and transformed:

| Field        | Source Field  | Description                                       |
| ------------ | ------------- | ------------------------------------------------- |
| name         | name          | Airport name                                      |
| code         | id            | Unique identifier                                 |
| type         | type          | Airport type (e.g. medium_airport, small_airport) |
| location     | municipality  | City or location                                  |
| country_id   | countryRef    | Country reference ID                              |
| country_code | country_code  | ISO country code                                  |
| IATA         | iata_code     | IATA airport code                                 |
| ICAO         | icao_code     | ICAO airport code                                 |
| Latitude     | latitude_deg  | Latitude in decimal degrees                       |
| Longitude    | longitude_deg | Longitude in decimal degrees                      |
| Altitude     | elevation_ft  | Altitude in feet                                  |
| EDI          | N/A           | (Optional field set to null)                      |
| status       | Added field   | Publication status (always "published")           |

### Running the Scripts

To process air port data:

```bash
# Process the data for individual countries
./air/process_airports.sh

# Combine all country data into one file
./air/combine_airports.sh
```

## Sea Port Data Processing

The sea port data follows a similar transformation process to the air port data, organizing ports by country and standardizing the data format.

### Sea Port Data Structure

The transformed sea port data contains the following fields:

| Field           | Description                        |
| --------------- | ---------------------------------- |
| name            | Port name                          |
| location        | Latitude and longitude as a string |
| land_region     | Geographic region (if available)   |
| country         | Full country name                  |
| country_code    | ISO country code                   |
| functional_area | Specific area within port          |
| body_of_water   | Associated sea or ocean            |
| code            | Unique identifier                  |
| isTerminal      | Whether the port is a terminal     |
| status          | Publication status ("published")   |

### Running Sea Port Scripts

To fetch sea port data:

```bash
# Fetch ports for a specific country
./sea/getPorts
# When prompted, enter the country code (e.g., US)

# Fetch ports for all countries
./sea/getAllPorts
```

## Example Data

### Air Port Example

Original format (simplified):

```json
{
  "contentType": "airport",
  "datatype": "airport",
  "id": "6359",
  "ident": "TAPA",
  "type": "medium_airport",
  "name": "V C Bird International Airport",
  "municipality": "Osbourn",
  "latitude_deg": "17.1367",
  "longitude_deg": "-61.792702",
  "elevation_ft": "62",
  "icao_code": "TAPA",
  "iata_code": "ANU",
  "countryRef": "302722",
  "country_code": "AG",
  "country_name": "Antigua and Barbuda"
}
```

Transformed format:

```json
{
  "name": "V C Bird International Airport",
  "code": "6359",
  "type": "medium_airport",
  "location": "Osbourn",
  "country_id": "302722",
  "country_code": "AG",
  "IATA": "ANU",
  "ICAO": "TAPA",
  "Latitude": "17.1367",
  "Longitude": "-61.792702",
  "Altitude": "62",
  "EDI": null,
  "status": "published"
}
```

### Sea Port Example

Original format:

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

Transformed format:

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
    "isTerminal": true,
    "status": "published"
  }
]
```

## Output Files

The main output files are:

- Individual country files in `air/modified_ports/` and `sea/modified_ports/`
- Combined air port data in `air/air_ports_all_data.json`
- Combined sea port data in `sea/modified_ports/all_sea_ports_combined.json`

These files contain all the port data in a standardized format that's ready for use in applications or further processing.
