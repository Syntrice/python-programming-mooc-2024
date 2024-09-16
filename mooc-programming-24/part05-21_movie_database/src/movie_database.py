# Write your solution here
 
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    database.append({
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    })