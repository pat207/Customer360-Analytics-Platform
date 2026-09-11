from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("Aathma@14")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

order_items = pd.read_csv(
    r"data\raw\olist_order_items_dataset.csv"
)

order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)

print(f"Rows found: {len(order_items)}")

order_items.to_sql(
    "order_items",
    engine,
    if_exists="append",
    index=False
)

print("✅ Order Items imported successfully!")