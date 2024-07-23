# Write your solution here
 
limit = int(input("Limit:"))
sum = 0
x = 0
calculation = "The consecutive sum: "
 
while sum < limit:
    x += 1
    sum += x
    if sum < limit:
        calculation += f"{x} + "
    else:
        calculation += f"{x} = {sum}"
print(calculation)