import sqlite3
import json
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class ResourceItem:
    entity_name: str
    item_type: str
    quantity: float
    unit: str
    location_zip: str
    id: Optional[int] = None

@dataclass
class MatchResult:
    donor: str
    receiver: str
    item_type: str
    amount_matched: float
    unit: str

class AdvancedMatchmaker:
    """
    Production-grade SQLite-backed Waste-to-Resource Matchmaking Engine.
    """
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS donations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    donor TEXT NOT NULL,
                    item_type TEXT NOT NULL,
                    quantity REAL NOT NULL,
                    unit TEXT NOT NULL,
                    location_zip TEXT NOT NULL
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    receiver TEXT NOT NULL,
                    item_type TEXT NOT NULL,
                    quantity_needed REAL NOT NULL,
                    unit TEXT NOT NULL,
                    location_zip TEXT NOT NULL
                )
            """)

    def add_donation(self, donation: ResourceItem):
        with self.conn:
            self.conn.execute(
                "INSERT INTO donations (donor, item_type, quantity, unit, location_zip) VALUES (?, ?, ?, ?, ?)",
                (donation.entity_name, donation.item_type, donation.quantity, donation.unit, donation.location_zip)
            )

    def add_request(self, receiver: str, item_type: str, quantity_needed: float, unit: str, location_zip: str):
        with self.conn:
            self.conn.execute(
                "INSERT INTO requests (receiver, item_type, quantity_needed, unit, location_zip) VALUES (?, ?, ?, ?, ?)",
                (receiver, item_type, quantity_needed, unit, location_zip)
            )

    def process_matches(self) -> List[MatchResult]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, donor, item_type, quantity, unit, location_zip FROM donations WHERE quantity > 0")
        donations = cursor.fetchall()

        cursor.execute("SELECT id, receiver, item_type, quantity_needed, unit, location_zip FROM requests WHERE quantity_needed > 0")
        requests = cursor.fetchall()

        results = []
        for req in requests:
            req_id, receiver, req_type, req_qty, req_unit, req_zip = req
            for don in donations:
                don_id, donor, don_type, don_qty, don_unit, don_zip = don
                
                if req_type.lower() == don_type.lower() and don_qty > 0:
                    matched_qty = min(req_qty, don_qty)
                    if matched_qty > 0:
                        results.append(MatchResult(
                            donor=donor,
                            receiver=receiver,
                            item_type=req_type,
                            amount_matched=matched_qty,
                            unit=don_unit
                        ))
                        # Update state
                        don_qty -= matched_qty
                        req_qty -= matched_qty

        return results
