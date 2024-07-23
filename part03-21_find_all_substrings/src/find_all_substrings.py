# Write your solution here
 
word = input("Please type in a word:")
character = input("Please type in a character:")
 
while True:
    if len(word) == 0:
        break
    
    index = word.find(character)
    
    if index != -1:
        value = word[index:index+3]
        if len(value) > 2: print(word[index:index+3])
        word = word[index+1:]
            
    else:
        word = word[1:]