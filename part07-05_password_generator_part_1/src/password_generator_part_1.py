# Write your solution here
from random import choices
from string import ascii_lowercase

def generate_password(length: int, numbers: bool, symbols: bool) -> str:
    
    
    return "".join(choices(ascii_lowercase, k=length))

if __name__ == "__main__":
    print(generate_password(7))