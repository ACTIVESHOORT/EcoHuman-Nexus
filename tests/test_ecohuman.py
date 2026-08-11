import unittest
from ecohuman.matchmaker import AdvancedMatchmaker, ResourceItem, haversine_distance
from ecohuman.carbon import CarbonTracker
from ecohuman.geo import LocalResourceMapper

class TestEcoHumanFramework(unittest.TestCase):
    def test_haversine(self):
        # Distance between LA (34.0522, -118.2437) and Pasadena (34.1478, -118.1445) is ~14 km
        dist = haversine_distance(34.0522, -118.2437, 34.1478, -118.1445)
        self.assertGreater(dist, 10.0)
        self.assertLess(dist, 20.0)

    def test_carbon_tracker(self):
        tracker = CarbonTracker("Test Co")
        res = tracker.calculate_footprint({"electricity_kwh": 100})
        self.assertEqual(res["total_kg_co2e"], 38.5)

    def test_matchmaker_within_distance(self):
        mm = AdvancedMatchmaker()
        mm.add_donation(ResourceItem(entity_name="Donor A", item_type="Wood", quantity=10.0, unit="boards", lat=34.0522, lon=-118.2437))
        mm.add_request("Receiver B", "Wood", 5.0, "boards", lat=34.0530, lon=-118.2440)
        matches = mm.process_matches(max_distance_km=10.0)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].amount_matched, 5.0)

    def test_matchmaker_exceeds_distance(self):
        mm = AdvancedMatchmaker()
        mm.add_donation(ResourceItem(entity_name="Donor A", item_type="Wood", quantity=10.0, unit="boards", lat=34.0522, lon=-118.2437))
        # Point far away
        mm.add_request("Receiver B", "Wood", 5.0, "boards", lat=40.7128, lon=-74.0060)
        matches = mm.process_matches(max_distance_km=50.0)
        self.assertEqual(len(matches), 0)

    def test_geo_mapper(self):
        geo = LocalResourceMapper()
        geo.add_point(0.0, 0.0, "Point A", "Category A", "Desc")
        json_str = geo.to_geojson()
        self.assertIn("FeatureCollection", json_str)

if __name__ == "__main__":
    unittest.main()
