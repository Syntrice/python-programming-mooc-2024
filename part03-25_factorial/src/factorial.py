# Write your solution here
while True:
    number = int(input("Please type in a number:"))
    
    if number <= 0: break
    
    factorial = 1
    for n in range(number,1,-1): factorial *= n
    print(f"The factorial of the number {number} is {factorial}")
    
    
print("Thanks and bye!")