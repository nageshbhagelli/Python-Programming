import pandas as pd

# 8.1 Determine the number of unique orders using the `order_id` column.
chipotle = pd.read_csv('module_8/chipotle.csv') # 8.1
print("Unique orders:", chipotle['order_id'].nunique())

# 8.2 Calculate the average revenue per order.
chipotle['item_price'] = chipotle['item_price'].replace('[\$,]', '', regex=True).astype(float)
avg_revenue = chipotle.groupby('order_id')['item_price'].sum().mean()
print("Average revenue per order:", avg_revenue)

# 8.3 Find out how many different items are sold (unique values in `item_name`).
print("Unique items sold:", chipotle['item_name'].nunique())

# 8.3.a List the top 5 items by total quantity sold.
top5 = chipotle.groupby('item_name')['quantity'].sum().sort_values(ascending=False).head(5)
print("Top 5 items by quantity:\n", top5)

# 8.4 Count the number of unique values in the `choice_description` column.
print("Unique choice_description:", chipotle['choice_description'].nunique())

# 8.5 Identify the order with the highest total bill amount.
order_totals = chipotle.groupby('order_id')['item_price'].sum()
max_order = order_totals.idxmax()
print("Order with highest bill:", max_order, "Amount:", order_totals.max())

# 8.6 Find all items that have inconsistent pricing (same `item_name` but different `item_price`values).
inconsistent = chipotle.groupby('item_name')['item_price'].nunique()
print("Items with inconsistent pricing:", inconsistent[inconsistent > 1])

# 8.7 List orders where any single item was ordered in a quantity greater than 5.
orders_gt5 = chipotle[chipotle['quantity'] > 5]['order_id'].unique()
print("Orders with quantity > 5:", orders_gt5)

# 8.8 Calculate the average price of an item.
avg_item_price = chipotle.groupby('item_name')['item_price'].mean().mean()
print("Average price of an item:", avg_item_price)

# 8.9 List all unique item prices and show the items associated with each price.
unique_prices = chipotle.groupby('item_price')['item_name'].unique()
print("Unique item prices and items:\n", unique_prices)

# 8.10 Display all orders that included *Canned Soda*.
canned_soda_orders = chipotle[chipotle['item_name'].str.contains('Canned Soda', na=False)]
print("Orders with Canned Soda:\n", canned_soda_orders)