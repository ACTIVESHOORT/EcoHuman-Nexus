"""
Carbon Emissions Estimator Module for Small Businesses and Community Groups.
"""
from typing import Dict

class CarbonTracker:
    # Average emission factors (kg CO2e per unit)
    EMISSION_FACTORS = {
        "electricity_kwh": 0.385,  # kg CO2e per kWh
        "natural_gas_therms": 5.3,  # kg CO2e per therm
        "gasoline_gallons": 8.89,   # kg CO2e per gallon
        "diesel_gallons": 10.18,   # kg CO2e per gallon
        "waste_landfill_kg": 0.45   # kg CO2e per kg waste
    }

    def __init__(self, entity_name: str):
        self.entity_name = entity_name

    def calculate_footprint(self, usage_data: Dict[str, float]) -> Dict[str, float]:
        """
        Calculates Scope 1 & Scope 2 carbon footprint in kg CO2e.
        """
        breakdown = {}
        total_co2e = 0.0

        for key, amount in usage_data.items():
            if key in self.EMISSION_FACTORS:
                emissions = amount * self.EMISSION_FACTORS[key]
                breakdown[key] = round(emissions, 2)
                total_co2e += emissions

        breakdown["total_kg_co2e"] = round(total_co2e, 2)
        breakdown["total_metric_tons_co2e"] = round(total_co2e / 1000.0, 4)
        return breakdown
