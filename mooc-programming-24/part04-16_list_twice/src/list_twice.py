# Write your solution here
 
li = []
while True:
    i = int(input("New item:"))
    if i == 0: break
    li.append(i)
    
    print(f"The list now: {li}")
    print(f"The list in order: {sorted(li)}")
    
print("Bye!")