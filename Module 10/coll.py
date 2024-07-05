from collections import deque

my_deque = deque()

# add to the end
my_deque.append('last')
# add to the front
my_deque.appendleft('first')

# pop from the end
my_deque.pop()
# pop from the front
my_deque.popleft()


# thread safe , memory efficient O(1)