from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class AggregatedSales(Base):
    __tablename__ = "aggregated_sales"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    order_date: Mapped[date] = mapped_column(Date)

    hour: Mapped[int] = mapped_column(Integer)

    day_of_week: Mapped[str] = mapped_column(String(20))

    month: Mapped[int] = mapped_column(Integer)

    weekend: Mapped[bool]

    pizza_name: Mapped[str] = mapped_column(String(100))

    category: Mapped[str] = mapped_column(String(50))

    size: Mapped[str] = mapped_column(String(5))

    quantity_sold: Mapped[int]

    revenue: Mapped[Decimal] = mapped_column(Numeric(10, 2))