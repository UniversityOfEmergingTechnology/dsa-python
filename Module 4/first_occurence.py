import bisect

def useStandardFunctions(arr , target) : 
    first = bisect.bisect_left(arr , target)
    last = bisect.bisect_right(arr , target) - 1

    return first , last

def firstOccurence(arr , target):
    start , end , result = 0 , len(arr) - 1 , -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target : 
            result = mid
            end = mid - 1
        elif arr[mid] < target :
            start = mid + 1
        else:
            end = mid - 1
    
    return result

def lastOccurence(arr , target):
    start , end , result = 0 , len(arr) - 1 , -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target : 
            result = mid
            start = mid + 1
        elif arr[mid] < target :
            start = mid + 1
        else:
            end = mid - 1
    
    return result

arr = [1 , 2 , 3 , 3 ,4  , 4 , 4 , 4 , 4 , 6 , 7 , 9]
result = firstOccurence(arr , 4)
resultLast = lastOccurence(arr , 4)

builtinLeft , builtinRight = useStandardFunctions(arr , 4)

print(f"The first occurence is {result}")
print(f"The last occurence is {resultLast}")
print(f"The first occurence is {builtinLeft}")
print(f"The last occurence is {builtinRight}")
