# Write your solution here

def read_input(msg: str, low: int, high: int):
    while True:
        try:
            number = int(input(msg))
        except ValueError:
            print(f"You must type in an integer between {low} and {high}")
            continue
        
        if low <= number <= high:
            return number
        else:
            print(f"You must type in an integer between {low} and {high}")
            
            
if __name__ == "__main__":
    number = read_input("num", 5, 10)
    print(number)