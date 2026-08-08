from collections import defaultdict

from app.database.session import SessionLocal
from app.repositories.recipe_repository import RecipeRepository
from app.services.prediction_service import PredictionService


class InventoryService:

    @staticmethod
    def calculate_inventory():

        prediction = PredictionService.predict_tomorrow()

        db = SessionLocal()

        recipe_repository = RecipeRepository(db)

        ingredient_usage = defaultdict(float)

        try:

            print("=" * 60)
            print("TOTAL PREDICTIONS:", len(prediction["predictions"]))

            for pizza in prediction["predictions"]:

                recipes = recipe_repository.get_recipe(
                    pizza["pizza_type_id"]
                )

                if len(recipes) == 0:
                    print("NO RECIPE FOUND ->", pizza["pizza_type_id"])

                else:
                    print(
                        pizza["pizza_type_id"],
                        "recipes:",
                        len(recipes)
                    )

                for recipe in recipes:

                    ingredient_usage[
                        recipe.ingredient
                    ] += (
                        float(recipe.quantity)
                        * pizza["predicted_quantity"]
                    )

            print("=" * 60)
            print("TOTAL INGREDIENTS:", len(ingredient_usage))
            print("=" * 60)

            return {
                "forecast_date": prediction["date"],
                "predicted_pizzas": prediction["total_predicted_quantity"],
                "ingredients": [
                    {
                        "ingredient": ingredient,
                        "required_quantity": round(quantity, 2)
                    }
                    for ingredient, quantity in ingredient_usage.items()
                ]
            }

        finally:
            db.close()