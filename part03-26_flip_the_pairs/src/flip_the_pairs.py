# Write your solution here
 
number = int(input("Please type in a number:"))
 
n = 2
while n <= number:
    print(n)
    n += -1 if n % 2 == 0 else 3
    
if number % 2 != 0: print(number)