# Write your solution here
gift_value = int(input("Value of gift:"))
tax = 0
 
if 5000 <= gift_value <= 25_000:
    tax = 100 + (gift_value - 5000) * 0.08
if 25_000 <= gift_value <= 55_000:
    tax = 1700 + (gift_value - 25_000) * 0.10
if 55_000 <= gift_value <= 200_000:
    tax = 4700 + (gift_value - 55_000) * 0.12
if 200_000 <= gift_value <= 1_000_000:
    tax = 22_100 + (gift_value - 200_000) * 0.15
if 1_000_000 < gift_value:
    tax = 142_100 + (gift_value - 1_000_000) * 0.17
 
if tax == 0:
    print("No tax!")
else:    
    print(f"Amount of tax: {tax} euros")