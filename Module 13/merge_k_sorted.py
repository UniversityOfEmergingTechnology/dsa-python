import heapq

def mergeKSortedArray(arrays):

    # intialize the heap

    heap = []

    # push the first element of array into the heap
    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(heap , (arrays[i][0] , i , 0))
    
    # intialize the merged array
    merged = []

    # merge process

    while heap:
        # extract the smallest element from the heap
        val , array_index , element_index = heapq.heappop(heap)

        merged.append(val)

        # if there is a next element in same array push it into heap
        if element_index + 1 < len(arrays[array_index]):
            next_val = arrays[array_index][element_index + 1]

            heapq.heappush(heap , (next_val , array_index , element_index + 1))
        
    
    return merged

arrays = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

merged_array = mergeKSortedArray(arrays)

print(merged_array)