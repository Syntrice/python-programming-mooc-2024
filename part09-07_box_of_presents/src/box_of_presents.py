# WRITE YOUR SOLUTION HERE:

class Present:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight
        
    def __str__(self) -> str:
        return f"{self.name} ({self.weight} kg)"

class Box:
    def __init__(self) -> None:
        self.presents = []
    
    def add_present(self, present: Present):
        self.presents.append(present)
        
    def total_weight(self) -> int:
        weight = 0
        for present in self.presents:
            weight += present.weight
            
        return weight