# Write your solution here:

# Write your solution here:
class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def tick(self):
        self.hour = (self.hour + (1 if self.minute == 59 and self.second == 59 else 0)) % 24
        self.minute = (self.minute + (1 if self.second == 59 else 0)) % 60
        self.second = (self.second + 1) % 60
        
    def set(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute
        self.second = 0
        
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)