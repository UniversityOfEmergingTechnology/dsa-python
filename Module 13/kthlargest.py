import heapq

def kthGreatest_min_heap(arr , k):

    # create a min heap with first k elements

    min_heap = arr[:k]
    heapq.heapify(min_heap)

    # process the remaining elements
    for num in arr[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap , num)
    # root of the min heap is kth greatest element
    return heapq.heappop(min_heap)

arr = [7 , 10, 4, 3 ,20,15]
k = 3

print(kthGreatest_min_heap(arr , k ))