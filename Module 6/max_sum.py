def maxSumNonAdjacent(arr , index = 0) :
    # base case if we are beyond the last index
    if index >= len(arr) :
        return 0
    
    # choice 1 include current element and skip the next
    include = arr[index] + maxSumNonAdjacent(arr , index + 2)

    # choice 2 skip the current element 
    exclude = maxSumNonAdjacent(arr , index + 1)

    # return maximum of including the element and excluding the element
    return max(include , exclude)

arr = [3 , 2 , 7 , 10]
print(maxSumNonAdjacent(arr))