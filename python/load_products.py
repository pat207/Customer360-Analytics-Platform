from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("Aathma@14")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

products = pd.read_csv(
    r"data\raw\olist_products_dataset.csv"
)

# Rename columns to match MySQL table
products = products.rename(columns={
    "product_name_lenght": "product_name_length",
    "product_description_lenght": "product_description_length"
})

print(f"Rows found: {len(products)}")

products.to_sql(
    "products",
    engine,
    if_exists="append",
    index=False
)

print("✅ Products imported successfully!")