# Write your solution here
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    return sorted(sample(range(lower, upper), amount))

if __name__ == "__main__":
    lottery_numbers(7,1,40)