# from array import array

# # python list with mixed data types
# mixed_list = [1 , "Hello" , 3.14 , [2,4,6]]

# # python array with integer type

# int_array = array('i' , [1,2,3,4])



# dynamic_array = [1,2,3,2]
# print("Initial array " , dynamic_array)


# # adding an element to the end of the array
# dynamic_array.append(4)
# print("Array after appending " , dynamic_array)

# # removing element
# dynamic_array.remove(2)
# print("Array after removing an element " , dynamic_array)


# # accessing element

# print("Element at index 1 " , dynamic_array[1])


# # iterating through dynamic

# for element in dynamic_array : 
#     print(element , end = ' ')

# 2d arrays

# matrix = [[1,2,3,4] , [5,6,7,8], [9,10,11,12]]
# row size
# print(len(matrix))
# # col size
# print(len(matrix[0]))

# print(matrix)
# # accessing an element
# print(matrix[1][1])


# iterating through rows

# print("Iterating through rows")
# for row in matrix :
#     print(row)


# # where we can access each and every element in the matrix
# rowsize = len(matrix)
# colsize = len(matrix[0])

# for i in range(rowsize) :
#     for j in  range(colsize) :
#         print(matrix[i][j] , end = ' ')


# # iterating through columns
# print()
# print()
# print("Iterating through columns")
# for i in range(colsize):
#     for row in matrix :
#         print(row[i] , end =' ')
#     print()

# modifying an element
# matrix[0][3] = 40
# print(matrix)


# List comprehension

# squared_numbers = [x**2 for x in range(11)]
# print(squared_numbers)

# nested list comprehension

# matrix =  [[j for j in range(4)] for i in range(3)]
# print(matrix)

# # transforming a matrix using nested list comprehension

# transformed_matrix = [[element * 2 for element in row] for row in matrix]
# print("Tranformed matrix" , transformed_matrix)


# new_matrix = [[i + j for j in range(2)] for i in range(2)]
# print(new_matrix)


matrix = [[1,2,3,4] , [5,6,7,8] , [9,10,11,12]]
# example -  transposing a matrix
# transposed_matrix = [[matrix[j][i] for j  in range(len(matrix))] for i in range(len(matrix[0]))]
# print(transposed_matrix)

# example - searching a matrix

search_element = 15
found = False

for row in matrix : 
    if search_element in row :
        found = True
        break

print(f"element {search_element} found - " , found)


