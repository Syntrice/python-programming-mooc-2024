# Write your solution here:

from random import choice

def word_generator(characters: str, length: int, amount: int):
    return ("".join([choice(characters) for i in range(length)]) for i in range(amount))