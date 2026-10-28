
# ISM2411 - Module 07 Lab
# Functions + Debug First, Then Ask
#
# SELF-ASSESSMENT
#
# 1. Exercise 5
# The first bug I noticed was `total = sale`, because it overwrites
# the running total instead of adding each sale. The missing colon
# causes a SyntaxError, and the while-loop boundary causes an
# IndexError after the last valid item. 
#
# 2. apply_discount(price, tier) takes a price and a customer tier.
# It returns the price after applying a 15% discount for gold,
# 10% for silver, 5% for bronze, or no discount for other tiers.
# A colleague can pass those two inputs and use the returned price.
#
# 3. AI disclosure: I used ChatGPT to help interpret the lab
# instructions and explain the errors in the debugging exercise.
# I reviewed the code and ran the script to check its output.


# --- Exercise 1: calculate_tax ---

def calculate_tax(price, rate):
    return price * rate


print("Tax on $100 at 7%: ${:.2f}".format(
    calculate_tax(100, 0.07)
))
print("Tax on $250 at 8%: ${:.2f}".format(
    calculate_tax(250, 0.08)
))


# --- Exercise 2: apply_discount ---

def apply_discount(price, tier):
    if tier == "gold":
        discount_rate = 0.15
    elif tier == "silver":
        discount_rate = 0.10
    elif tier == "bronze":
        discount_rate = 0.05
    else:
        discount_rate = 0.0

    return price * (1 - discount_rate)


for tier in ["gold", "silver", "bronze", "none"]:
    discounted_price = apply_discount(200, tier)
    print(f"{tier}: ${discounted_price:.2f}")


# --- Exercise 3: Compose the functions ---

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


price_after_discount = apply_discount(200, "gold")
print(f"After gold discount: ${price_after_discount:.2f}")

tax_after_discount = calculate_tax(price_after_discount, 0.07)
print(f"After tax: ${price_after_discount + tax_after_discount:.2f}")

print(
    f'final_price(200, "gold", 0.07) = '
    f'${final_price(200, "gold", 0.07):.2f}'
)


# --- Exercise 4: Loop + function ---

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5: Fixed version of broken_sales.py ---

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    
    total += sale

print(f"Total: ${total}")

count = 0

for sale in sales:
    count += 1

print(f"Count: {count}")

i = 0

while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6: Scope experiment ---

x = 100  # Global variable


def double_it():
    x = 999  # Local variable, separate from global x
    return x * 2



print(x)
print(double_it())
print(x)
