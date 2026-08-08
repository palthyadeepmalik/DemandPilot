from sqlalchemy.orm import Session

from app.models.pizza import Pizza


class PizzaRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, pizza_id: str):
        return (
            self.db.query(Pizza)
            .filter(Pizza.pizza_id == pizza_id)
            .first()
        )

    def exists(self, pizza_id: str) -> bool:
        return self.get_by_id(pizza_id) is not None