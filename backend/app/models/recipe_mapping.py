from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class RecipeMapping(Base):
    __tablename__ = "recipe_mapping"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    pizza_type_id: Mapped[str] = mapped_column(
        ForeignKey("pizza_types.pizza_type_id")
    )

    ingredient: Mapped[str] = mapped_column(String(50))

    quantity: Mapped[Decimal] = mapped_column(
        Numeric(8, 2)
    )

    unit: Mapped[str] = mapped_column(String(20))