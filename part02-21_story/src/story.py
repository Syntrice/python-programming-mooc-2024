# Write your solution here
 
words = []
last_word = None
while True:
    word = input("Please type in a word:")
    
    if word == "end":
        break
    
    if word == last_word:
        break
    
    last_word = word
    words.append(word)
    
print(" ".join(words))