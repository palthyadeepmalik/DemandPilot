import pandas as pd
from pathlib import Path
import random

BASE_DIR = Path(__file__).resolve().parents[1]

DATASET_DIR = BASE_DIR / "datasets" / "pizza_sales"

pizza_types = pd.read_csv(DATASET_DIR / "pizza_types.csv", encoding="cp1252")

recipe_rows = []

all_ingredients = set()

for _, row in pizza_types.iterrows():

    pizza_type_id = row["pizza_type_id"]

    ingredients = row["ingredients"].split(",")

    for ingredient in ingredients:

        ingredient = ingredient.strip()

        all_ingredients.add(ingredient)

        recipe_rows.append({
            "pizza_type_id": pizza_type_id,
            "ingredient": ingredient,
            "quantity": round(random.uniform(0.05, 0.35), 2),
            "unit": "kg"
        })

recipe_df = pd.DataFrame(recipe_rows)

recipe_df.to_csv(
    DATASET_DIR / "recipe_mapping.csv",
    index=False
)

inventory_rows = []

for ingredient in sorted(all_ingredients):

    inventory_rows.append({
        "ingredient": ingredient,
        "quantity_available": random.randint(40, 120),
        "unit": "kg"
    })

inventory_df = pd.DataFrame(inventory_rows)

inventory_df.to_csv(
    DATASET_DIR / "inventory.csv",
    index=False
)

print("=" * 60)
print("Recipe Mapping Rows :", len(recipe_df))
print("Inventory Rows      :", len(inventory_df))
print("=" * 60)
print("Files generated successfully!")