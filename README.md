# EcoHuman-Nexus

A lightweight, zero-dependency Python framework for localized resource routing, geospatial asset mapping, and carbon accounting.

## Architectural Overview

EcoHuman-Nexus provides modular components designed for community resilience projects and urban sustainability programs.

```
EcoHuman-Nexus/
├── ecohuman/
│   ├── __init__.py
│   ├── matchmaker.py   # SQLite-backed Haversine geospatial matching engine
│   ├── carbon.py       # Scope 1/2 GHG emission calculator
│   ├── geo.py          # GeoJSON FeatureCollection mapper
│   └── policy.py       # Municipal environmental policy parser
├── tests/
│   └── test_ecohuman.py # Comprehensive unit test suite
├── .github/
│   └── workflows/
│       └── ci.yml      # Automated GitHub Actions test pipeline
├── setup.py            # Standard Python package configuration
└── main.py             # CLI Entrypoint
```

## Modules & Specifications

### 1. Geospatial Waste Matchmaker (`ecohuman.matchmaker`)
Employs the Haversine formula to compute great-circle distances between resource donors and receivers:

$$\text{Distance} = 2r \arcsin \left( \sqrt{\sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta \lambda}{2}\right)} \right)$$

Matches are filtered dynamically based on custom radius constraints (`max_distance_km`).

### 2. GHG Emission Accounting (`ecohuman.carbon`)
Calculates Scope 1 and Scope 2 equivalent carbon emissions ($\text{kg CO}_2\text{e}$) using standard EPA inventory conversion metrics across electricity grid consumption, natural gas, and liquid fuels.

### 3. Local GIS Mapper (`ecohuman.geo`)
Generates standardized GeoJSON structures for integration with Leaflet.js, OpenStreetMap, or ArcGIS platforms.

---

## Quickstart

### Prerequisites
Python 3.8+ (Zero external dependencies required).

### Installation
```bash
git clone https://github.com/ACTIVESHOORT/EcoHuman-Nexus.git
cd EcoHuman-Nexus
pip install -e .
```

### Execution
Run the system demonstration CLI:
```bash
python main.py --max-distance 50.0
```

### Running Test Suite
Execute the automated test suite locally:
```bash
python -m unittest discover tests
```

---

## License
MIT License. See [LICENSE](LICENSE) for details.
