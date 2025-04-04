def add_matrices(A, B):
    """Adds two matrices."""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def transpose(matrix):
    """Finds the transpose of a matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

A = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

B = [[9, 8, 7], 
     [6, 5, 4], 
     [3, 2, 1]]

sum_matrix = add_matrices(A, B)
transpose_matrix = transpose(sum_matrix)

# Print results
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nSum of Matrices:")
for row in sum_matrix:
    print(row)

print("\nTranspose of the Sum:")
for row in transpose_matrix:
    print(row)
