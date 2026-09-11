from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("Aathma@14")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

with engine.connect() as conn:
    result = pd.read_sql(
        text("SELECT COUNT(*) AS customer_count FROM customers"),
        conn
    )

print(result)