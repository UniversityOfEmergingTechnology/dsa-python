def exponential_bs(arr , target) :
    if arr[0] == target :
        return 0
    
    index = 1

    while index < len(arr) and arr[index] <= target :
        index *= 2
    
    # perform binary search
    
    left , right = index // 2 , min(index , len(arr) - 1)

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target : 
            return mid
        elif arr[mid] < target :
            left = mid + 1
        else : 
            right = mid - 1
    
    return -1


arr = [i for i in range(1 , 51)]
target = 1

print("Index of " , target , " : " , exponential_bs(arr,target))