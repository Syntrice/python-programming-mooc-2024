# upgrade this solution

def read_matrix():
    result = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.split(",")
            for value in line:
                result.append(int(value))
    return result

def matrix_sum():
    return sum(read_matrix())

def matrix_max():
    return max(read_matrix())
    
def row_sums():
    result = []
    with open("matrix.txt") as file:
        for line in file:
            line_result = []
            line = line.split(",")
            for value in line:
                line_result.append(int(value))
            result.append(sum(line_result))
    return result


if __name__ == "__main__":
    print(matrix_sum())