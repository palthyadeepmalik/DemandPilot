from sqlalchemy import func
import pandas as pd

from app.database.session import SessionLocal
from app.models.order import Order
from app.models.order_detail import OrderDetail
from app.models.pizza import Pizza
from app.models.pizza_type import PizzaType


def load_training_dataset():

    db = SessionLocal()

    try:

        query = (
            db.query(
                Order.order_date.label("date"),
                Pizza.pizza_id,
                PizzaType.category,
                Pizza.size,
                func.sum(OrderDetail.quantity).label("quantity")
            )

            .join(OrderDetail, Order.order_id == OrderDetail.order_id)
            .join(Pizza, OrderDetail.pizza_id == Pizza.pizza_id)
            .join(PizzaType, Pizza.pizza_type_id == PizzaType.pizza_type_id)

            .group_by(
                Order.order_date,
                Pizza.pizza_id,
                PizzaType.category,
                Pizza.size
            )

            .order_by(Order.order_date)

        )

        rows = query.all()

        df = pd.DataFrame(
            rows,
            columns=[
                "date",
                "pizza_id",
                "category",
                "size",
                "quantity"
            ]
        )

        return df

    finally:
        db.close()