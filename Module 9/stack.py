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
    

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print(f"Size is  {s.size()}")
print(f"Peek element of my stack is {s.peek()}")
s.print()





    

