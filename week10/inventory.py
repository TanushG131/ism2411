
# ISM2411 - Module 10 Lab: Inventory List Manager
# Name: Tanush Gangadhara
#
# Reflection 1:
# One surprising thing about Python lists is that they can be changed
# after they are created, and negative indexing helps you get items at the end easier
#
# Reflection 2:
# During a marketing internship, a Python list could have helped me
# organize social media posts and compare engagement results more quickly
# than entering and sorting each item manually in Excel.


# Exercise 1: Build the list
print("EXERCISE 1: BUILD THE LIST")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print("Total items:", len(inventory))


# Exercise 2: Index practice
print("\nEXERCISE 2: INDEX PRACTICE")

print("First item:", inventory[0])
print("Last item:", inventory[-1])

middle_index = len(inventory) // 2
print("Middle item:", inventory[middle_index])


# Exercise 3: Slicing
print("\nEXERCISE 3: SLICING")

print("First three items:", inventory[:3])
print("Last two items:", inventory[-2:])
print("Every other item:", inventory[::2])


# Exercise 4: Modify the inventory
print("\nEXERCISE 4: MODIFY THE INVENTORY")

inventory.append("envelope")
print("After appending envelope:", inventory)

inventory.remove("tape")
print("After removing tape:", inventory)

inventory.sort()
print("After sorting:", inventory)


# Exercise 5: Tuple comparison
print("\nEXERCISE 5: TUPLE COMPARISON")

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print(
        "Tuples are useful for coordinates because "
        "their values cannot be changed after creation."
    )

print("Original coordinates:", coords)


# Exercise 6: Average of sales
print("\nEXERCISE 6: AVERAGE OF SALES")

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best_day = max(sales)
worst_day = min(sales)

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", best_day)
print("Worst:", worst_day)


# Exercise 7: Accumulator pattern
print("\nEXERCISE 7: DISCOUNTED PRICES")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original prices:", prices)
print("Discounted prices:", discounted)


# Exercise 8: Filter above threshold
print("\nEXERCISE 8: HIGH SALES")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))
