def solve(arr):
    s  , e = 0 , len(arr) - 1

    while s <= e :
        mid = s  + (e - s) // 2
        if s == e :
            return s
        
        # two cases mid is even or odd

        if mid % 2 == 0 :
            if arr[mid] == arr[mid + 1] :
                s = mid + 2
            else :
                e = mid 
        else :
            if arr[mid] == arr[mid - 1] :
                s = mid + 1 
            else :
                e = mid - 1
                
    return -1

arr = [1,1,2,2,1]

ans = solve(arr)

print(f"The index is {ans}")
print(f"The element is {arr[ans]}")