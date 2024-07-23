# Write your solution here
def squared(string, size):
    for i in range(size):
        for j in range(size):
            print(string[(i*size+j) % len(string)],end="")
        print("")