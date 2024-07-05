def quicksort(arr , low , high ):
    if low < high :
        pi = partition(arr , low , high)

        # separately sort elements before and after partition
        quicksort(arr , low ,  pi - 1)
        quicksort(arr , pi + 1 , high)


def partition(arr , low , high):
    # choosing the last element as pivot
    pivot = arr[high]

    i = low - 1

    for j in range(low , high):
        # if current element is smaller than or equal to pivot
        if arr[j] <= pivot :
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]
    
    arr[i + 1] , arr[high] = arr[high] , arr[i + 1]

    return i + 1

arr = [1 , 0, 7 , 8, 9, 1 ,5]

n = len(arr)
quicksort(arr , 0 , n - 1)

print("Sorted array " , arr)