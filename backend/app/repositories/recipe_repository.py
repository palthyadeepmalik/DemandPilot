from sqlalchemy.orm import Session

from app.models.recipe_mapping import RecipeMapping


class RecipeRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_recipe(self, pizza_type_id: str):
        return (
            self.db.query(RecipeMapping)
            .filter(
                RecipeMapping.pizza_type_id == pizza_type_id
            )
            .all()
        )