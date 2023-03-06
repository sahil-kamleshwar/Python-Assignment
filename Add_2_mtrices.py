def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions!")
        return None
    # Create a new matrix to store the result
    result = []
    # Iterate through the matrices and add the corresponding elements
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    # Return the result
    return result

# Example usage
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
print(add_matrices(matrix1, matrix2)) # Output: [[6, 8], [10, 12]]

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
print(add_matrices(matrix1, matrix2)) # Output: [[8, 10, 12], [14, 16, 18]]

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6, 7], [8, 9, 10]]
add_matrices(matrix1, matrix2) # Output: "Matrices must have the same dimensions!"