names = ["Apple", "Banana", "Mango", "Orange"]
stocks = [121, 238, 195, 50]
prices = [20.50, 15.75, 25.00, 18.00]

print("\n--- Inventory List---\n")

item_number = 1

for name, stock, price in zip(names, stocks, prices):
    total_value = stock * price

    print(f"Item {item_number}:")
    print(f"  Name         : {name}")
    print(f"  Stock        : {stock:8.2f}")
    print(f"  Price        : {price:8.2f}")
    print(f"  Total Value  : {total_value:8,.2f}")
    print("  -----------------------------\n")

    item_number += 1



