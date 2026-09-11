from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

# MySQL password
password = quote_plus("Aathma@14")

# Database connection
engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

# Read customer data
customers = pd.read_csv(
    r"data\raw\olist_customers_dataset.csv"
)

print(f"Rows found: {len(customers)}")

# Load into MySQL
customers.to_sql(
    name="customers",
    con=engine,
    if_exists="append",
    index=False
)

print("✅ Customers imported successfully!")