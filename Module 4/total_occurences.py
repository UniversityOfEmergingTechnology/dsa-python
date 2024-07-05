import bisect
def firstOccurence(arr , target) :
    start , end , ans = 0 , len(arr) - 1 , -1

    while start <= end :
        mid = start + (end - start) // 2

        if arr[mid] == target : 
            ans = mid
            end = mid - 1
        elif arr[mid] < target :
            start = mid + 1
        else : 
            end = mid - 1
    return ans 

def totalOccurences(arr,target) :
    # first = bisect.bisect_left(arr , target)
    first = firstOccurence(arr,target)
    last = bisect.bisect_right(arr , target) - 1


    return last - first + 1


arr = [1 , 2 , 3 ,3 , 3 , 3 , 4, 5, 6]
target = 3

result = totalOccurences(arr , target)

print(result)