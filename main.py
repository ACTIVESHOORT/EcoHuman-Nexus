import argparse
from ecohuman.matchmaker import AdvancedMatchmaker, ResourceItem
from ecohuman.carbon import CarbonTracker
from ecohuman.geo import LocalResourceMapper
from ecohuman.policy import PolicyTracker

def main():
    parser = argparse.ArgumentParser(description="EcoHuman-Nexus Toolkit CLI")
    parser.add_argument("--demo", action="store_true", help="Run full suite demonstration")
    args = parser.parse_args()

    print("==================================================")
    print("[+] EcoHuman-Nexus Framework v0.2.0")
    print("==================================================")

    # 1. Matchmaker Demo
    print("\n[1] Waste-to-Resource Matchmaker Database Engine")
    mm = AdvancedMatchmaker()
    mm.add_donation(ResourceItem(entity_name="City Bakery", item_type="Surplus Flour", quantity=100.0, unit="kg", location_zip="90210"))
    mm.add_request(receiver="Community Kitchen", item_type="Surplus Flour", quantity_needed=60.0, unit="kg", location_zip="90210")
    matches = mm.process_matches()
    for m in matches:
        print(f"  -> MATCH: {m.donor} provides {m.amount_matched} {m.unit} of {m.item_type} to {m.receiver}")

    # 2. Carbon Tracker Demo
    print("\n[2] Carbon Footprint Estimator")
    tracker = CarbonTracker("Green Bakery")
    res = tracker.calculate_footprint({"electricity_kwh": 1200, "natural_gas_therms": 45})
    print(f"  -> Total Carbon Footprint: {res['total_kg_co2e']} kg CO2e ({res['total_metric_tons_co2e']} Metric Tons)")

    # 3. Geo Mapper Demo
    print("\n[3] Local Resource GeoJSON Generator")
    geo = LocalResourceMapper()
    geo.add_point(34.0522, -118.2437, "Downtown Clean Water Station", "Water", "Public accessible water filtration point")
    print("  -> GeoJSON generated successfully.")

    # 4. Policy Tracker
    print("\n[4] Environmental Policy Tracker")
    policy = PolicyTracker()
    latest = policy.get_latest_policies()
    print(f"  -> Active Policy Monitored: '{latest[0]['title']}' ({latest[0]['status']})")
    print("\n==================================================")

if __name__ == "__main__":
    main()
