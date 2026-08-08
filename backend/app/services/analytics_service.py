from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    def __init__(self, db):
        self.repository = AnalyticsRepository(db)

    # ---------------- Dashboard Summary ---------------- #

    def dashboard_summary(self):

        revenue = self.repository.get_total_revenue()
        total_orders = self.repository.get_total_orders()
        total_pizzas = self.repository.get_total_pizzas_sold()
        top_pizza = self.repository.get_top_pizza()

        return {
            "total_revenue": float(revenue or 0),
            "total_orders": int(total_orders or 0),
            "total_pizzas_sold": int(total_pizzas or 0),
            "top_pizza": top_pizza.pizza_name if top_pizza else None,
            "top_pizza_sales": int(top_pizza.total_sold) if top_pizza else 0
        }

    # ---------------- Revenue ---------------- #

    def total_revenue(self):
        revenue = self.repository.get_total_revenue()

        return {
            "total_revenue": float(revenue)
        }

    # ---------------- Top Pizzas ---------------- #

    def top_pizzas(self, limit=10):

        result = self.repository.get_top_pizzas(limit)

        return [
            {
                "pizza_name": row.pizza_name,
                "total_sold": row.total_sold
            }
            for row in result
        ]

    # ---------------- Hourly Sales ---------------- #

    def hourly_sales(self):

        result = self.repository.get_hourly_sales()

        return [
            {
                "hour": int(row.hour),
                "total_orders": row.total_orders
            }
            for row in result
        ]

    # ---------------- Daily Sales ---------------- #

    def daily_sales(self):

        result = self.repository.get_daily_sales()

        return [
            {
                "date": row.order_date,
                "orders": row.total_orders,
                "revenue": float(row.revenue)
            }
            for row in result
        ]

    # ---------------- Monthly Sales ---------------- #

    def monthly_sales(self):

        result = self.repository.get_monthly_sales()

        return [
            {
                "month": int(row.month),
                "revenue": float(row.revenue)
            }
            for row in result
        ]

    # ---------------- Category Sales ---------------- #

    def category_sales(self):

        result = self.repository.get_category_sales()

        return [
            {
                "category": row.category,
                "total_sold": row.total_sold,
                "revenue": float(row.revenue)
            }
            for row in result
        ]

    # ---------------- Weekend vs Weekday ---------------- #

    def weekend_vs_weekday(self):

        result = self.repository.get_weekend_vs_weekday()

        return [
            {
                "day_type": row.day_type,
                "orders": row.total_orders,
                "revenue": float(row.revenue)
            }
            for row in result
        ]