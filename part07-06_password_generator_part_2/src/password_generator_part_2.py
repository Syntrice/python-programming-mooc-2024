# Write your solution here
from random import choices
from string import ascii_lowercase, digits

def generate_strong_password(length: int, use_digits: bool = False, use_symbols: bool = False) -> str:
    
    collection = []
    symbols = ["!","?","=","+","-","(",")","#"]
    collection += ascii_lowercase
    if use_digits: collection += digits
    if use_symbols: collection += symbols
    
    # Validate password
    while True:
        password = "".join(choices(collection, k=length))
    
        if (use_digits or use_symbols) and not any(element in password for element in ascii_lowercase): continue
        
        if use_digits and not any(element in password for element in digits): continue
        
        if use_symbols and not any(element in password for element in ["!","?","=","+","-","(",")","#"]): continue
        
        return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))