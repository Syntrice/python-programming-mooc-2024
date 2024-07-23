def transpose(matrix: list):
    matrix[:] = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
 
if __name__ == "__main__":
    m = [[1, 2], [3, 4], [5, 6]]
    print(m)
    transpose(m)
    print(m)