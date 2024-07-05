class CircularDeque:
    def __init__(self , capacity) -> None:
        # +1 to distinguish full from empty
        self.capacity = capacity + 1
        self.deque = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def insertFront(self, value):
        if self.isFull():
            return False

        self.head = (self.head - 1) % self.capacity
        self.deque[self.head] = value
        return True

    def insertLast(self, value) :
        if self.isFull():
            return False
        
        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        return True
    
    def deleteFront(self , value):
        if self.isEmpty() :
            return False

        self.head = (self.head + 1) % self.capacity
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.capacity
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.deque[self.head]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.deque[(self.tail - 1) % self.capacity]
    
    def isEmpty(self):
        return self.head == self.tail
    
    def isFull(self):
        return (self.tail + 1) % self.capacity == self.head
    
