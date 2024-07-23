# Write your solution here
 
def column_correct(sudoku: list, column_no: int):
    column = [v[column_no] for v in sudoku if v[column_no] != 0]
    return len(column) == len(set(column))
 