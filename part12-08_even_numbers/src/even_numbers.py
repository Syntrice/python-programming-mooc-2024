# Write your solution here

def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    elif beginning == 0:
        beginning = 2
        
    while beginning <= maximum:
        yield beginning
        beginning += 2
    
    