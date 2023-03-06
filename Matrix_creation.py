def create_matrix(n):
    # Create an empty matrix
    matrix = []
    # Iterate over rows and columns and add elements to the matrix
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    # Return the matrix
    return matrix

# Example usage
matrix = create_matrix(3)
print(matrix)