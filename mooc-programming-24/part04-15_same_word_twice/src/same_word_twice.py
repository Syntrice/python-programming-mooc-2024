# Write your solution here
#Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
words = []
while True:
    word = input("Word:")
    if word in words:
        print("You typed in", len(words), "different words")
        break
    else:
        words.append(word)