import heapq

# # create a min heap
# min_heap = []

# elements = [20,18,10,12,9,9,5,1]

# for element in elements:
#     heapq.heappush(min_heap , element)

# print("Min heap : " , min_heap)

# # pop elements from the heap

# while min_heap:
#     print("Popped" , heapq.heappop(min_heap))
# import heapq

# create a max heap

max_heap = []

elements = [20,18,10,12,9,9,5,1]

for element in elements:
    heapq.heappush(max_heap , -element)

print("Max heap(inverted) : " , max_heap)

# pop elements from the heap

while max_heap:
    print("Popped" , -heapq.heappop(max_heap))