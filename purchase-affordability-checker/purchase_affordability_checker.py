# --- Purchase Affordability Checker ---

# Step 1: Taking input and stored it in a variable
budget = float(input("How much money I have: "))
product_price = float(input("The amount of product: "))

# Step 2: Checking affordability and calculate
affordable = budget >= product_price
remaining_balance = budget - product_price
non_affordable = product_price - budget

# Step 3: Display results.
print(f"Is affordable or not (True/False): {affordable}")
print(f"Your balance is left: {remaining_balance:.2f}")
print(f"Amount Short: {non_affordable:.2f}")
