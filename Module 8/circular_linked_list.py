class Node :
    def __init__(self , data) -> None:
        self.data = data
        self.next = None
    

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self , data) : 

        if not self.head : 
            self.head = Node(data)
            self.head.next = self.head
        else :
            new_node = Node(data)
            curr = self.head

            while curr.next !=self.head :
                curr = curr.next

            curr.next = new_node
            new_node.next = self.head

    def print_list(self) :
        curr = self.head

        while curr : 
            print(curr.data , end = " -> ")
            curr = curr.next
            if curr == self.head :
                break
        print("Circular link")


    def prepend(self , data) :
        new_node = Node(data)

        curr = self.head
        new_node.next = self.head

        if not self.head :
            new_node.next = new_node
        else :
            while curr.next != self.head :
                curr = curr.next
            
            curr.next = new_node
            self.head = new_node

cll = CircularLinkedList()

cll.append(1)
cll.append(2)
cll.append(3)
cll.print_list()

cll.prepend(0)
cll.print_list()