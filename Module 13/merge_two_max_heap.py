import heapq

def mergeHeaps(heap1 , heap2):
    # combine two heaps into single array

    merged_heap = heap1 + heap2

    return merged_heap

# convert combined array into max heap

def heapify(arr , n , i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right] :
        largest = right
    
    # change root if needed
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]

        # heapify the root
        heapify(arr , n , largest)

def buildMaxHeap(arr):
    n = len(arr)

    # build a maxheap

    for i in range(n // 2 - 1 , -1 , -1):
        heapify(arr , n , i)



heap1 = [10,5,6,2]
heap2 = [12,7,9]

merged_heap = mergeHeaps(heap1 , heap2)

buildMaxHeap(merged_heap)
print(merged_heap)