class Queue:
    def __init__(self) -> None:
        # intialize an empty list to represent my queue
        self.queue = []


    def enqueue(self , data):
        # add an item to the end of the queue
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            # remove the first item from the queue
            return self.queue.pop(0)
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0

    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.queue)
q.dequeue()
print(q.queue)

print(q.peek())