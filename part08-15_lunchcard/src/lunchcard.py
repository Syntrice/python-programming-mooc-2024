# Write your solution here:

class LunchCard:
    
    def __init__(self, balance: float) -> None:
        self.balance = balance
        
    def __str__(self) -> str:
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60
    
    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60
    
    def deposit_money(self, amount: float):
        
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
            return
        
        self.balance += amount
    
peter = LunchCard(20)
grace = LunchCard(30)
peter.eat_special()
grace.eat_lunch()
print("Peter: " + str(peter))
print("Grace: " + str(grace))
peter.deposit_money(20)
grace.eat_special()
print("Peter: " + str(peter))
print("Grace: " + str(grace))
peter.eat_lunch()
peter.eat_lunch()
grace.deposit_money(50)
print("Peter: " + str(peter))
print("Grace: " + str(grace))