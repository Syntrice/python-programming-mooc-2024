# Write your solution here
 
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        for cell in row:
            if cell == element: count += 1
            
    return count