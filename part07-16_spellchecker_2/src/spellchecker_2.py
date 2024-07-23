# write your solution here

from difflib import get_close_matches

# load the wordlist into a list of strings
def load_wordlist(path: str) -> list[str]:
    wordlist = []
    with open(path) as file:
        for word in file:
            wordlist.append(word.strip())
    return wordlist

def spellcheck(text: str, wordlist: list[str]) -> tuple[str, list]:
    """ Checks words in a string against a list of correct words

    Args:
        text (str): the text to check
        wordlist (list[str]): the list of correct words to check against

    Returns:
        result, the formatted string to highlight errors
        suggestions, a list of suggestion for all incorrect words
    """
    
    result = ""
    suggestions = []
    
    for word in text.split():
        if word.lower() not in wordlist:
            
            suggestion = ", ".join(get_close_matches(word, wordlist))
            suggestions.append(f"{word}: {suggestion}")
            
            word = f"*{word}*"
        result += word + " "
    
    return result, suggestions

def main():
    
    text = input("Write text:") 
    correct_words = load_wordlist("wordlist.txt")
    
    checked = spellcheck(text, correct_words)
    print(checked[0])
    print("suggestions:")
    for suggestion in checked[1]:
        print(suggestion)
    
main()