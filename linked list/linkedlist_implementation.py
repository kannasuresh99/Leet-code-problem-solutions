class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        """add a element at the end of a linkedlist"""
        new_data = Node(data)
        
        if self.head is None:
            self.head = new_data
            return
        
        current = self.head
        
        while current.next:
            current = current.next
        current.next = new_data
        return
    
    def prepend(self, data):
        "add a element at the start of a linkedlist"
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data
        return
    
    def delete(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
            
    def display(self):
        node_list = []
        current = self.head
        while current:
            node_list.append(current.data)
            current = current.next
        print(" -> ".join(map(str, node_list)))
            
    def insert_after(self, prev_node_value, data):
        if self.head is None:
            return
        
        new_data = Node(data)
        
        current = self.head
        
        while current:
            if current.data == prev_node_value:
                new_data.next = current.next
                current.next = new_data
                return
            current = current.next
    
    def search(self, data):
        if self.head is None:
            return False
        
        current = self.head
        
        while current:
            if current.data == data:
                return True
            current = current.next
        
        return False
    
    def get_length_of_linkedlist(self):
        if self.head is None:
            return 0
        
        current = self.head
        length = 0
        
        while current:
            length += 1
            current = current.next
        
        return length

    def reverse(self):
        """
        Input: 1->2->3->4->None
        prev = None
        curr = 1->2->3->4->None
        
        loop starts
        
        iteration 1:
        next_node = 2->3->4->None
        curr = 1->None
        prev = 1->None
        curr = 2->3->4->None
        
        iteration 2:
        next_node = 3->4->None
        curr = 2->1->None
        prev = 2->1->None
        curr = 3->4
        
        iteration 3:
        next_node = 4->None
        curr = 3->2->1->None
        prev = 3->2->1->None
        curr = 4->None
        
        iteration 4:
        next_node = None
        curr = 4->3->2->1->None
        prev = 4->3->2->1->None
        curr = None
        
        loop breaks
        """
        if self.head is None:
            return
        
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            
            prev = curr
            curr = next_node
        
        self.head = prev
    
    
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.display()  # Output: 0 -> 1 -> 2 -> 3

linked_list.delete(2)
linked_list.display()  # Output: 0 -> 1 -> 3
linked_list.insert_after(1,2)
linked_list.display()
key_to_search = 6
if linked_list.search(key_to_search):
    print(f"{key_to_search} is present in the linkedlist")
else:
    print(f"{key_to_search} is not present in the linkedlist")
print(linked_list.get_length_of_linkedlist())
linked_list.append(4)
linked_list.reverse()
linked_list.display()
linked_list.delete(4)
linked_list.display()
linked_list.delete(0)
linked_list.display()
linked_list.prepend(4)
linked_list.append(0)
linked_list.reverse()
linked_list.display()
