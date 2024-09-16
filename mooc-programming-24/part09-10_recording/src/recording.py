# WRITE YOUR SOLUTION HERE:

class Recording:
    def __init__(self, length: int) -> None:
        self.length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        
        if value < 0:
            raise ValueError("Length value must be greater than 0")
        
        self.__length = value
