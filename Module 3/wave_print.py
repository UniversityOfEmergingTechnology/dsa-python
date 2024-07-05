def wavePrint(matrix) :
    rows , cols= len(matrix) , len(matrix[0])

    for col in range(cols):
        # top to bottom
        if col % 2 == 0 :
            for row in range(rows) :
                print(matrix[row][col] , end = " ")
        else :
            # bottom to top
            for row in range(rows - 1 , -1 , -1) :
                print(matrix[row][col] , end = " ")
matrix = [[1,2,3] , [4,5,6] ,[7,8,9]]
wavePrint(matrix)


# T.C - O(rows * cols)
# S.C - O(1)
