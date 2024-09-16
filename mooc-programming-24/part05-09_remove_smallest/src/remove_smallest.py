# Write your solution here
 
def remove_smallest(numbers: list):
    smallest = min(numbers)
    numbers.remove(smallest)
# remove_smallest(numbers=[1,3,4,5,4,3,5,6,3,8,8,6,6,4,3,4,6,7,8]) => 0.00000 seconds
    