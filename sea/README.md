# Port Search Tools

Tools to fetch and search for ports by country code.

## Requirements

- Node.js
- curl
- jq (JSON processor)

## Quick Start

1. **Setup**

```bash
chmod +x getPorts
chmod +x getAllPorts
```

2. **Fetch ports for a single country:**

```bash
./getPorts
Enter country code: US
```

2. **Fetch ports for all countries:**

```bash
./getAllPorts
```

This will create a `ports` directory with all port data.

## Examples

```bash
# Get ports for United States
./getPorts
Enter country code: US

# Get all countries' ports
./getAllPorts
```

## Files Created

- `[country_code].json`: Individual country port data
- `ports/`: Directory containing all port data
