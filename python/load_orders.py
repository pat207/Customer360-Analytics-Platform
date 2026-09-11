from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("Aathma@14")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

orders = pd.read_csv(
    r"data\raw\olist_orders_dataset.csv"
)

date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(
        orders[col],
        errors="coerce"
    )

print(f"Rows found: {len(orders)}")

orders.to_sql(
    "orders",
    engine,
    if_exists="append",
    index=False
)

print("✅ Orders imported successfully!")