# Write your solution here

from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

result = datetime(1999, 12, 31) - datetime(year, month, day)

if result.days > 0:
    print(f"You were {result.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")