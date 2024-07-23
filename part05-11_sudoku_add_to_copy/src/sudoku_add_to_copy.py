# Write your solution here
 
def print_sudoku(sudoku: list):
    for row in range(9):
        for col in range(9):
            print(" ", end="")
            if col in (3,6):
                print(" ",end="") 
            print("_" if sudoku[row][col] == 0 else sudoku[row][col],end="")
        if row in (2,5):
            print("")
        print("")
        
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    result = [[i for i in row] for row in sudoku]
    result[row_no][column_no] = number
    return result