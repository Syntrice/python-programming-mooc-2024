# Write your solution here
# How many times a week do you eat at the student cafeteria? 4
# The price of a typical student lunch? 2.5
# How much money do you spend on groceries in a week? 28.5
 
cafeteria_days = int(input("How many times a week do you eat at the student cafeteria? "))
cafeteria_price = float(input("The price of a typical student lunch? "))
groceries_weekly_price = float(input("How much money do you spend on groceries in a week? "))
currency = "euros"
 
print("Average food expenditure:")
print(f"Daily: {(cafeteria_days * cafeteria_price + groceries_weekly_price) / 7} {currency}")
print(f"Weekly: {cafeteria_days * cafeteria_price + groceries_weekly_price} {currency}")
 