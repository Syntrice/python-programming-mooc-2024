# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:
    def __init__(self, week: int, numbers: list[int]) -> None:
        self.__numbers = numbers
        self.week = week
        
    
    def number_of_hits(self, numbers: list[int]) -> int:
        return len([hit for hit in numbers if hit in self.__numbers])
    
    def hits_in_place(self, numbers: list[int]) -> list[int]:
        return [num if num in self.__numbers else -1 for num in numbers]
    
    def __validate_numbers(self, numbers: list[int]) -> None:
        if len(numbers) != 7:
            raise ValueError('"numbers" must contain exactly 7 items')
        
        
        
if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))
    [1,2,3,10,20,30,33]
    [1,4,7,10,11,20,30]