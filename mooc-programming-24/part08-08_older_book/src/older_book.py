# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------

def older_book(book1: Book, book2: Book):
    oldest = book1
    
    if book1.year < book2.year:
        oldest = book1
    elif book2.year < book1.year:
        oldest = book2
    else:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")
        return
    
    print(f"{oldest.name} is older, it was published in {oldest.year}")