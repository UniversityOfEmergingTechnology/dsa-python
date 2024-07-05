class Node :
    def __init__(self , data) :
        self.data = data
        self.next = None


class LinkedList :
    def __init__(self):
        self.head = None

# inserting at the end of linked list
    def append(self , data) :
        new_node = Node(data)

        # whether my list is empty or not
        if self.head is None :
            self.head = new_node
            return
        
        last = self.head

        while last.next :
            last = last.next

        last.next = new_node
    
    def print_list(self) :
        cur_node = self.head

        while cur_node:
            print(cur_node.data , end = "-> ")
            cur_node = cur_node.next
        
        print("NULL")
    
    # insert at the head of linked list
    def prepend(self , data) :
        new_node = Node(data)
        # whether my list is empty or not
        if self.head is None :
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self , prev_node , data) :
        
        if not prev_node : 
            print("Previous node is not in list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    
    # deletion by value
    def delete_node(self, key) :
        curr_node = self.head

        if curr_node and curr_node.data == key :
            self.head = curr_node.next
            curr_node = None
            return
    
        prev = None
        while curr_node and curr_node.data != key : 
            prev = curr_node
            curr_node = curr_node.next
        
        if curr_node is None :
            return

        prev.next = curr_node.next
        curr_node = None


    

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()

linked_list.prepend(0)
linked_list.print_list()

linked_list.insert_after_node(linked_list.head.next, 1.5)
linked_list.print_list()

linked_list.delete_node(1.5)
linked_list.print_list()