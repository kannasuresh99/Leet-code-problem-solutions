#creation of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #inserting elements in linkedlist
    def insert_sll(self,value,location):
        newNode = ListNode(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.next = nextNode
    
    def tranverse_sll(self):
        if self.head is None:
            return "The Linked List is empty"
        else:
            current_node = self.head
            while current_node:
                print(current_node.val)
                current_node = current_node.next

                


singlylinkedlist = LinkedList()
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)

# singlylinkedlist.head = node1
# singlylinkedlist.head.next = node2
# singlylinkedlist.head.next.next = node3
# singlylinkedlist.tail = node3
singlylinkedlist.insert_sll(22,0)
singlylinkedlist.insert_sll(44,-1)
singlylinkedlist.insert_sll(66,-1)
singlylinkedlist.insert_sll(23,-1)
singlylinkedlist.insert_sll(67,0)
print([node.val for node in singlylinkedlist])
singlylinkedlist.tranverse_sll()