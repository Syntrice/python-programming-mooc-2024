# Write your solution here

# Recipies[Recipie{name:str, time:int, ingrediants:list[str]}]
# 

def load_recipes(path: str) -> list[dict]:
    
    recipies = []
    i = 0
    recipies.append([])
    
    with open(path) as file:
        for line in file:
            if line == '\n':
                recipies.append([])
                i += 1
                continue
            recipies[i].append(line.strip())
                
        return recipies
    
def search_by_name(filename: str, word: str):
    recipies = load_recipes(filename)
    found = []
    for r in recipies:
        if word in r[0].lower():
            found.append(r[0])
    return found

def search_by_time(filename: str, prep_time: int):
    recipies = load_recipes(filename)
    found = []
    for r in recipies:
        if prep_time >= int(r[1]):
            found.append(f"{r[0]}, preparation time {r[1]} min")
    return found

def search_by_ingredient(filename: str, ingredient: str):
    recipies = load_recipes(filename)
    found = []
    for r in recipies:
        for i in r[1::]:
            if i == ingredient:
                found.append(f"{r[0]}, preparation time {r[1]} min")
    return found