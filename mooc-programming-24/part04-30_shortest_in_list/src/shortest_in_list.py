# Write your solution here
 
def shortest(strings: list[str]):
    shortest = strings[0]
    for string in strings:
        if len(string) < len(shortest):
            shortest = string
    return shortest