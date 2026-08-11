"""
Environmental Policy Tracker & Scraper Interface.
"""
from typing import List, Dict

class PolicyTracker:
    def __init__(self):
        self.mock_policies = [
            {
                "title": "Local Urban Canopy Protection Act",
                "jurisdiction": "City Level",
                "status": "Under Review",
                "impact": "High - Requires 30% tree canopy maintenance for new developments."
            },
            {
                "title": "Single-Use Plastic Ban Expansion",
                "jurisdiction": "State Level",
                "status": "Passed",
                "impact": "Medium - Prohibits styrofoam containers in food service."
            }
        ]

    def get_latest_policies(self, topic_keyword: str = None) -> List[Dict]:
        if not topic_keyword:
            return self.mock_policies
        
        return [
            p for p in self.mock_policies 
            if topic_keyword.lower() in p["title"].lower() or topic_keyword.lower() in p["impact"].lower()
        ]
