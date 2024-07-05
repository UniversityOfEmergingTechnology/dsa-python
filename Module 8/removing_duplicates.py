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

    def remove_duplicates_sorted(self):
        current = self.head

        while current and current.next :
            if current.data == current.next.data :
                current.next = current.next.next
            else :
                current = current.next
    
    def remove_duplicates_unsorted(self) :
        # using buffer
        if not self.head or not self.head.next :
            return
        
        seen = set()

        current = self.head

        seen.add(self.head.data)

        while current.next :
            if current.next.data in seen:
                current.next = current.next.next
            else :
                seen.add(current.next.data)
                current = current.next
    def remove_duplicates_unsorted_without_space(self):
        current = self.head
        while current :
            runner = current 
            while runner.next :
                if runner.next.data == current.data :
                    runner.next = runner.next.next
                else :
                    runner = runner.next
            
            current = current.next



linked_list = LinkedList()
linked_list_unsorted = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
linked_list.append(3)
linked_list.append(4)
linked_list.append(4)
linked_list.print_list()
linked_list.remove_duplicates_sorted()
linked_list.print_list()


linked_list_unsorted.append(1)
linked_list_unsorted.append(5)
linked_list_unsorted.append(4)
linked_list_unsorted.append(3)
linked_list_unsorted.append(2)
linked_list_unsorted.append(4)
linked_list_unsorted.append(3)
linked_list_unsorted.append(2)
linked_list_unsorted.append(1)
linked_list_unsorted.print_list()
linked_list_unsorted.remove_duplicates_unsorted()
linked_list_unsorted.remove_duplicates_unsorted_without_space()
linked_list_unsorted.print_list()