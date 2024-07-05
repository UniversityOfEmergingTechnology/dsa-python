def isArraySorted(arr , index = 0):
    # base case if we're at the last element or if array is empty
    if index == len(arr) - 1 or len(arr) == 0 :
        return True

    # if the current element is greater than next one array is not sorted
    if arr[index] > arr[index + 1] :
        return False

    # recursive step
    return isArraySorted(arr , index + 1)

print(isArraySorted([1,2,3,4] ))
print(isArraySorted([1,2,4,3] ))