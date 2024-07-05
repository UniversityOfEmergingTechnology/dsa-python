def find_position(target) : 
    start , end = 0 , 1

    # expand the range exponentially until target is within the range
    while target > end :
        start = end
        end *= 2
    
    return binary_search(start , end , target)

def binary_search(start , end , target) :
    while start <= end :
        mid = start + (end - start) // 2
        if mid == target : 
            return mid
        elif mid < target : 
            start = mid + 1
        else :
            end = mid - 1
    return -1

print(find_position(30))