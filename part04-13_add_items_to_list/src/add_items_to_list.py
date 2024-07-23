# Write your solution here
 
number = int(input("How many items:"))
items = []
 
for i in range(number):
    items.append(int(input(f"Item {i+1}:")))
    
print(items)