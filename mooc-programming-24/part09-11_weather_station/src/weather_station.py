# WRITE YOUR SOLUTION HERE:

class WeatherStation:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observations = []
        
    def add_observation(self, observation: str) -> None:
        self.__observations.append(observation)
        
    def latest_observation(self) -> str:
        return self.__observations[len(self.__observations) -1] if bool(self.__observations) else ""

    def number_of_observations(self) -> int:
        return len(self.__observations)
    
    def __str__(self) -> str:
        return f"{self.__name}, {self.number_of_observations()} observations"