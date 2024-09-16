# Write your solution here

num = int(input("Please type in a positive integer:"))

for i in range(num * -1, num + 1):
    if (i == 0):
        continue
    print(i)