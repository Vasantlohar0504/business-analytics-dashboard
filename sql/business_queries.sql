-- Total sales
SELECT SUM(Sales) AS Total_Sales
FROM superstore;

-- Sales by region
SELECT Region, SUM(Sales) AS Revenue
FROM superstore
GROUP BY Region;

-- Profit by category
SELECT Category, SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category;

-- Top 10 customers
SELECT "Customer Name", SUM(Sales) AS Revenue
FROM superstore
GROUP BY "Customer Name"
ORDER BY Revenue DESC
LIMIT 10;