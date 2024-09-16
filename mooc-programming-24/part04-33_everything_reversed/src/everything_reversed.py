# Write your solution here
 
def everything_reversed(strings: list[str]):
    result = []
    for string in strings:
        result.append(string[::-1])
    return result[::-1]