# Write your solution here
 
def row_correct(sudoku: list, row_no: int):
    sudoku_row = [v for v in sudoku[row_no] if v != 0]
    print(sudoku_row)
    print(len(sudoku_row))
    print(len(set(sudoku_row)))
    return len(sudoku_row) == len(set(sudoku_row))