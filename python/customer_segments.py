import pandas as pd

rfm = pd.read_csv("reports/rfm_scores.csv")

def segment_customer(row):
    
    r = int(row["R"])
    f = int(row["F"])
    m = int(row["M"])

    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"

    elif r >= 3 and f >= 4:
        return "Loyal Customers"

    elif r >= 4:
        return "Potential Loyalists"

    elif r <= 2 and f >= 3:
        return "At Risk"

    else:
        return "Lost Customers"

rfm["Segment"] = rfm.apply(segment_customer, axis=1)

segment_summary = (
    rfm["Segment"]
    .value_counts()
    .reset_index()
)

segment_summary.columns = [
    "Segment",
    "Customer_Count"
]

print(segment_summary)

segment_summary.to_csv(
    "reports/customer_segments.csv",
    index=False
)

rfm.to_csv(
    "reports/rfm_segmented.csv",
    index=False
)

print("\n✅ Customer segmentation completed")