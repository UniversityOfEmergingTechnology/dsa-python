def binary_search_recursive(arr , target , start  , end):
    # base condition

    if start > end :
        return -1
    
    middle = start + (end - start) // 2

    if arr[middle] == target : 
        return middle
    # recursive step
    elif arr[middle] < target :
        return binary_search_recursive(arr , target , middle + 1 , end)
    else :
        return binary_search_recursive(arr , target , start , middle - 1)
    

arr = [1,2,3,4,5,6,7,8,9]

target = 5

print(binary_search_recursive(arr , target , 0 , len(arr) - 1))