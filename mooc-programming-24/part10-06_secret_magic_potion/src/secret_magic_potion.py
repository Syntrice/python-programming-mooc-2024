# Write your solution here:
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")
            
class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self.__password = password

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self.__password:
            return super().add_ingredient(ingredient, amount)
        else:
            raise ValueError("Password is incorrect!")
    
    def print_recipe(self, password: str):
        if password == self.__password:
            return super().print_recipe()
        else:
            raise ValueError("Password is incorrect!")
