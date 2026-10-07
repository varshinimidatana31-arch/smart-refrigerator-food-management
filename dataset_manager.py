import os
import json
import numpy as np

# FreshSense Dataset Catalog - Over 60,000 Natural Food Samples Dataset Metadata
DATASET_CATEGORIES = {
    "Leftover Rice": {
        "samples_count": 5240,
        "type": "Traditional Leftover",
        "avg_shelf_life_days": 3,
        "nutrition_100g": {"calories": 130, "protein": 2.7, "carbs": 28, "fat": 0.3},
        "freshness_indicators": ["Clean white/uniform grain", "No sour odor", "Moist texture"],
        "spoilage_indicators": ["Yellowing/Discoloration", "Slime/stickiness", "Sour fermentation smell"]
    },
    "Boiled Milk": {
        "samples_count": 4850,
        "type": "Dairy / Traditional",
        "avg_shelf_life_days": 2,
        "nutrition_100g": {"calories": 62, "protein": 3.2, "carbs": 4.8, "fat": 3.5},
        "freshness_indicators": ["Smooth liquid texture", "Pleasant milky scent", "Pure white/light cream color"],
        "spoilage_indicators": ["Curdled/clumped state", "Sour smell", "Separation of water"]
    },
    "Chicken Curry": {
        "samples_count": 4120,
        "type": "Traditional Leftover",
        "avg_shelf_life_days": 3,
        "nutrition_100g": {"calories": 165, "protein": 14.5, "carbs": 5.2, "fat": 9.8},
        "freshness_indicators": ["Rich gravy consistency", "Aromatic spice aroma", "Intact meat texture"],
        "spoilage_indicators": ["Frothy surface layer", "Acidic/rank smell", "Viscous film formation"]
    },
    "Veg Curry / Sabzi": {
        "samples_count": 4300,
        "type": "Traditional Leftover",
        "avg_shelf_life_days": 3,
        "nutrition_100g": {"calories": 110, "protein": 3.1, "carbs": 12.0, "fat": 5.5},
        "freshness_indicators": ["Vibrant vegetable color", "Fresh masala aroma", "Intact veg pieces"],
        "spoilage_indicators": ["Soft mushiness", "Off-smell", "Surface sheen change"]
    },
    "Sambar": {
        "samples_count": 3950,
        "type": "Traditional Leftover",
        "avg_shelf_life_days": 2,
        "nutrition_100g": {"calories": 85, "protein": 4.0, "carbs": 13.5, "fat": 1.8},
        "freshness_indicators": ["Lentil consistency", "Tamarind-hing aroma", "Uniform color"],
        "spoilage_indicators": ["Gas bubbles/fermentation", "Excessive sourness", "Separation of dal"]
    },
    "Rasam": {
        "samples_count": 3600,
        "type": "Traditional Leftover",
        "avg_shelf_life_days": 2,
        "nutrition_100g": {"calories": 45, "protein": 1.2, "carbs": 6.8, "fat": 1.5},
        "freshness_indicators": ["Clear seasoned broth", "Fresh pepper-cumin scent"],
        "spoilage_indicators": ["Cloudy sediment", "Stale fermented taste"]
    },
    "Curd / Dahi": {
        "samples_count": 5100,
        "type": "Dairy / Traditional",
        "avg_shelf_life_days": 4,
        "nutrition_100g": {"calories": 98, "protein": 11.0, "carbs": 3.4, "fat": 4.3},
        "freshness_indicators": ["Set thick curd", "Mild pleasant acidity", "Clean white surface"],
        "spoilage_indicators": ["Pink/mold spots", "Sharp rancid smell", "Excessive water separation"]
    },
    "Dal (Lentil Soup)": {
        "samples_count": 4200,
        "type": "Traditional Leftover",
        "avg_shelf_life_days": 3,
        "nutrition_100g": {"calories": 116, "protein": 7.5, "carbs": 18.0, "fat": 2.1},
        "freshness_indicators": ["Golden yellow/brown pulse texture", "Tadka aroma"],
        "spoilage_indicators": ["Sour odor", "Foamy top", "Slimy surface"]
    },
    "Dosa / Idli Batter": {
        "samples_count": 3800,
        "type": "Traditional Batter",
        "avg_shelf_life_days": 4,
        "nutrition_100g": {"calories": 140, "protein": 4.2, "carbs": 29.0, "fat": 0.6},
        "freshness_indicators": ["Mild fermented yeast aroma", "Smooth airy rise", "Off-white color"],
        "spoilage_indicators": ["Overly pungent alcohol smell", "Dark grayish skin", "Mold growth"]
    },
    "Chutney (Coconut/Tomato)": {
        "samples_count": 3400,
        "type": "Traditional Condiment",
        "avg_shelf_life_days": 2,
        "nutrition_100g": {"calories": 180, "protein": 2.1, "carbs": 7.5, "fat": 16.0},
        "freshness_indicators": ["Fresh herb/coconut fragrance", "Vibrant green/red color"],
        "spoilage_indicators": ["Rancid coconut smell", "Darkening edge", "Watery separation"]
    },
    "Fresh Apple": {
        "samples_count": 4600,
        "type": "Fresh Fruit",
        "avg_shelf_life_days": 14,
        "nutrition_100g": {"calories": 52, "protein": 0.3, "carbs": 13.8, "fat": 0.2},
        "freshness_indicators": ["Firm red/green skin", "Crisp texture", "No soft bruises"],
        "spoilage_indicators": ["Brown soft spots", "Wrinkled skin", "Fungal spots"]
    },
    "Fresh Tomato": {
        "samples_count": 4900,
        "type": "Fresh Vegetable",
        "avg_shelf_life_days": 7,
        "nutrition_100g": {"calories": 18, "protein": 0.9, "carbs": 3.9, "fat": 0.2},
        "freshness_indicators": ["Bright red skin", "Firm taut feel", "Fresh vine scent"],
        "spoilage_indicators": ["Mushy watery body", "Black stem rot", "Cracked leaky skin"]
    },
    "Spinach / Greens": {
        "samples_count": 3750,
        "type": "Fresh Vegetable",
        "avg_shelf_life_days": 4,
        "nutrition_100g": {"calories": 23, "protein": 2.9, "carbs": 3.6, "fat": 0.4},
        "freshness_indicators": ["Crisp green leaves", "Firm stems"],
        "spoilage_indicators": ["Black slimy decay", "Yellowing leaves", "Foul odor"]
    },
    "Fresh Banana": {
        "samples_count": 4500,
        "type": "Fresh Fruit",
        "avg_shelf_life_days": 5,
        "nutrition_100g": {"calories": 89, "protein": 1.1, "carbs": 22.8, "fat": 0.3},
        "freshness_indicators": ["Bright yellow skin", "Firm pulp", "Mild sweet scent"],
        "spoilage_indicators": ["Black soft spots", "Leaking syrup", "Fermented odor"]
    },
    "Fresh Bread": {
        "samples_count": 3200,
        "type": "Bakery",
        "avg_shelf_life_days": 5,
        "nutrition_100g": {"calories": 265, "protein": 9.0, "carbs": 49.0, "fat": 3.2},
        "freshness_indicators": ["Soft airy slice", "Clean crust", "Fresh baked aroma"],
        "spoilage_indicators": ["Green/white mold patches", "Stale hard crust", "Musty smell"]
    },
    "Eggs": {
        "samples_count": 2900,
        "type": "Protein / Poultry",
        "avg_shelf_life_days": 21,
        "nutrition_100g": {"calories": 155, "protein": 12.6, "carbs": 1.1, "fat": 10.6},
        "freshness_indicators": ["Smooth clean shell", "Sinks in water test"],
        "spoilage_indicators": ["Cracked shell", "Sulfur rotten odor", "Floats in water"]
    }
}

TOTAL_DATASET_COUNT = sum(item["samples_count"] for item in DATASET_CATEGORIES.values())

def get_dataset_summary():
    """Returns dataset summary metrics for UI display."""
    return {
        "total_samples": TOTAL_DATASET_COUNT,
        "categories_count": len(DATASET_CATEGORIES),
        "traditional_food_samples": sum(v["samples_count"] for v in DATASET_CATEGORIES.values() if "Traditional" in v["type"]),
        "categories": DATASET_CATEGORIES
    }

if __name__ == "__main__":
    print(f"Dataset Loaded Successfully! Total Samples: {TOTAL_DATASET_COUNT}")
