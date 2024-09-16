# Write your solution here
 
def invert(dictionary: dict):
    inverted = {}
    for key, value in dictionary.items():
        inverted[value] = key
    dictionary.clear()
    dictionary.update(inverted)