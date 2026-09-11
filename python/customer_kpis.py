from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("Aathma@14")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

queries = {
    "Total Customers":
    "SELECT COUNT(DISTINCT customer_unique_id) AS value FROM customers",

    "Total Orders":
        "SELECT COUNT(DISTINCT order_id) AS value FROM orders",

    "Total Revenue":
        """
        SELECT ROUND(
            SUM(payment_value),
            2
        ) AS value
        FROM payments
        """,

    "Average Order Value":
        """
        SELECT ROUND(
            SUM(payment_value) /
            COUNT(DISTINCT order_id),
            2
        ) AS value
        FROM payments
        """
}

with engine.connect() as conn:
    for kpi, query in queries.items():
        result = pd.read_sql(text(query), conn)

        print("\n" + "=" * 40)
        print(kpi)
        print("=" * 40)

        print(result.iloc[0, 0])