# TEE RATKAISUSI TÄHÄN:
from typing import Self

class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __eq__(self, other: Self) -> bool:
        return self.__euros == other.__euros and self.__cents == other.__cents
    
    def __lt__(self, other: Self) -> bool:
        money = self.__euros + self.__cents / 100
        other_money = other.__euros + other.__cents / 100
        
        return money < other_money
    
    def __gt__(self, other: Self) -> bool:
        money = self.__euros + self.__cents / 100
        other_money = other.__euros + other.__cents / 100
        
        return money > other_money
    
    def __ne__(self, other: Self) -> bool:
        return not self.__eq__(other)
    
    def __sub__(self, other: Self) -> Self:
        cents = self.__cents - other.__cents
        euros = self.__euros - other.__euros
        
        if cents < 0:
            cents += 100
            euros -= 1
    
        if euros < 0:
            raise ValueError("Negative money value")
        
        return Money(euros, cents)
        
    def __add__(self, other: Self) -> Self:
        cents = self.__cents + other.__cents
        euros = self.__euros + other.__euros
        
        if cents >= 100:
            cents -= 100
            euros += 1
        
        return Money(euros, cents)
    
    
if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)

        #e5 = e2-e1