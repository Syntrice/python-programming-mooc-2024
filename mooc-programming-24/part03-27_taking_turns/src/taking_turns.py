# Write your solution here
 
number = int(input("Please type in a number:"))
 
up = True
for i in range(1,number - (number)//2 + 1):
    print(i)
    b = number+1 - i
    if b == i: break
    print(b)