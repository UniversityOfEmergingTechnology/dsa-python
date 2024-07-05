class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self , val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self,index):
        # access the parent index
        parent_index = (index - 1) // 2
        
        if index > 0 and self.heap[index] > self.heap[parent_index]: 
            # swap the parent value with current value
            self.swap(index , parent_index)
            self.heapify_up(parent_index)
    
    def delete(self):
        if len(self.heap) > 1:
            # swap first and last values
            self.swap(0 , len(self.heap) - 1)
            # remove the last value
            max_val = self.heap.pop()
            self.heapify_down()
        elif self.heap:
            max_val = self.heap.pop()
        else:
            max_val = None
        
        return max_val

    def heapify_down(self , index = 0):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest] :
            largest = left_child_index
        
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        
        if largest != index :
            self.swap(index , largest)
            self.heapify_down(largest)


    def swap(self , i , j):
        self.heap[i] , self.heap[j] = self.heap[j] , self.heap[i]


heap = MaxHeap()
heap.insert(20)
heap.insert(18)
heap.insert(10)
heap.insert(12)
heap.insert(9)
heap.insert(9)
heap.insert(5)
heap.insert(1)

print("After insertion" , heap.heap)

heap.delete()

print("After deletion" , heap.heap)
