# Write your solution here

from random import sample

def words(n: int, beginning: str):
    words = []
    
    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            if line.startswith(beginning): words.append(line)
            
    if len(words) < n: raise ValueError(f"Not enough words beginning with {beginning} for sample of size {n}.")
    
    return sample(words, k=n)
    
    
if __name__ == "__main__":
    words(7,"careen")