# Write your solution here
 
def length_of_longest(strings):
    length = 0
    for s in strings:
        l = len(s)
        if l > length: length = l
    
    return length