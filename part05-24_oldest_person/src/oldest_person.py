# Write your solution here
 
def oldest_person(people: list):
    
    oldest_age = people[0][1]
    oldest_person = people[0][0]
    
    for name, age in people:
        if age < oldest_age:
            oldest_age = age
            oldest_person = name
    
    return oldest_person
 
if __name__ == "__main__":
    people = [('Arthur', 1977), ('Emily', 2014)]
    print(oldest_person(people))