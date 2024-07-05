class Stack :
    def __init__(self) :
        # initialize an empty list to store stack elements 
        self.items = []
    
    def is_empty(self):
        # check if list is empty
        return not self.items
    
    def push(self , item):
        # add an item to top of the stack
        self.items.append(item)
    
    def pop(self) :
        if not self.is_empty() :
            # remove the topmost element from the stack
            return self.items.pop()

        return "Stack is empty"

    def peek(self):
        if not self.is_empty() :
            return self.items[-1]

        return "Stack is empty"


    def size(self) :
        return len(self.items)
    
    def print(self) :
        while not self.is_empty() :
            temp = self.pop()
            print(temp)
    
    def insert_at_bottom(self , item) :
        if self.is_empty():
            self.push(item)
        else :
            # remove all items recursively until stack is empty
            top = self.pop()
            self.insert_at_bottom(item)
            # backtracking
            self.push(top)
    

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.items)

s.insert_at_bottom(100)
s.insert_at_bottom(101)
s.insert_at_bottom(102)
print(s.items)
