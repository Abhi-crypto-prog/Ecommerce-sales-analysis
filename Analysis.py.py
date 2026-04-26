import sqlite3
import pandas as pd

# CSV load --- use encoding = latin1 (cz file is not in UTF-8)
df = pd.read_csv(r"C:\Users\Abhishek Chatterjee\OneDrive\Desktop\Ecommerce_project\data\superstore.csv",encoding='latin1')

# Database create/connect
conn = sqlite3.connect("ecommerce.db")

# Table create + data insert
df.to_sql("orders", conn, if_exists = "replace", index = False)

# SQL query run
query = "SELECT Region,SUM(sales) FROM orders GROUP BY Region"
result = pd.read_sql(query, conn)

print(result)

print(df.head())     # top 5 rows
print(df.columns)    # column names
print(df.shape)      # rows, columns
print(df.info())    # data types

# Missing values check
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Profit percentage
df["Profit_percent"] = (df["Profit"] / df["Sales"]) * 100

# Profit/Loss label
df["status"] = df["Profit"].apply(lambda x: "Profit" if x > 0 else "Loss")

# Region wise sales
print(df.groupby("Region")["Sales"].sum())

# Category wise profit
print(df.groupby("Category")["Profit"].sum())

# Top 5 Products
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending = False).head(5))

# save file
df.to_csv("cleaned_data.csv",index = False)

print("file saved successfully")

print(df["status"].value_counts())
