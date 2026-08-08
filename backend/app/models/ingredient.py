from sqlalchemy import Column, Integer, String

from app.database.base import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), unique=True, nullable=False)

    unit = Column(String(20), nullable=False)