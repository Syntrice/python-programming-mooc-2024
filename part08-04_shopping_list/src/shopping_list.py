# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------

def total_units(my_list: ShoppingList):
    total_units = 0
<<<<<<< Updated upstream
    for item in my_list.products:
        total_units += item[1]
        
=======
    for product in my_list.products:
        total_units += product[1]
>>>>>>> Stashed changes
    return total_units