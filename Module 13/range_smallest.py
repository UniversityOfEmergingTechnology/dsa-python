import heapq

def smallestRange(nums):
    min_heap = []

    current_max = float('-inf')

    # intialize the heap with the first element of each list

    for i , lst in enumerate(nums):
        heapq.heappush(min_heap , (lst[0] , i , 0))
        current_max = max(current_max , lst[0])
    
    min_range = float('inf')

    range_start , range_end = -1 , -1

    # merge process

    while min_heap :
        min_val , list_index , element_index = heapq.heappop(min_heap)

        # update the smallest range
        if current_max - min_val < min_range:
            min_range = current_max - min_val
            range_start , range_end = min_val , current_max
        
        # if there is a next element in same list, push it into heap
        if element_index + 1 < len(nums[list_index]) :
            next_val = nums[list_index][element_index + 1]
            heapq.heappush(min_heap , (next_val , list_index , element_index + 1))
            current_max = max(current_max , next_val)
        else :
            break

    return [range_start , range_end]


nums = [
    [4,10,15,24,26],
    [0 , 9, 12 , 20],
    [5,18,22,30]
]

result = smallestRange(nums)
print("Smallest range is : " , result)
 
