class SmartShoppingEngine:
    def __init__(self):
        self.suggested_items = []

    def generate_shopping_list(self, inventory_items):
        """Auto-generates smart shopping list based on low stock or expired items."""
        shopping_list = []
        
        # Check expired items that need replacement
        for item in inventory_items:
            if item["status"] == "Expired":
                shopping_list.append({
                    "name": item["name"],
                    "category": item["category"],
                    "reason": "Expired - Needs Replacement",
                    "quantity": "1 Unit",
                    "est_cost": "₹60 - ₹120",
                    "priority": "High"
                })
            elif item["status"] == "Expiring Soon":
                shopping_list.append({
                    "name": item["name"],
                    "category": item["category"],
                    "reason": "Expiring Soon - Restock Buffer",
                    "quantity": "1 Unit",
                    "est_cost": "₹50 - ₹150",
                    "priority": "Medium"
                })
                
        # Recommended staples if not present
        names = [i["name"] for i in inventory_items]
        staples = [
            {"name": "Boiled Milk", "category": "Dairy", "est_cost": "₹35", "priority": "High"},
            {"name": "Curd / Dahi", "category": "Dairy", "est_cost": "₹45", "priority": "Medium"},
            {"name": "Fresh Tomato", "category": "Vegetable", "est_cost": "₹40", "priority": "Medium"},
            {"name": "Eggs", "category": "Protein", "est_cost": "₹80", "priority": "Low"},
        ]
        
        for staple in staples:
            if staple["name"] not in names and not any(s["name"] == staple["name"] for s in shopping_list):
                shopping_list.append({
                    "name": staple["name"],
                    "category": staple["category"],
                    "reason": "Essential Kitchen Staple Low",
                    "quantity": "Standard Pack",
                    "est_cost": staple["est_cost"],
                    "priority": staple["priority"]
                })
                
        return shopping_list

if __name__ == "__main__":
    shop = SmartShoppingEngine()
    print("Smart Shopping Engine Initialized.")
