class CircularQueue :
    def __init__(self , size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self , item):
        # whether queue is full
        if(self.rear + 1) % self.size == self.front :
            print("The circular queue is full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("The circular queue is empty")
        elif self.rear == self.front :
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else :
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    
    def display(self):
        if self.front == -1:
            print("The circular queue is empty")
        elif self.rear >= self.front :
            for i in range(self.front , self.rear + 1):
                print(self.queue[i] , end = ' ')
        else:
            for i in range(self.front , self.size):
                print(self.queue[i] , end = ' ')
            for i in range( 0 , self.rear + 1):
                print(self.queue[i] , end = ' ')

cq = CircularQueue(5)

cq.dequeue()
print()
cq.display()
