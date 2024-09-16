# WRITE YOUR SOLUTION HERE:
from typing import Self
import math

class SimpleDate:
    
    def __init__(self, day: int, month: int, year: int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year
        
    def __lt__(self, other: Self) -> bool:
        return self.__as_year_float() < other.__as_year_float()
        
    def __gt__(self, other: Self) -> bool:
        return self.__as_year_float() > other.__as_year_float()
        
    def __eq__(self, other: Self) -> bool:
        return self.__as_year_float() == other.__as_year_float()
        
    def __ne__(self, other: Self) -> bool:
        return self.__as_year_float() != other.__as_year_float()
        
    def __as_year_float(self) -> float:
        return self.__year + self.__month / 12 + self.__day / 360

    def __add__(self, days: int) -> Self:
        day = (self.__day + days) % 30
        month = (self.__month + (self.__day + days) // 30) % 12
        year = self.__year + (self.__month + (self.__day + days) // 30) // 12
        return SimpleDate(day, month, year)
    
    def __sub__(self, other: Self) -> int:
        self_days = self.__day + self.__month * 30 + self.__year * 360
        other_days = other.__day + other.__month * 30 + other.__year * 360
        
        return abs(self_days - other_days)
            
        
    def __str__(self) -> str:
            return f"{self.__day}.{self.__month}.{self.__year}"
        
        
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)