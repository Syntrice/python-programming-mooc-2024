# Write your solution here
 
string = input("Please type in a string:")
i = len(string) - 1
while i > -1:
    print(string[i:len(string)])
    i -= 1