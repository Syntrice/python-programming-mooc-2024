# WRITE YOUR SOLUTION HERE:

class Car:
    def __init__(self) -> None:
        self.__petrol = 0
        self.__odometer = 0
    
    def fill_up(self) -> None:
        self.__petrol = 60
    
    # this method is an example of clamping a value in a range
    def drive(self, km: int) -> None:
        km = max(0, min(km, self.__petrol))
        self.__odometer += km
        self.__petrol -= km
        
    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"
    
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
