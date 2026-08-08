from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    ingredient: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True
    )

    quantity_available: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    unit: Mapped[str] = mapped_column(String(20))