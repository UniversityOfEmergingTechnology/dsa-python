# def countInversionsBruteForce(arr) :
#     inv_count = 0
#     n = len(arr)
    
#     for i in range(n):
#         for j in range( i + 1 , n ):
#             if arr[i] > arr[j]:
#                 inv_count += 1
    
#     return inv_count



# arr = [8 , 4 , 2 , 1]
# print(countInversionsBruteForce(arr))


def countInversions(arr):
    def merge(arr , temp , left ,mid ,right):
        i , j , k = left , mid + 1 , left
        inv_count = 0
        while i <= mid  and j <= right :
            if arr[i] <= arr[j] :
                temp[k] = arr[i]
                i += 1
            else : # we actually count over here because arr[i] > arr[j] and i < j
                temp[k] = arr[j]
                j += 1
                inv_count += mid - i + 1
            k += 1
        
        while i <= mid :
            temp[k] = arr[i]
            i += 1
            k += 1
            
        while j <= right :
            temp[k] = arr[j]
            j += 1
            k += 1
        
        for idx in range(left , right + 1):
            arr[idx] = temp[idx]
            
        return inv_count
        
        
    def mergeSort(arr , temp , left , right):
        inv_count = 0
        
        if left < right :
            mid = (left + right) // 2
            inv_count += mergeSort(arr , temp , left , mid)
            inv_count += mergeSort(arr , temp , mid + 1 , right)
            inv_count += merge(arr , temp , left , mid , right)
            
        return inv_count
    temp = arr[:]
    return mergeSort(arr , temp , 0 , len(arr) - 1)


arr = [8 ,4 , 2 , 1]
print("Number of inversions : " , countInversions(arr))