# Write your solution here
string = input("Please type in a string:")
if string[-2] == string[1]:
    print(f"The second and the second to last characters are {string[1]}")
else:
    print("The second and the second to last characters are different")