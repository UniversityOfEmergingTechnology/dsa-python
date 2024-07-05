def findMissingNumber(arr ):
    start , end = 0 , len(arr) - 1

    while start <= end :
        midIndex = start + (end - start) // 2

        if arr[midIndex] != midIndex + 1 :
            # this means either we are on the answer or answer lies on left hand side
            if arr[midIndex - 1] == midIndex or midIndex == 0:
                return midIndex + 1
            end = midIndex - 1
        else :
            # if until now at middle we are not having missing number so that means answer lie on right hand side
            start = midIndex + 1


arr = [2,3,4,5,6]
result = findMissingNumber(arr)
print(result)