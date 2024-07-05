from queue import Queue
import collections


def reverseFirstKElements(qt , k):
    if qt.empty() or k <= 0:
        return 

    stack = collections.deque()

    # step 1 reverse k elements

    for _ in range(k):
        stack.append(qt.get())
    

    # step 2 re enqueue reversed elements to the queue
    while stack:
        qt.put(stack.pop())

    
    # step 3 rotate the rest of the queue
    for _ in range(qt.qsize() - k) :
        qt.put(qt.get())
    
    return qt

q = Queue()
for i in range(1,6):
    q.put(i)

reverseFirstKElements(q , 3)

while not q.empty():
    print(q.get() , end = ' ')