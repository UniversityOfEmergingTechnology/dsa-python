class MyDeque:
    def __init__(self) -> None:
        self.items = []
    
    def addFront(self , item) :
        '''
            Adds an item to the front of the deque
        '''
        self.items.insert(0 , item)

    def addRear(self , item):
        # add an item to the rear of deque
        self.items.append(item)
    
    def removeFront(self) :
        # remove and return the item from the front of the deque
        if self.items:
            return self.items.pop(0)
        return None
    
    def removeRear(self):
        # remove and return item from rear of my deque
        if self.items:
            return self.items.pop()
        
        return None

    def isEmpty(self):
        # check if the deque is empty
        return not self.items

    def size(self):
        return len(self.items)
    
md = MyDeque()

md.addRear('apple')
md.addRear('orange')
md.removeRear()

print(md.items)