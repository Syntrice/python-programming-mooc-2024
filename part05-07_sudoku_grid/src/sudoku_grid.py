# Write your solution here
 
def row_correct(sudoku: list, row_no: int):
    sudoku_row = [v for v in sudoku[row_no] if v != 0]
    return len(sudoku_row) == len(set(sudoku_row))
 
def column_correct(sudoku: list, column_no: int):
    column = [v[column_no] for v in sudoku if v[column_no] != 0]
    return len(column) == len(set(column))
 
def block_correct(sudoku: list, row_no: int, column_no: int):
    block = [j for i in sudoku[row_no:row_no+3] for j in i[column_no:column_no+3] if j != 0]
    return len(block) == len(set(block))
 
def sudoku_grid_correct(sudoku: list):
    for row in range(9):
        if not row_correct(sudoku,row):
            return False
        for column in range(9):
            if not column_correct(sudoku,column):
                return False
            if (row % 3 == 0 or row == 0) and (column % 3 == 0 or column == 0):
                if not block_correct(sudoku, row, column):
                    return False
    return True
            
if __name__ == "__main__":
 
    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
 
    print(sudoku_grid_correct(sudoku2))