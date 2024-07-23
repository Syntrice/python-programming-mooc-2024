# Write your solution here
 
phone_book = {}
 
def search():
    name = input("name:")
    if name in phone_book:
        print(phone_book[name])
    else:
        print("no number")
 
def add():
    name = input("name:")
    number = input("number:")
    phone_book[name] = number
    print("ok!")
    
 
while True:
    match (input("command (1 search, 2 add, 3 quit)")):
        case "1":
            search()
        case "2":
            add()
        case "3":
            print("quitting...")
            break
 