from datetime import datetime, timedelta
import pandas as pd

from app.database.session import SessionLocal
from app.models.pizza import Pizza
from app.models.pizza_type import PizzaType

from app.ml.predict import predict_demand


class PredictionService:

    @staticmethod
    def predict_tomorrow():

        db = SessionLocal()

        try:

            pizzas = (
                db.query(Pizza, PizzaType)
                .join(PizzaType, Pizza.pizza_type_id == PizzaType.pizza_type_id)
                .all()
            )

            tomorrow = datetime.now().date() + timedelta(days=1)

            rows = []

            for pizza, pizza_type in pizzas:

                rows.append(
                    {
                        "date": tomorrow,
                        "pizza_id": pizza.pizza_id,
                        "pizza_type_id": pizza.pizza_type_id,
                        "category": pizza_type.category,
                        "size": pizza.size,
                    }
                )

            df = pd.DataFrame(rows)

            predictions = predict_demand(df)

            total_quantity = int(predictions["predicted_quantity"].sum())

            return {
                "date": str(tomorrow),
                "total_predicted_quantity": total_quantity,
                "predictions": predictions.to_dict(orient="records"),
            }

        finally:
            db.close()