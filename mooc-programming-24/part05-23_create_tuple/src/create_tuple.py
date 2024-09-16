# Write your solution here
 
def create_tuple(x: int, y: int, z: int):
    args = [x, y, z]
    return (min(args), max(args), sum(args))