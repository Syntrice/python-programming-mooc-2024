# Write your solution here
 
def all_the_longest(strings: list[str]):
    longest = [""]
    for string in strings:
        if len(string) > len(longest[0]):
            longest = [string]
        elif len(string) == len(longest[0]):
            longest.append(string)
    return longest