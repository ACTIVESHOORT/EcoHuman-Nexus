import unittest
from ecohuman.matchmaker import AdvancedMatchmaker, ResourceItem
from ecohuman.carbon import CarbonTracker
from ecohuman.geo import LocalResourceMapper

class TestEcoHumanFramework(unittest.TestCase):
    def test_carbon_tracker(self):
        tracker = CarbonTracker("Test Co")
        res = tracker.calculate_footprint({"electricity_kwh": 100})
        self.assertEqual(res["total_kg_co2e"], 38.5)

    def test_matchmaker(self):
        mm = AdvancedMatchmaker()
        mm.add_donation(ResourceItem(entity_name="Donor A", item_type="Wood", quantity=10.0, unit="boards", location_zip="10001"))
        mm.add_request("Receiver B", "Wood", 5.0, "boards", "10001")
        matches = mm.process_matches()
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].amount_matched, 5.0)

    def test_geo_mapper(self):
        geo = LocalResourceMapper()
        geo.add_point(0.0, 0.0, "Point A", "Category A", "Desc")
        json_str = geo.to_geojson()
        self.assertIn("FeatureCollection", json_str)

if __name__ == "__main__":
    unittest.main()
