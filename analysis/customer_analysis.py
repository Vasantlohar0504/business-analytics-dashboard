import pandas as pd

df = pd.read_excel("data/superstore_sales.xls")

# Sales by customer segment
segment_sales = df.groupby("Segment")["Sales"].sum()

print("Sales by Customer Segment:")
print(segment_sales)

# Top customers
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop Customers:")
print(top_customers)