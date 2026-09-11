from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("Aathma@14")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/customer360"
)

query = """
SELECT
    c.customer_unique_id,
    MAX(o.order_purchase_timestamp) AS last_purchase,
    COUNT(DISTINCT o.order_id) AS frequency,
    SUM(p.payment_value) AS monetary
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN payments p
    ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
"""

rfm = pd.read_sql(text(query), engine)

rfm["last_purchase"] = pd.to_datetime(rfm["last_purchase"])

snapshot_date = rfm["last_purchase"].max() + pd.Timedelta(days=1)

rfm["recency"] = (
    snapshot_date - rfm["last_purchase"]
).dt.days

rfm = rfm[
    [
        "customer_unique_id",
        "recency",
        "frequency",
        "monetary"
    ]
]

# RFM Scores
rfm["R"] = pd.qcut(
    rfm["recency"],
    5,
    labels=[5,4,3,2,1]
)

rfm["F"] = pd.qcut(
    rfm["frequency"].rank(method="first"),
    5,
    labels=[1,2,3,4,5]
)

rfm["M"] = pd.qcut(
    rfm["monetary"],
    5,
    labels=[1,2,3,4,5]
)

rfm["RFM_SCORE"] = (
    rfm["R"].astype(str) +
    rfm["F"].astype(str) +
    rfm["M"].astype(str)
)

print(
    rfm[
        [
            "customer_unique_id",
            "recency",
            "frequency",
            "monetary",
            "RFM_SCORE"
        ]
    ].head()
)

rfm.to_csv(
    r"reports\rfm_scores.csv",
    index=False
)

print("\n✅ RFM Scores exported")