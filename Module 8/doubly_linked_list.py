class Node :
    def __init__(self , data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList :
    def __init__(self) -> None:
        self.head = None
        # self.tail = None

    
    # appending the nodes to end of list
        
    def append(self , data) :
        new_node = Node(data)

        if not self.head :
            self.head = new_node
            # self.tail = new_node
            return

        last = self.head
        while last.next :
            last = last.next
        
        last.next = new_node
        new_node.prev = last
        # self.tail = new_node

    # printing the list
    
    def print_list(self):
        curr_node = self.head

        while curr_node : 
            print(curr_node.data , end = " <-> ")
            curr_node = curr_node.next
        
        print("NULL")

    # def print_list_backwards(self):
    #     curr_node = self.tail

    #     while curr_node : 
    #         print(curr_node.data , end = " <-> ")
    #         curr_node = curr_node.prev
        
    #     print("NULL")

    # insert at the head
    def prepend(self , data) :
        new_node = Node(data)
        new_node.next = self.head

        if self.head :
            self.head.prev = new_node
            self.head = new_node

    def insert_after_node(self , prev_node , data):
        if not prev_node : 
            print("previos node is not in the list")
            return

        new_node = Node(data)
        new_node.prev = prev_node
        new_node.next = prev_node.next

        if prev_node.next : 
            prev_node.next.prev = new_node
            prev_node.next = new_node
    
    def delete_node(self,node) :
        if not node :
            return
        if node.prev :
            node.prev.next = node.next
        if node.next :
            node.next.prev = node.prev
        if node == self.head : 
            self.head = node.next
        
        node = None
    
dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.print_list()

dll.prepend(0)
dll.print_list()

dll.insert_after_node(dll.head.next.next , 2.5)
dll.print_list()

dll.delete_node(dll.head)
dll.print_list()

# dll.print_list_backwards()