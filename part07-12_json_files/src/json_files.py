# Write your solution here

import json
def print_persons(filename: str):
    with open(filename) as f:
        content = f.read()
    persons = json.loads(content)
    for person in persons:
        name = person['name']
        age = person['age']
        hobbies = ", ".join(person['hobbies'])
        
        
    # the join method is invaluable here - it inserts the string between each item in an iterable
        
        print(f"{name} {age} years ({hobbies})")

if __name__ == "__main__":
    print_persons("file4.json")