# Write your solution here

def find_words(search_term: str) -> list[str]:
    if "." in search_term:
        search_term = search_term.replace(".", "")
    elif "*" in search_term:
        search_term = search_term.replace("*", "")
        
        