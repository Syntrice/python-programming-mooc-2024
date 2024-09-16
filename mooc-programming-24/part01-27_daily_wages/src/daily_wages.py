# Write your solution here
wage = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")
 
if day == "Sunday": wage *= 2
 
print(f"Daily wages: {wage * hours} euros")