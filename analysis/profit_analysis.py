import pandas as pd

df = pd.read_excel("data/superstore_sales.xls")

# Profit by category
profit_category = df.groupby("Category")["Profit"].sum()

print("Profit by Category:")
print(profit_category)

# Profit by sub-category
profit_sub = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)

print("\nProfit by Sub-Category:")
print(profit_sub)