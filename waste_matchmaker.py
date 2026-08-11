import json
from typing import List, Dict

class WasteMatchmaker:
    """
    A simple matchmaking algorithm to connect businesses with excess materials
    to organizations that need them.
    """
    def __init__(self):
        self.donations = []
        self.requests = []

    def load_data(self):
        # In a real-world scenario, this would load from a database or API.
        # For now, we are using mock data to demonstrate the logic.
        self.donations = [
            {"id": 1, "donor": "Local Bakery", "item_type": "food", "quantity": 50, "unit": "loaves"},
            {"id": 2, "donor": "Construction Co.", "item_type": "lumber", "quantity": 200, "unit": "planks"},
            {"id": 3, "donor": "Tech Office", "item_type": "electronics", "quantity": 15, "unit": "monitors"}
        ]
        
        self.requests = [
            {"id": 101, "receiver": "Downtown Shelter", "item_type": "food", "quantity_needed": 30},
            {"id": 102, "receiver": "Community Garden", "item_type": "lumber", "quantity_needed": 50},
            {"id": 103, "receiver": "Afterschool Program", "item_type": "electronics", "quantity_needed": 10},
            {"id": 104, "receiver": "Food Bank", "item_type": "food", "quantity_needed": 100}
        ]

    def find_matches(self) -> List[Dict]:
        """Finds overlapping needs and supplies based on item_type."""
        matches = []
        for req in self.requests:
            for don in self.donations:
                if req["item_type"] == don["item_type"] and don["quantity"] > 0:
                    # Calculate how much can be fulfilled
                    amount_to_give = min(req["quantity_needed"], don["quantity"])
                    
                    if amount_to_give > 0:
                        matches.append({
                            "donor": don["donor"],
                            "receiver": req["receiver"],
                            "item_type": req["item_type"],
                            "amount_matched": amount_to_give,
                            "unit": don.get("unit", "items")
                        })
                        
                        # Deduct from donation pool and request pool
                        don["quantity"] -= amount_to_give
                        req["quantity_needed"] -= amount_to_give
                        
        return matches

if __name__ == "__main__":
    print("🌱 Initializing EcoHuman-Nexus Waste Matchmaker...")
    matchmaker = WasteMatchmaker()
    matchmaker.load_data()
    
    print("\n🔍 Searching for matches...")
    successful_matches = matchmaker.find_matches()
    
    print("\n✅ Matches Found:")
    for match in successful_matches:
        print(f"  -> {match['donor']} will provide {match['amount_matched']} {match['unit']} of {match['item_type']} to {match['receiver']}.")
    
    print("\n🌍 Together, we are keeping resources out of landfills!")
