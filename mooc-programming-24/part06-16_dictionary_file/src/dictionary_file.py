# Write your solution here

running = True
dictionary = []
with open("dictionary.txt") as file:
    for line in file:
        dictionary.append(line.strip())

while running:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    
    match function:
        case "1":
            finnish = input("The word in Finnish: ")
            english = input("The word in English: ")
            dictionary.append(f"{finnish} - {english}")
            with open("dictionary.txt", "a") as file:
                file.write(f"{finnish} - {english}\n")
            print("Dictionary entry added")
        case "2":
            search = input("Search term: ")
            for entry in dictionary:
                if search in entry:
                    print(entry)
        case "3":
            running = False
            print("Bye!")
        
        
        