from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from app.database.base import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)

    pizza_type_id = Column(
        String,
        ForeignKey("pizza_types.pizza_type_id"),
        nullable=False,
    )

    ingredient = Column(String(100), nullable=False)

    quantity = Column(Float, nullable=False)

    unit = Column(String(20), nullable=False)

    pizza_type = relationship("PizzaType")