# write your solution here

def load_wordlist(path: str) -> list[str]:
    wordlist = []
    with open(path) as file:
        for word in file:
            wordlist.append(word.strip())
    return wordlist

def highlight_errors(text: str, wordlist: list[str]) -> str:
    result = ""
    for word in text.split():
        if word.lower() not in wordlist:
            word = f"*{word}*"
        result += word + " "
    
    return result

def main():
    
    text = input("Write text:") 
    correct_words = load_wordlist("wordlist.txt")
    print(highlight_errors(text, correct_words))
    
main()
