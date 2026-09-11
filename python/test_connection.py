from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("Aathma@14")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

with engine.connect() as conn:
    df = pd.read_sql(text("SHOW TABLES"), conn)

print(df)