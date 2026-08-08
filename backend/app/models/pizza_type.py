from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class PizzaType(Base):
    __tablename__ = "pizza_types"

    pizza_type_id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    ingredients: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    pizzas = relationship(
        "Pizza",
        back_populates="pizza_type"
    )