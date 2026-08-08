from app.models import *

from app.database.base import Base
from app.database.session import engine
from app.models.recipe import Recipe
from app.models.ingredient import Ingredient


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()