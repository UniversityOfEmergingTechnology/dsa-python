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

    def find_middle_element(self , current_size = None):
        # have stack size and calculate middle index
        if current_size == None :
            current_size = self.size()
        
        if current_size == 0:
            return None # if stack is empty edge case

        middle_index = (current_size // 2) + (current_size % 2)

        # recursive traversal
        def _find_and_restore(middle , counter = 1) :

            # base case
            if middle == counter :
                middle_element = self.pop()
                self.push(middle_element)
                return middle_element

            top = self.pop()
            result = _find_and_restore(middle , counter + 1)
            # backtracking
            self.push(top)

            return result

        return _find_and_restore(middle_index)

s = Stack()


s.push(1)
s.push(2)
s.push(3)
s.push(4)


print(s.items)

print(f"The middle element is {s.find_middle_element()}")
