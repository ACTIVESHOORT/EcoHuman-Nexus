import sqlite3
import math
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class ResourceItem:
    entity_name: str
    item_type: str
    quantity: float
    unit: str
    lat: float
    lon: float
    id: Optional[int] = None

@dataclass
class MatchResult:
    donor: str
    receiver: str
    item_type: str
    amount_matched: float
    unit: str
    distance_km: float

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) in kilometers.
    """
    r = 6371.0  # Radius of Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(r * c, 2)

class AdvancedMatchmaker:
    """
    Production-grade SQLite-backed Waste-to-Resource Matchmaking Engine
    incorporating geospatial Haversine proximity scoring.
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
                    lat REAL NOT NULL,
                    lon REAL NOT NULL
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    receiver TEXT NOT NULL,
                    item_type TEXT NOT NULL,
                    quantity_needed REAL NOT NULL,
                    unit TEXT NOT NULL,
                    lat REAL NOT NULL,
                    lon REAL NOT NULL
                )
            """)

    def add_donation(self, donation: ResourceItem):
        with self.conn:
            self.conn.execute(
                "INSERT INTO donations (donor, item_type, quantity, unit, lat, lon) VALUES (?, ?, ?, ?, ?, ?)",
                (donation.entity_name, donation.item_type, donation.quantity, donation.unit, donation.lat, donation.lon)
            )

    def add_request(self, receiver: str, item_type: str, quantity_needed: float, unit: str, lat: float, lon: float):
        with self.conn:
            self.conn.execute(
                "INSERT INTO requests (receiver, item_type, quantity_needed, unit, lat, lon) VALUES (?, ?, ?, ?, ?, ?)",
                (receiver, item_type, quantity_needed, unit, lat, lon)
            )

    def process_matches(self, max_distance_km: float = 50.0) -> List[MatchResult]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, donor, item_type, quantity, unit, lat, lon FROM donations WHERE quantity > 0")
        donations = cursor.fetchall()

        cursor.execute("SELECT id, receiver, item_type, quantity_needed, unit, lat, lon FROM requests WHERE quantity_needed > 0")
        requests = cursor.fetchall()

        results = []
        for req in requests:
            req_id, receiver, req_type, req_qty, req_unit, r_lat, r_lon = req
            for don in donations:
                don_id, donor, don_type, don_qty, don_unit, d_lat, d_lon = don
                
                if req_type.lower() == don_type.lower() and don_qty > 0:
                    dist = haversine_distance(r_lat, r_lon, d_lat, d_lon)
                    if dist <= max_distance_km:
                        matched_qty = min(req_qty, don_qty)
                        if matched_qty > 0:
                            results.append(MatchResult(
                                donor=donor,
                                receiver=receiver,
                                item_type=req_type,
                                amount_matched=matched_qty,
                                unit=don_unit,
                                distance_km=dist
                            ))
                            don_qty -= matched_qty
                            req_qty -= matched_qty

        return results
