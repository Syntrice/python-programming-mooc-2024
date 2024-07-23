# Write your solution here
start_year = int(input("Year:"))
year = start_year
while True:
    year += 1
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
        
print(f"The next leap year after {start_year} is {year}")