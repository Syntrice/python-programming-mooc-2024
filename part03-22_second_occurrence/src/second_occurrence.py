# Write your solution here
 
string = input("Please type in a string:")
substring = input("Please type in a substring:")
 
# find first substring index
index1 = string.find(substring)
 
# check if second substring exists
index2 = string[index1+len(substring):].find(substring)
 
# exit clause
if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    index2 += index1+len(substring)
    print(f"The second occurrence of the substring is at index {index2}.")