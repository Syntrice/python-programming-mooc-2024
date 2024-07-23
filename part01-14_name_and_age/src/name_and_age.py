# Write your solution here
# What is your name? Frances Fictitious
# Which year were you born? 1990
# Hi Frances Fictitious, you will be 31 years old at the end of the year 2021
 
name = input("What is your name? ")
year = int(input("Which year were you born? "))
age = 2021 - year
print(f"Hi {name}, you will be {age} years old at the end of the year 2021".format(name, age))
