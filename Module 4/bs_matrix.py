def searchMatrix(matrix , target) :
    rows , cols = len(matrix) , len(matrix[0])

    start , end = 0 , rows * cols - 1

    while start <= end :
        mid =  start + (end - start) // 2
        mid_element = matrix[mid // cols][mid % cols]

        if mid_element == target:
            return True
        elif mid_element < target :
            start = mid + 1
        else : 
            end = mid - 1
    
    return False

matrix = [[1,2,3,4,5] , [6,7,8,9,10] , [11,12,13,14,15]]
target = 16

print(searchMatrix(matrix , target))
