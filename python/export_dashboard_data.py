from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("Aathma@14")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

# Revenue Trend
revenue_query = """
SELECT
    DATE_FORMAT(o.order_purchase_timestamp,'%Y-%m') AS month,
    ROUND(SUM(p.payment_value),2) AS revenue
FROM orders o
JOIN payments p
ON o.order_id = p.order_id
GROUP BY month
ORDER BY month
"""

# Orders Trend
orders_query = """
SELECT
    DATE_FORMAT(order_purchase_timestamp,'%Y-%m') AS month,
    COUNT(*) AS orders
FROM orders
GROUP BY month
ORDER BY month
"""

revenue = pd.read_sql(text(revenue_query), engine)
orders = pd.read_sql(text(orders_query), engine)

revenue.to_csv(
    "reports/revenue_trend.csv",
    index=False
)

orders.to_csv(
    "reports/orders_trend.csv",
    index=False
)

print("Dashboard datasets exported successfully")