# Creating a 2D array (3x3 matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)

# Accessing an element in 2D array
print("Element at row 1, column 2:", matrix[1][2])

# Iterating through rows
print("Iterating through rows:")
for row in matrix:
    print(row)

# iterating rowise
for i in range(len(matrix)) :
    for j in range(len(matrix[i])):
        print(matrix[i][j] , end=' ')
    print()

# Iterating through columns
print("Iterating through columns:")
for i in range(len(matrix[0])):
    for row in matrix:
        print(row[i], end=' ')
    print()


# Creating a 2x2 matrix with nested list comprehensions
new_matrix = [[i + j for j in range(2)] for i in range(2)]
print("New Matrix:", new_matrix)

# Transposing a matrix
transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Transposed Matrix:", transposed_matrix)
