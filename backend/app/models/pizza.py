from decimal import Decimal

from sqlalchemy import String, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Pizza(Base):
    __tablename__ = "pizzas"

    pizza_id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True,
        index=True
    )

    pizza_type_id: Mapped[str] = mapped_column(
        ForeignKey("pizza_types.pizza_type_id"),
        nullable=False
    )

    size: Mapped[str] = mapped_column(
        String(5),
        nullable=False
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False
    )

    pizza_type = relationship(
        "PizzaType",
        back_populates="pizzas"
    )

    order_details = relationship(
        "OrderDetail",
        back_populates="pizza"
    )