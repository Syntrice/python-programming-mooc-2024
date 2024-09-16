# Write your solution here
 
def even_numbers(numbers):
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
    return even