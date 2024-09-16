# Write your solution here

def prime_numbers():
    n = 2
    while True:
        for num in range(2,n-1):
            if n % num == 0:
                n += 1
                break
        else:
            yield n
            n += 1
        
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(10):
        print(next(numbers))
    
    