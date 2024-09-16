# Write your solution here
 
list1 = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index:"))
    
    if index == -1: break
    
    new_val = int(input("New value:"))
    list1[index] = new_val
    
    print(list1)
    