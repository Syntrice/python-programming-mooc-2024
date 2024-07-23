# Write your solution here

from fractions import Fraction

def fractionate(amount: int):
    return [Fraction(1,amount) for x in range(amount)]


""" from fractions import Fraction
 
def fractionate(amount: int):
    # numerator, denominator
    fraction = Fraction(1, amount)
 
    return [fraction] * amount """