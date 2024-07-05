from queue import Queue

def interleaveQueue(qt):
    n = qt.qsize()

    if n % 2 != 0:
        print('Queue requires an even number of elements')
        return

    # to store the first half
    halfQueue = Queue()

    # separate the halves
    for _ in range(n // 2):
        halfQueue.put(qt.get())
    
    # interleave the halves
    while not halfQueue.empty():
        """ put one from the first half """
        qt.put(halfQueue.get())
        # move one from the second half to the correct position
        qt.put(qt.get())
    
    return qt


q = Queue()

for i in range(1,7):
    q.put(i)

interleaveQueue(q)

while not q.empty():
    print(q.get() , end=" ")