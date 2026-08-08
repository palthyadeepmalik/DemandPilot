from sqlalchemy import Date, Integer, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    order_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False
    )

    order_time: Mapped[Time] = mapped_column(
        Time,
        nullable=False
    )

    order_details = relationship(
        "OrderDetail",
        back_populates="order"
    )