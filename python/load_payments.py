from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("Aathma@14")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

payments = pd.read_csv(
    r"data\raw\olist_order_payments_dataset.csv"
)

print(f"Rows found: {len(payments)}")

payments.to_sql(
    "payments",
    engine,
    if_exists="append",
    index=False
)

print("✅ Payments imported successfully!")