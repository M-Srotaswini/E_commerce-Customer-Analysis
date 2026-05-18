import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_data.csv")

# Create Total Sales column
df['Total Sales'] = df['Quantity'] * df['Price']

# Total Sales
print("Total Sales:")
print(df['Total Sales'].sum())

# Top Selling Products
print("\nTop Selling Products:")
print(df.groupby('Product')['Quantity'].sum())

# City-wise Sales
print("\nCity-wise Sales:")
print(df.groupby('City')['Total Sales'].sum())

# Category-wise Sales
print("\nCategory-wise Sales:")
print(df.groupby('Category')['Total Sales'].sum())

# Top Customers
print("\nTop Customers:")
print(df.groupby('Customer Name')['Total Sales'].sum())

# Visualization
df.groupby('Product')['Quantity'].sum().plot(kind='bar')

plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.title("Top Selling Products")

plt.show()