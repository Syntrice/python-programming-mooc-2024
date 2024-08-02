# Write your solution here:

from typing import Optional

class Item:
    def __init__(self, name: str, weight: int) -> None:
        self.__name = name
        self.__weight = weight 
        
    def name(self) -> str:
        return self.__name
        
    def weight(self) -> int:
        return self.__weight
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__contents: list[Item] = []
    
    def add_item(self, item: Item) -> None:
        current_weight = self.weight()
        if current_weight + item.weight() < self.__max_weight:
            self.__contents.append(item)
            
    def print_items(self) -> None:
        for item in self.__contents:
            print(item)
    
    def weight(self) -> int:
        weight = 0
        if bool(self.__contents):
            for item in self.__contents:
                weight += item.weight()
    
        return weight
    
    def heaviest_item(self) -> Optional[Item]:
        it = iter(self.__contents)
        heaviest = next(it, None)
        for item in it:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest
    
        # could also use the max() function with a lambda. Might not even be necessary to do that. (See solutions, they do it differently)
    
    def __str__(self) -> str:
        num_items = len(self.__contents)
        return f"{num_items} item{"" if num_items == 1  else "s"} ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__contents: list[Suitcase] = []
    
    def add_suitcase(self, suitcase: Suitcase) -> None:
        current_weight = self.weight()
        if current_weight + suitcase.weight() < self.__max_weight:
            self.__contents.append(suitcase)
    
    def weight(self) -> int:
        weight = 0
        if bool(self.__contents):
            for suitcase in self.__contents:
                weight += suitcase.weight()
    
        return weight
    
    def print_items(self) -> None:
        for suitcase in self.__contents:
            suitcase.print_items()
    
    def __str__(self) -> str:
        num_items = len(self.__contents)
        return f"{num_items} suitcase{"" if num_items == 1  else "s"}, space for {self.__max_weight - self.weight()} kg"
        

if __name__ == "__main__":
    
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()