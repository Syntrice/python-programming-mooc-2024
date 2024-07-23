# Write your solution here
 
def list_of_stars(stars: list[int]):
    for n in stars:
        print("*" * n)
        
        
if __name__ == '__main__':
    list_of_stars([2, 3])