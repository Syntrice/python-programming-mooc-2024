# Write your solution here
 
def sum_of_positives(numbers):
    sum = 0
    for number in numbers:
        if number > 0:
            sum += number
    return sum