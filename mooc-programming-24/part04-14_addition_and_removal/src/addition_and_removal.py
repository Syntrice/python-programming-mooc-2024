# Write your solution here
 
li = []
 
while True:
    print(f"The list is now {li}")
    
    choice = input("a(d)d, (r)emove or e(x)it: ")
    
    if choice == "x": break
    
    if choice == "d": li.append(len(li)+1)
    
    if choice == "r": li.pop()
    
print("Bye!")