# Write your solution here
from math import inf

def smallest_average(person: dict, person2: dict, person3: dict):
    largest_average = (None, inf)
    
    for p in [person, person2, person3]:
        average = (p["result1"] + p["result2"] + p["result3"]) / 3
        if average < largest_average[1]:
            largest_average = (p, average)
    
    return largest_average[0]
        
        
if __name__ == "__main__":
    
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))