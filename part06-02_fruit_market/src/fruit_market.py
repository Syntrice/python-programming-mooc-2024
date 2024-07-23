# write your solution here

def read_fruits():
    fruits = {}
    
    with open("fruits.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            fruits[parts[0]] = float(parts[1])
            
    return fruits