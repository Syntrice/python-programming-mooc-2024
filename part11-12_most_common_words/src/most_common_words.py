# WRITE YOUR SOLUTION HERE:

def most_common_words(filename: str, lower_limit: int):
    words = {}
    punctuation = ".!?,;:"
    with open(filename) as file:
        for line in file:
            line = line.strip()
            for char in punctuation:
                line = line.replace(char, "")
            parts = line.split(" ")
            for part in parts:
                if part not in words:
                    words[part] = 0
                words[part] += 1
    
    return {word : words[word] for word in words.keys() if words[word] >= lower_limit}

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 1))