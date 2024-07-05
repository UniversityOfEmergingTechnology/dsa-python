def mergeSort(arr):
    # if array contains more than one element then do splitting
    if len(arr) > 1 :
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L) # splitting the first half
        mergeSort(R) # splitting the right half

        merge(arr , L , R) # merging the sorted halves

def merge(arr , L , R) :
    i = j = k = 0

    # copy data to temp arrays

    while i < len(L) and j < len(R) :
        if L[i] < R[j] :
            arr[k] = L[i]
            i += 1
        else :
            arr[k] = R[j]
            j+= 1
        
        k+= 1


    # checking if any element was left in any of the arrays
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R) :
        arr[k] = R[j]
        j += 1
        k += 1

arr = [12,11,13,5,6,7]

mergeSort(arr)

print("Sorted array is " , arr)