import pandas as pd

# Load Excel dataset
df = pd.read_excel("data/superstore_sales.xls", engine="xlrd")

# Show first rows
print(df.head())

# Sales by Region
sales_region = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(sales_region)

# Top 10 products by sales
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products:")
print(top_products)