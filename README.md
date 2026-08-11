# EcoHuman-Nexus 🌱🤝

> A modular, open-source python framework for crowdsourcing solutions to systemic environmental and social problems.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

EcoHuman-Nexus is a multi-module ecological toolkit. Rather than focusing on single-use scripts, it provides an extensible Python engine for community-driven sustainability.

---

## 📦 Architecture & Key Modules

1. **`ecohuman.matchmaker` (SQLite Waste-to-Resource Engine)**  
   Production-grade relational matching system that routes surplus food, construction materials, and electronics away from landfills to organizations that need them.

2. **`ecohuman.carbon` (Scope 1 & 2 Carbon Footprint Estimator)**  
   Calculates greenhouse gas emissions (in kg and Metric Tons of CO2e) for small businesses based on electricity, gas, fuel, and landfill waste metrics.

3. **`ecohuman.geo` (GIS Resource FeatureCollection Generator)**  
   Outputs valid GeoJSON FeatureCollections for mapping local clean water stations, urban gardens, and recycling points.

4. **`ecohuman.policy` (Environmental Policy Monitor)**  
   Tracks and filters municipal and state-level environmental regulations.

---

## 🛠️ Quickstart

### Installation
```bash
git clone https://github.com/ACTIVESHOORT/EcoHuman-Nexus.git
cd EcoHuman-Nexus
pip install -r requirements.txt
```

### Running the CLI Suite
```bash
python main.py
```

### Running Unit Tests
```bash
pytest tests/
```

---

## 🤝 Contributing
Contributions are welcome! Please open an Issue or PR to expand our module ecosystem.

*Built with ❤️ for community-driven ecological action.*
