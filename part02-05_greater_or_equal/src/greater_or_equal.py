# Write your solution here
number_1 = int(input("Please type in the first number:"))
number_2 = int(input("Please type in another number:"))
 
if number_1 == number_2:
    print("The numbers are equal!")
elif number_1 > number_2:
    print(f"The greater number was: {number_1}")
else:
    print(f"The greater number was: {number_2}")