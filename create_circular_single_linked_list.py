#creation of circular singly linked list
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
            if node.next == self.head:
                break
            node = node.next
    #inserting elements in linkedlist
    def insert_ssl(self,value,location):
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
    
    def createCSLL(self,value):
        node = ListNode(value)
        node.next = node
        self.head = node
        self.tail = node
        return "Circular Linkedlist has been created"



                


circular_sll = LinkedList()
circular_sll.createCSLL(1)
circular_sll.createCSLL(2)
circular_sll.createCSLL(3)
print([node.val for node in circular_sll])