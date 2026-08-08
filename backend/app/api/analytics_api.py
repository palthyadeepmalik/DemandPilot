from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# ---------------- Dashboard ---------------- #

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    return AnalyticsService(db).dashboard_summary()


# ---------------- Revenue ---------------- #

@router.get("/revenue")
def revenue(db: Session = Depends(get_db)):
    return AnalyticsService(db).total_revenue()


# ---------------- Top Pizzas ---------------- #

@router.get("/top-pizzas")
def top_pizzas(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return AnalyticsService(db).top_pizzas(limit)


# ---------------- Hourly Sales ---------------- #

@router.get("/hourly-sales")
def hourly_sales(db: Session = Depends(get_db)):
    return AnalyticsService(db).hourly_sales()


# ---------------- Daily Sales ---------------- #

@router.get("/daily-sales")
def daily_sales(db: Session = Depends(get_db)):
    return AnalyticsService(db).daily_sales()


# ---------------- Monthly Sales ---------------- #

@router.get("/monthly-sales")
def monthly_sales(db: Session = Depends(get_db)):
    return AnalyticsService(db).monthly_sales()


# ---------------- Category Sales ---------------- #

@router.get("/category-sales")
def category_sales(db: Session = Depends(get_db)):
    return AnalyticsService(db).category_sales()


# ---------------- Weekend vs Weekday ---------------- #

@router.get("/weekend-vs-weekday")
def weekend_vs_weekday(db: Session = Depends(get_db)):
    return AnalyticsService(db).weekend_vs_weekday()