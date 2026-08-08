from app.services.inventory_service import InventoryService


class DecisionSupportService:

    @staticmethod
    def generate_decisions():

        inventory = InventoryService.calculate_inventory()

        recommendations = []

        for item in inventory["ingredients"]:

            qty = item["required_quantity"]
            ingredient = item["ingredient"]

            if qty >= 20:
                recommendations.append(
                    {
                        "priority": "HIGH",
                        "ingredient": ingredient,
                        "message": f"Reorder {ingredient}. Expected usage is {qty:.2f} units."
                    }
                )

            elif qty >= 10:
                recommendations.append(
                    {
                        "priority": "MEDIUM",
                        "ingredient": ingredient,
                        "message": f"Monitor {ingredient}. Stock may become low."
                    }
                )

            else:
                recommendations.append(
                    {
                        "priority": "LOW",
                        "ingredient": ingredient,
                        "message": f"{ingredient} inventory is sufficient."
                    }
                )

        return {
            "forecast_date": inventory["forecast_date"],
            "predicted_pizzas": inventory["predicted_pizzas"],
            "recommendations": recommendations
        }