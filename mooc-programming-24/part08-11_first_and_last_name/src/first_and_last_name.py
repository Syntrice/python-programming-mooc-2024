# Write your solution here:

class Person:
    
    def __init__(self, name: str) -> None:
        self.name = name
        
    def return_first_name(self) -> str:
        return self.name.split(" ")[0]
    
    def return_last_name(self) -> str:
        return self.name.split(" ")[-1]










