# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self) -> None:
        self.people = []
    
    def add(self, person: Person):
        self.people.append(person)
    
    def is_empty(self):
        return not bool(self.people)
    
    def print_contents(self):
        person_details = []
        total_height = 0
        for person in self.people:
            person_details.append(f"{person.name} ({person.height} cm)")
            total_height += person.height
        
        print(f"There are {len(self.people)} persons in the room, and their combined height is {total_height} cm")
        print("\n".join(person_details))
        
    def shortest(self):
        if not self.people:
            return None
        shortest_person = min(self.people, key=lambda person: person.height)
        return shortest_person
    
    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.people.remove(shortest_person)
        return shortest_person
        
        
    
if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()