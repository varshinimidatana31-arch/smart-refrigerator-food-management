import json
import os
from datetime import datetime, timedelta

DEFAULT_INVENTORY_FILE = os.path.join(os.path.dirname(__file__), "inventory_data.json")

INITIAL_INVENTORY = [
    {
        "id": "FS-101",
        "name": "Leftover Rice",
        "category": "Traditional Leftover",
        "quantity": "1 Bowl (350g)",
        "added_date": "2026-10-06",
        "expiry_date": "2026-10-09",
        "days_remaining": 2,
        "freshness_pct": 88,
        "status": "Fresh",
        "location": "Middle Shelf",
        "icon": "🍚"
    },
    {
        "id": "FS-102",
        "name": "Boiled Milk",
        "category": "Dairy / Traditional",
        "quantity": "500 ml",
        "added_date": "2026-10-07",
        "expiry_date": "2026-10-08",
        "days_remaining": 1,
        "freshness_pct": 65,
        "status": "Expiring Soon",
        "location": "Door Shelf",
        "icon": "🥛"
    },
    {
        "id": "FS-103",
        "name": "Chicken Curry",
        "category": "Traditional Leftover",
        "quantity": "1 Container (400g)",
        "added_date": "2026-10-05",
        "expiry_date": "2026-10-08",
        "days_remaining": 1,
        "freshness_pct": 58,
        "status": "Expiring Soon",
        "location": "Top Shelf",
        "icon": "🥘"
    },
    {
        "id": "FS-104",
        "name": "Curd / Dahi",
        "category": "Dairy / Traditional",
        "quantity": "1 Container (300g)",
        "added_date": "2026-10-06",
        "expiry_date": "2026-10-10",
        "days_remaining": 3,
        "freshness_pct": 92,
        "status": "Fresh",
        "location": "Middle Shelf",
        "icon": "🥣"
    },
    {
        "id": "FS-105",
        "name": "Sambar",
        "category": "Traditional Leftover",
        "quantity": "1 Container (450g)",
        "added_date": "2026-10-04",
        "expiry_date": "2026-10-06",
        "days_remaining": 0,
        "freshness_pct": 25,
        "status": "Expired",
        "location": "Top Shelf",
        "icon": "🍲"
    },
    {
        "id": "FS-106",
        "name": "Fresh Apple",
        "category": "Fresh Fruit",
        "quantity": "6 Pcs",
        "added_date": "2026-10-02",
        "expiry_date": "2026-10-16",
        "days_remaining": 9,
        "freshness_pct": 95,
        "status": "Fresh",
        "location": "Crisper Drawer",
        "icon": "🍎"
    },
    {
        "id": "FS-107",
        "name": "Fresh Tomato",
        "category": "Fresh Vegetable",
        "quantity": "1 kg",
        "added_date": "2026-10-03",
        "expiry_date": "2026-10-10",
        "days_remaining": 3,
        "freshness_pct": 89,
        "status": "Fresh",
        "location": "Crisper Drawer",
        "icon": "🍅"
    },
    {
        "id": "FS-108",
        "name": "Spinach / Greens",
        "category": "Fresh Vegetable",
        "quantity": "1 Bunch",
        "added_date": "2026-10-06",
        "expiry_date": "2026-10-08",
        "days_remaining": 1,
        "freshness_pct": 62,
        "status": "Expiring Soon",
        "location": "Crisper Drawer",
        "icon": "🥬"
    },
    {
        "id": "FS-109",
        "name": "Dosa / Idli Batter",
        "category": "Traditional Batter",
        "quantity": "1 Pack (1kg)",
        "added_date": "2026-10-05",
        "expiry_date": "2026-10-09",
        "days_remaining": 2,
        "freshness_pct": 84,
        "status": "Fresh",
        "location": "Door Shelf",
        "icon": "🫓"
    }
]

class InventoryManager:
    def __init__(self, filepath=DEFAULT_INVENTORY_FILE):
        self.filepath = filepath
        self.items = self.load_inventory()

    def load_inventory(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    return json.load(f)
            except Exception:
                pass
        self.save_inventory(INITIAL_INVENTORY)
        return INITIAL_INVENTORY

    def save_inventory(self, items=None):
        if items is not None:
            self.items = items
        with open(self.filepath, "w") as f:
            json.dump(self.items, f, indent=2)

    def get_summary(self):
        total = len(self.items)
        fresh = sum(1 for item in self.items if item["status"] == "Fresh")
        expiring_soon = sum(1 for item in self.items if item["status"] == "Expiring Soon")
        expired = sum(1 for item in self.items if item["status"] == "Expired")
        return {
            "total": total,
            "fresh": fresh,
            "expiring_soon": expiring_soon,
            "expired": expired
        }

    def add_item(self, name, category, quantity, days_left, freshness_pct, status, location="Middle Shelf", icon="📦"):
        today = datetime.now()
        expiry = today + timedelta(days=days_left)
        new_item = {
            "id": f"FS-{len(self.items) + 101}",
            "name": name,
            "category": category,
            "quantity": quantity,
            "added_date": today.strftime("%Y-%m-%d"),
            "expiry_date": expiry.strftime("%Y-%m-%d"),
            "days_remaining": days_left,
            "freshness_pct": freshness_pct,
            "status": status,
            "location": location,
            "icon": icon
        }
        self.items.insert(0, new_item)
        self.save_inventory()
        return new_item

    def delete_item(self, item_id):
        self.items = [item for item in self.items if item["id"] != item_id]
        self.save_inventory()

if __name__ == "__main__":
    inv = InventoryManager()
    print("Inventory Loaded Summary:", inv.get_summary())
