# Write your solution here
 
word = input("Word:")
if len(word) % 2 != 0: word = " " + word
 
print("*" * 30)
print("*" + " " * ((28 - len(word)) // 2) + word + " " * ((28 - len(word)) // 2) + "*")
print("*" * 30)