# Write your solution here

import string

def separate_characters(my_string: str) -> tuple[str,str,str]:
    
    ascii_letters = ""
    punctuation = ""
    other = ""
    
    for char in my_string:
        if char in string.ascii_letters: ascii_letters += char
        elif char in string.punctuation: punctuation += char
        else: other += char
        
    return (ascii_letters, punctuation, other)

if __name__ == "__main__":
    print(separate_characters("Olé!!! Hey, are ümläüts wörking?"))