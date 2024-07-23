# Write your solution here
 
def longest(strings: list):
    longest = ""
    for s in strings:
        if len(s) > len(longest): longest = s
    return longest