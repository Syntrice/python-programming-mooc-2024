# Write your solution here
 
def histogram(string: str):
    chars = {}
    for c in string:
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    
    for key, value in chars.items():
        print(f"{key} {'*' * value}")