# Write your solution here
 
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    database.append({
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    })
    
def find_movies(database: list, search_term: str):
    return [movie for movie in database if search_term.lower() in movie["name"].lower() or search_term.lower() in movie["director"].lower()]
