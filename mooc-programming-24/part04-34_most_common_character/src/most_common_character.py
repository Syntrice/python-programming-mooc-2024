# Write your solution here
 
def most_common_character(string: str):
    chars = set(string)
    result = 0
    for c in chars:
        value = string.count(c)
        if value > result:
            result = value
            char = c
    return char
    
if __name__ == "__main__":
    most_common_character("hello world")