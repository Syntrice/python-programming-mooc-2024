# Write your solution here
 
def factorials(n: int):
    result = {}
    multiples = 1
    for i in range(1,n+1):
        multiples *= i
        result[i] = multiples
    return result