from sqlalchemy import text
from decimal import Decimal
from pathlib import Path

from app.models.recipe import Recipe
from app.models.ingredient import Ingredient

import pandas as pd
from sqlalchemy.orm import Session

from app.models import (
    Order,
    OrderDetail,
    Pizza,
    PizzaType,
)

from app.models.recipe_mapping import RecipeMapping
from app.models.inventory import Inventory



BASE_DIR = Path(__file__).resolve().parents[3]

PIZZA_DATASET_DIR = BASE_DIR / "datasets" / "pizza_sales"

RECIPE_MAPPING_PATH = BASE_DIR / "datasets" / "pizza_sales" / "recipe_mapping.csv"

INVENTORY_PATH = BASE_DIR / "datasets" / "pizza_sales" / "inventory.csv"



def read_csv(file_path: Path):
    return pd.read_csv(file_path, encoding="cp1252")


class CSVImportService:

    def __init__(self, db: Session):
        self.db = db

    def import_recipe_mapping(self):
        print("\n========== IMPORTING RECIPE MAPPING ==========")

        print("Reading:", RECIPE_MAPPING_PATH)

        recipe_df = read_csv(RECIPE_MAPPING_PATH)

        print(recipe_df.head())
        print("Recipe rows found:", len(recipe_df))

        recipes = [
            RecipeMapping(
                pizza_type_id=row["pizza_type_id"],
                ingredient=row["ingredient"],
                quantity=Decimal(str(row["quantity"])),
                unit=row["unit"],
            )
            for _, row in recipe_df.iterrows()
        ]

        print("Recipe objects created:", len(recipes))

        self.db.bulk_save_objects(recipes)

        print("Recipe Mapping imported successfully!")

        return len(recipes)

    def import_inventory(self):
        print("\n========== IMPORTING INVENTORY ==========")

        print("Reading:", INVENTORY_PATH)

        inventory_df = read_csv(INVENTORY_PATH)

        print(inventory_df.head())
        print("Inventory rows found:", len(inventory_df))

        inventory = [
            Inventory(
                ingredient=row["ingredient"],
                quantity_available=Decimal(str(row["quantity_available"])),
                unit=row["unit"],
            )
            for _, row in inventory_df.iterrows()
        ]

        print("Inventory objects created:", len(inventory))

        self.db.bulk_save_objects(inventory)

        print("Inventory imported successfully!")

        return len(inventory)

    def import_data(self):

        try:
            # Clear existing data
            self.db.execute(text("""
                TRUNCATE TABLE
                    order_details,
                    orders,
                    pizzas,
                    pizza_types,
                    recipe_mapping,
                    inventory
                RESTART IDENTITY CASCADE;
            """))

            # ---------------- Pizza Types ----------------
            pizza_types_df = read_csv(PIZZA_DATASET_DIR / "pizza_types.csv")

            pizza_types = [
                PizzaType(
                    pizza_type_id=row["pizza_type_id"],
                    name=row["name"],
                    category=row["category"],
                    ingredients=row["ingredients"],
                )
                for _, row in pizza_types_df.iterrows()
            ]

            self.db.bulk_save_objects(pizza_types)

            # ---------------- Pizzas ----------------
            pizzas_df = read_csv(PIZZA_DATASET_DIR / "pizzas.csv")

            pizzas = [
                Pizza(
                    pizza_id=row["pizza_id"],
                    pizza_type_id=row["pizza_type_id"],
                    size=row["size"],
                    price=Decimal(str(row["price"])),
                )
                for _, row in pizzas_df.iterrows()
            ]

            self.db.bulk_save_objects(pizzas)

            # ---------------- Orders ----------------
            orders_df = read_csv(PIZZA_DATASET_DIR / "orders.csv")

            orders = [
                Order(
                    order_id=row["order_id"],
                    order_date=pd.to_datetime(
                        row["date"],
                        format="%d/%m/%Y"
                    ).date(),
                    order_time=pd.to_datetime(
                        row["time"],
                        format="%H:%M:%S"
                    ).time(),
                )
                for _, row in orders_df.iterrows()
            ]

            self.db.bulk_save_objects(orders)

            # ---------------- Order Details ----------------
            order_details_df = read_csv(
                PIZZA_DATASET_DIR / "order_details.csv"
            )

            order_details = [
                OrderDetail(
                    order_details_id=row["order_details_id"],
                    order_id=row["order_id"],
                    pizza_id=row["pizza_id"],
                    quantity=row["quantity"],
                )
                for _, row in order_details_df.iterrows()
            ]

            self.db.bulk_save_objects(order_details)

            # ---------------- Recipe Mapping ----------------
            # Uncomment after recipe_mapping.csv is created
            recipe_count = self.import_recipe_mapping()

            # ---------------- Inventory ----------------
            # Uncomment after inventory.csv is created
            inventory_count = self.import_inventory()

            self.db.commit()

            return {
                "pizza_types": len(pizza_types),
                "pizzas": len(pizzas),
                "orders": len(orders),
                "order_details": len(order_details),
                "recipe_mapping": recipe_count,
                "inventory": inventory_count,
                "message": "Dataset imported successfully."
            }

        except Exception as e:
            self.db.rollback()
            raise e