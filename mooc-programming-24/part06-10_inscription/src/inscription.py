# Write your solution here

name = input("Whoem should I sign this to:")
path = input("Where shall I save it:")

with open(path, "w") as file:
    file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")