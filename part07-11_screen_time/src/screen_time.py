# Write your solution here
from datetime import datetime, timedelta


    
filename = input("Filename: ")
starting_date = input("Starting date: ").split(".")
starting_date = datetime(year=int(starting_date[2]), month=int(starting_date[1]), day=int(starting_date[0]))
days = int(input("How many days: "))

print("Please type in screen time in minutes on each day (TV computer mobile):")

data = []
total_minutes = 0

for d in range(days):
    current_date = (starting_date + timedelta(days=d)).strftime("%d.%m.%Y")
    screen_time = input(f"Screen time {current_date}: ")
    screen_time = screen_time.split(" ")
    for i in screen_time:
        total_minutes += int(i)
    
    data.append(f"{current_date}: {screen_time[0]}/{screen_time[1]}/{screen_time[2]}")

average_minutes = total_minutes / days

with open(filename, "w") as file:
    
    file.write(f"Time period: {starting_date:%d.%m.%Y}-{(starting_date + timedelta(days=days-1)):%d.%m.%Y}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {average_minutes}\n")
    
    for entry in data:
        file.write(entry + "\n")
    
print("Data stored in file late_june.txt")

# for an expandable program, might be a good idea to implement reading of existing files / appending, and also store the data as a tuple rather than as an already formatted string. For this use case, works fine howerver.