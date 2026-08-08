from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class OrderDetail(Base):
    __tablename__ = "order_details"

    order_details_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.order_id"),
        nullable=False
    )

    pizza_id: Mapped[str] = mapped_column(
        ForeignKey("pizzas.pizza_id"),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    order = relationship(
        "Order",
        back_populates="order_details"
    )

    pizza = relationship(
        "Pizza",
        back_populates="order_details"
    )