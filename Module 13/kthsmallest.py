import heapq

def kthsmallest_max_heap(arr , k ):
    # create max heap of first k elements

    max_heap = [-x for x in arr[:k]]
    heapq.heapify(max_heap)

    # process the remaining elements

    for num in arr[k:]:
        if num < -max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap , -num)

    return -heapq.heappop(max_heap)


arr = [7 , 10, 4 , 3 , 20 , 15]
k = 3

print(kthsmallest_max_heap(arr , k))
