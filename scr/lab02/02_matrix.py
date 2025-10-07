def transpose(mat):
    if not isinstance(mat, list):
        raise TypeError("Input must be a list")
    
    if len(mat) == 0:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("All elements must be lists")
        if len(row) != row_length:
            raise ValueError("Jagged matrix is not allowed")
    
    transposed = []
    for col_index in range(len(mat[0])):
        new_row = []
        for row_index in range(len(mat)):
            new_row.append(mat[row_index][col_index])
        transposed.append(new_row)
    
    return transposed


def row_sums(mat):
    if not isinstance(mat, list):
        raise TypeError("Input must be a list")
    
    if len(mat) == 0:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("All elements must be lists")
        if len(row) != row_length:
            raise ValueError("Jagged matrix is not allowed")
    
    sums = []
    for row in mat:
        row_sum = 0
        for element in row:
            row_sum += element
        sums.append(row_sum)
    
    return sums


def col_sums(mat):
    if not isinstance(mat, list):
        raise TypeError("Input must be a list")
    
    if len(mat) == 0:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("All elements must be lists")
        if len(row) != row_length:
            raise ValueError("Jagged matrix is not allowed")
    
    sums = []
    for col_index in range(len(mat[0])):
        col_sum = 0
        for row_index in range(len(mat)):
            col_sum += mat[row_index][col_index]
        sums.append(col_sum)
    
    return sums

print("=== transpose ===")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
try:
    print(transpose([[1, 2], [3]]))
except ValueError as e:
    print("Error:", e)
    
print("\n=== row_sums ===")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
try:
    print(row_sums([[1, 2], [3]]))
except ValueError as e:
    print("Error:", e)
    
print("\n=== col_sums ===")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
try:
    print(col_sums([[1, 2], [3]]))
except ValueError as e:
    print("Error:", e)
