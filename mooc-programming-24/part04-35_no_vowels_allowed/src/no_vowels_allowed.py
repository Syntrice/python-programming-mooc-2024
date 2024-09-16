# Write your solution here

def no_vowels(string):
    new_string = ""
    for char in string:
        if char not in "aeiou":
            new_string += char
    return new_string
        

if __name__ == "__main__":
    print(no_vowels("this is an example"))