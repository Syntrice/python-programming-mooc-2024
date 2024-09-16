# Write your solution here
def chessboard(size):
    
    for y in range(size):
        for x in range(size):
            if y % 2 == 0:
                if x % 2 == 0:
                    print(1, end='')
                else:
                    print(0,end='')
            else:
                if x % 2 == 0:
                    print(0,end='')
                else:
                    print(1,end='')
        print()
    
# Testing the function
if __name__ == "__main__":
    chessboard(3)