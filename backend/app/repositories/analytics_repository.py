from sqlalchemy import text
from sqlalchemy.orm import Session


class AnalyticsRepository:

    def __init__(self, db: Session):
        self.db = db

    # ---------------- Dashboard ---------------- #

    def get_total_revenue(self):
        query = text("""
            SELECT ROUND(SUM(od.quantity * p.price), 2) AS revenue
            FROM order_details od
            JOIN pizzas p
                ON od.pizza_id = p.pizza_id;
        """)

        return self.db.execute(query).scalar()

    def get_total_orders(self):
        query = text("""
            SELECT COUNT(*) AS total_orders
            FROM orders;
        """)

        return self.db.execute(query).scalar()

    def get_total_pizzas_sold(self):
        query = text("""
            SELECT SUM(quantity) AS total_pizzas
            FROM order_details;
        """)

        return self.db.execute(query).scalar()

    def get_top_pizza(self):
        query = text("""
            SELECT
                pt.name AS pizza_name,
                SUM(od.quantity) AS total_sold
            FROM order_details od
            JOIN pizzas p
                ON od.pizza_id = p.pizza_id
            JOIN pizza_types pt
                ON p.pizza_type_id = pt.pizza_type_id
            GROUP BY pt.name
            ORDER BY total_sold DESC
            LIMIT 1;
        """)

        return self.db.execute(query).first()

    # ---------------- Top Pizzas ---------------- #

    def get_top_pizzas(self, limit: int):
        query = text("""
            SELECT
                pt.name AS pizza_name,
                SUM(od.quantity) AS total_sold
            FROM order_details od
            JOIN pizzas p
                ON od.pizza_id = p.pizza_id
            JOIN pizza_types pt
                ON p.pizza_type_id = pt.pizza_type_id
            GROUP BY pt.name
            ORDER BY total_sold DESC
            LIMIT :limit;
        """)

        return self.db.execute(query, {"limit": limit})

    # ---------------- Hourly Sales ---------------- #

    def get_hourly_sales(self):
        query = text("""
            SELECT
                EXTRACT(HOUR FROM o.order_time) AS hour,
                SUM(od.quantity) AS total_orders
            FROM orders o
            JOIN order_details od
                ON o.order_id = od.order_id
            GROUP BY hour
            ORDER BY hour;
        """)

        return self.db.execute(query)

    # ---------------- Daily Sales ---------------- #

    def get_daily_sales(self):
        query = text("""
            SELECT
                o.order_date,
                SUM(od.quantity) AS total_orders,
                ROUND(SUM(od.quantity * p.price), 2) AS revenue
            FROM orders o
            JOIN order_details od
                ON o.order_id = od.order_id
            JOIN pizzas p
                ON od.pizza_id = p.pizza_id
            GROUP BY o.order_date
            ORDER BY o.order_date;
        """)

        return self.db.execute(query)

    # ---------------- Monthly Sales ---------------- #

    def get_monthly_sales(self):
        query = text("""
            SELECT
                EXTRACT(MONTH FROM o.order_date) AS month,
                ROUND(SUM(od.quantity * p.price), 2) AS revenue
            FROM orders o
            JOIN order_details od
                ON o.order_id = od.order_id
            JOIN pizzas p
                ON od.pizza_id = p.pizza_id
            GROUP BY month
            ORDER BY month;
        """)

        return self.db.execute(query)

    # ---------------- Category Sales ---------------- #

    def get_category_sales(self):
        query = text("""
            SELECT
                pt.category,
                SUM(od.quantity) AS total_sold,
                ROUND(SUM(od.quantity * p.price), 2) AS revenue
            FROM order_details od
            JOIN pizzas p
                ON od.pizza_id = p.pizza_id
            JOIN pizza_types pt
                ON p.pizza_type_id = pt.pizza_type_id
            GROUP BY pt.category
            ORDER BY revenue DESC;
        """)

        return self.db.execute(query)

    # ---------------- Weekend vs Weekday ---------------- #

    def get_weekend_vs_weekday(self):
        query = text("""
            SELECT
                CASE
                    WHEN EXTRACT(DOW FROM o.order_date) IN (0, 6)
                        THEN 'Weekend'
                    ELSE 'Weekday'
                END AS day_type,
                SUM(od.quantity) AS total_orders,
                ROUND(SUM(od.quantity * p.price), 2) AS revenue
            FROM orders o
            JOIN order_details od
                ON o.order_id = od.order_id
            JOIN pizzas p
                ON od.pizza_id = p.pizza_id
            GROUP BY day_type;
        """)

        return self.db.execute(query)