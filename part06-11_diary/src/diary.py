# Write your solution here

running = True
while running:
    print("1 - add an entry, 2 - read entries, 0 - quit")

    match input("Function: "):
        case "1":
            entry = input("Diary entry: ")
            with open("diary.txt", "a") as file:
                file.write(entry + "\n")
            
            print("Diary saved")
        case "2":
            print("Entries:")
            with open("diary.txt") as file:
                for line in file:
                    print(line, end="")
        case "0": 
            print("Bye now!")
            running = False
            
            
# actual solution should probably first load all entries into a list, 
# then add new entries to the list and write the whole list back to the file.
# this way the file is only opened once for reading and once for writing, better than appending to the file every time.