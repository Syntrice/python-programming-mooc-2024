# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup:
    def __init__(self, name: str, location: str) -> None:
        self._name: str = name
        self._location: str = location
        self._members: list[SuperHero] = []
        
    def name(self) -> str:
        return self._name
    
    def location(self) -> str:
        return self._location
    
    def add_member(self, hero: SuperHero) -> None:
        self._members.append(hero)
        
    def print_group(self) -> None:
        print(f"{self._name}, {self._location}")
        print("Members:")
        for member in self._members:
            print(member)
            
if __name__ == "__main__":
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()