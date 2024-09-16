# Write your solution here
 
phone_book = {}
 
def search():
    name = input("name:")
    try:
        for item in phone_book[name]:
            print(item)
    except KeyError as e:
        print("no number")
        return
 
 
def add():
    name = input("name:")
    number = input("number:")
 
    if name not in phone_book:
        phone_book[name] = []
 
    phone_book[name].append(number)
    print("ok!")
 
def main():
    while True:
        match (input("command (1 search, 2 add, 3 quit)")):
            case "1":
                search()
            case "2":
                add()
            case "3":
                print("quitting...")
                break
            
main()