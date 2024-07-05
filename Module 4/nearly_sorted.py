def modifiedBinarySearch(arr,target) : 
    start , end = 0 , len(arr) - 1

    while start <= end :
        mid = start + (end - start) // 2

        if arr[mid] == target : 
            return mid
        
        if mid > start and arr[mid - 1] == target : 
            return mid - 1
        
        if mid < end and arr[mid + 1] == target : 
            return mid + 1
        
        # move end and start pointers

        if arr[mid] > target : 
            end = mid - 2
        else :
            start = mid + 2
    
    return -1


arr = [10,3,40,20,50,80,70]

print(modifiedBinarySearch(arr , 100))
        