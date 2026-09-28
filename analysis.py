import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Calculate Total Sales = (Quantity * Price)
df['Total_Sales'] = df['Quantity'] * df['Price']

print("--- Sales Data with Total Sales ---")
print(df)

# Total Sales by Category
category_sales = df.groupby('Category')['Total_Sales'].sum()
print("\n--- Total Sales by Category ---")
print(category_sales)

# Total Sales by Region
region_sales = df.groupby('Region')['Total_Sales'].sum()
print("\n--- Total Sales by Region ---")
print(region_sales)

# Most sold Product (by quantity)
most_sold = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("\n--- Most Sold Product (Quantity) ---")
print(most_sold)

# Bar chart for Category Sales
plt.figure(figsize=(8, 5))
category_sales.plot(kind='bar', color=['blue', 'orange', 'green', 'red'])
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales (Rs)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('category_sales.png') # This will save the chart
plt.show()

print("\nChart saved as category_sales.png")

# Bar chart for region sales
plt.figure(figsize=(8, 5))
region_sales.plot(kind='bar', color=["#84E94E", "#064B6C", "#5EB006", "#FAE710"])
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales (Rs)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('region_sales.png') # Saves second chart
plt.show()

# Line chart for monthly sales trend
df['Date'] = pd.to_datetime(df['Date'])
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Total_Sales'].sum()
plt.figure(figsize=(8, 5))
monthly_sales.plot(kind='line', marker='o', color='blue')
plt.title('Monthly Sales Trend', fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Sales (Rs)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png') # Saves third chart
plt.show()