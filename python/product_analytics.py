import pandas as pd

# Load datasets
products = pd.read_csv("data/raw/olist_products_dataset.csv")
order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")

# Merge
merged = order_items.merge(
    products[["product_id", "product_category_name"]],
    on="product_id",
    how="left"
)

# Replace missing categories
merged["product_category_name"] = merged["product_category_name"].fillna("Unknown")

# Revenue by Category
category_revenue = (
    merged.groupby("product_category_name")["price"]
    .sum()
    .reset_index()
    .sort_values(by="price", ascending=False)
)

category_revenue.columns = ["Category", "Revenue"]

# Top 10 Categories
top_categories = category_revenue.head(10)

# Top 10 Products
top_products = (
    merged.groupby("product_id")["price"]
    .sum()
    .reset_index()
    .sort_values(by="price", ascending=False)
    .head(10)
)

top_products.columns = ["Product_ID", "Revenue"]

# Export
category_revenue.to_csv(
    "reports/category_revenue.csv",
    index=False
)

top_categories.to_csv(
    "reports/top_categories.csv",
    index=False
)

top_products.to_csv(
    "reports/top_products.csv",
    index=False
)

print("✅ Product analytics datasets exported successfully")