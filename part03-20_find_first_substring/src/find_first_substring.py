# Write your solution here
 
word = input("Please type in a word:")
character = input("Please type in a character:")
 
i = word.find(character)
 
word = word[i:]
if len(word) > 2: print(word[:3])