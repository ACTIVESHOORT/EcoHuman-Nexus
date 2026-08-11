import argparse
from ecohuman.matchmaker import AdvancedMatchmaker, ResourceItem
from ecohuman.carbon import CarbonTracker
from ecohuman.geo import LocalResourceMapper
from ecohuman.policy import PolicyTracker

def main():
    parser = argparse.ArgumentParser(description="EcoHuman-Nexus Core Framework CLI")
    parser.add_argument("--max-distance", type=float, default=50.0, help="Maximum matching distance in kilometers")
    args = parser.parse_args()

    print("--------------------------------------------------")
    print("EcoHuman-Nexus System Engine v0.2.1")
    print("--------------------------------------------------")

    # 1. Matchmaker Demo
    print("\n[1] Waste-to-Resource Haversine Matching Engine")
    mm = AdvancedMatchmaker()
    mm.add_donation(ResourceItem(entity_name="City Bakery", item_type="Surplus Flour", quantity=100.0, unit="kg", lat=34.0522, lon=-118.2437))
    mm.add_request(receiver="Community Kitchen", item_type="Surplus Flour", quantity_needed=60.0, unit="kg", lat=34.0622, lon=-118.2537)
    matches = mm.process_matches(max_distance_km=args.max_distance)
    for m in matches:
        print(f"  -> MATCH: {m.donor} -> {m.receiver} | {m.amount_matched} {m.unit} of {m.item_type} (Dist: {m.distance_km} km)")

    # 2. Carbon Tracker Demo
    print("\n[2] GHG Emission Inventory Engine")
    tracker = CarbonTracker("Green Bakery")
    res = tracker.calculate_footprint({"electricity_kwh": 1200, "natural_gas_therms": 45})
    print(f"  -> Calculated Footprint: {res['total_kg_co2e']} kg CO2e ({res['total_metric_tons_co2e']} MT)")

    # 3. Geo Mapper Demo
    print("\n[3] GIS Resource Map Generator")
    geo = LocalResourceMapper()
    geo.add_point(34.0522, -118.2437, "Downtown Clean Water Station", "Water", "Public filtration unit")
    print("  -> GeoJSON FeatureCollection generated successfully.")

    # 4. Policy Tracker
    print("\n[4] Municipal Policy Parser")
    policy = PolicyTracker()
    latest = policy.get_latest_policies()
    print(f"  -> Policy: {latest[0]['title']} [{latest[0]['status']}]")
    print("\n--------------------------------------------------")

if __name__ == "__main__":
    main()
