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
    
    def has_cycle(self):
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# Make it circular (connecting the last node to the first node)
ll.head.next.next.next.next = ll.head.next

if ll.has_cycle():
    print("The linked list is circular.")
else:
    print("The linked list is not circular.")