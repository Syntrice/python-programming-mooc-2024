from math import sqrt
# Write your solution here
 
while True:
    number = int(input("Please type in a number:"))
 
    if number == 0:
        print("Exiting...")
        break
    
    if number < 0:
        print("Invalid number")
        continue
    
    print(sqrt(number))