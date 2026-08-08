from sqlalchemy.orm import Session

from app.models.recipe import Recipe


class InventoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_recipe(self, pizza_type_id: str):

        return (
            self.db.query(Recipe)
            .filter(
                Recipe.pizza_type_id == pizza_type_id
            )
            .all()
        )

    def get_all_recipes(self):

        return self.db.query(Recipe).all()