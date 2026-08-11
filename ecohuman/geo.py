"""
GeoJSON Feature Collection Generator for Local Ecological Resources.
"""
import json
from typing import List, Dict

class LocalResourceMapper:
    def __init__(self):
        self.features: List[Dict] = []

    def add_point(self, latitude: float, longitude: float, name: str, category: str, description: str):
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [longitude, latitude]
            },
            "properties": {
                "name": name,
                "category": category,
                "description": description
            }
        }
        self.features.append(feature)

    def to_geojson(self) -> str:
        geojson = {
            "type": "FeatureCollection",
            "features": self.features
        }
        return json.dumps(geojson, indent=2)
