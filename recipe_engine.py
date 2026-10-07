class RecipeRecommendationEngine:
    def __init__(self):
        self.recipe_db = [
            {
                "id": "REC-01",
                "title": "Quick Leftover Fried Rice",
                "category": "Traditional Quick Fix",
                "key_ingredient": "Leftover Rice",
                "matching_ingredients": ["Leftover Rice", "Veg Curry / Sabzi", "Fresh Tomato"],
                "prep_time": "10 mins",
                "calories": "320 kcal",
                "protein": "6.5g",
                "carbs": "58g",
                "fat": "7.0g",
                "steps": [
                    "Heat 1 tbsp oil in a wok or pan over medium flame.",
                    "Sauté diced tomatoes and leftover veg sabzi for 2 minutes.",
                    "Add cold leftover rice, splash 1 tsp soy sauce, salt, and pepper.",
                    "Toss on high heat for 3 minutes until steaming hot and serve fresh."
                ],
                "waste_reduction_note": "Uses 1-day old rice and leftover vegetables to save food from going stale!"
            },
            {
                "id": "REC-02",
                "title": "Creamy Paneer & Veg Curry Delight",
                "category": "Main Course",
                "key_ingredient": "Curd / Dahi",
                "matching_ingredients": ["Curd / Dahi", "Fresh Tomato", "Boiled Milk"],
                "prep_time": "20 mins",
                "calories": "290 kcal",
                "protein": "12.0g",
                "carbs": "14g",
                "fat": "18.0g",
                "steps": [
                    "Whisk fresh curd with turmeric, coriander powder, and garam masala.",
                    "Puree ripe tomatoes and cook with ginger-garlic paste in 1 tbsp ghee.",
                    "Stir in the spiced curd mixture slowly to avoid curdling.",
                    "Simmer with paneer cubes or mixed veggies for 10 minutes."
                ],
                "waste_reduction_note": "Consumes expiring curd and tomatoes efficiently."
            },
            {
                "id": "REC-03",
                "title": "South Indian Sambar Rice (Bisibelebath Style)",
                "category": "Traditional Comfort Food",
                "key_ingredient": "Sambar",
                "matching_ingredients": ["Sambar", "Leftover Rice"],
                "prep_time": "12 mins",
                "calories": "280 kcal",
                "protein": "9.0g",
                "carbs": "52g",
                "fat": "4.5g",
                "steps": [
                    "In a pot, combine leftover sambar and leftover rice with 1/2 cup water.",
                    "Simmer on low flame for 7 minutes until well blended.",
                    "Temper with mustard seeds, curry leaves, and a tsp of ghee.",
                    "Serve hot with papad or curd."
                ],
                "waste_reduction_note": "Perfectly utilizes remaining sambar and rice in 15 mins!"
            },
            {
                "id": "REC-04",
                "title": "Crispy Golden Dosa with Coconut Chutney",
                "category": "Breakfast / Snack",
                "key_ingredient": "Dosa / Idli Batter",
                "matching_ingredients": ["Dosa / Idli Batter", "Chutney (Coconut/Tomato)"],
                "prep_time": "15 mins",
                "calories": "240 kcal",
                "protein": "5.5g",
                "carbs": "44g",
                "fat": "5.0g",
                "steps": [
                    "Heat a non-stick tawa pan and grease lightly with oil.",
                    "Pour a ladle of fermented Dosa batter and spread in thin concentric circles.",
                    "Drizzle oil around edges, cook until golden and crisp.",
                    "Fold and serve hot with coconut/tomato chutney."
                ],
                "waste_reduction_note": "Uses fermented batter at its peak flavor."
            },
            {
                "id": "REC-05",
                "title": "Nutritious Spinach & Tomato Kadhi",
                "category": "Healthy Light Soup",
                "key_ingredient": "Spinach / Greens",
                "matching_ingredients": ["Spinach / Greens", "Boiled Milk", "Fresh Tomato"],
                "prep_time": "15 mins",
                "calories": "160 kcal",
                "protein": "7.0g",
                "carbs": "12g",
                "fat": "8.0g",
                "steps": [
                    "Wash and finely chop fresh spinach leaves.",
                    "Sauté mustard seeds, green chilies, and spinach for 3 minutes.",
                    "Add warm milk mixed with 1 tbsp besan (gram flour).",
                    "Season with salt, cumin, simmer for 5 minutes and serve warm."
                ],
                "waste_reduction_note": "Prevents spinach leaves from wilting."
            }
        ]

    def get_recommendations(self, inventory_items):
        """Finds best matching recipes based on current inventory items."""
        available_names = [item["name"] for item in inventory_items]
        expiring_names = [item["name"] for item in inventory_items if item["status"] in ["Expiring Soon", "Moderate"]]
        
        ranked_recipes = []
        for recipe in self.recipe_db:
            matched = [ing for ing in recipe["matching_ingredients"] if ing in available_names]
            match_score = len(matched)
            has_expiring = any(ing in expiring_names for ing in matched)
            
            priority_score = match_score * 10 + (15 if has_expiring else 0)
            
            ranked_recipes.append({
                "recipe": recipe,
                "matched_ingredients": matched,
                "missing_ingredients": [ing for ing in recipe["matching_ingredients"] if ing not in available_names],
                "priority_score": priority_score,
                "expiring_used": has_expiring
            })
            
        ranked_recipes.sort(key=lambda x: x["priority_score"], reverse=True)
        return ranked_recipes

if __name__ == "__main__":
    engine = RecipeRecommendationEngine()
    print("Recipe Engine Loaded with", len(engine.recipe_db), "recipes.")
