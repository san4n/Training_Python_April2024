# Build dictionary of products and prices
products = {
    'apple': 1.20,
    'banana': 0.80,
    'milk': 2.50,
    'bread': 1.75,
    'eggs': 3.00,
    'cheese': 4.50,
    'chicken': 7.25
}

# Look up a product price
name = input("Enter product name to look up: ").lower()
if name in products:
    print(f"{name} costs ${products[name]:.2f}")
else:
    print("Product not found.")

# Filter by dollar amount
limit = float(input("Enter maximum price: "))
print(f"Products costing ${limit:.2f} or less:")
for product, price in products.items():
    if price <= limit:
        print(f"- {product}: ${price:.2f}")
