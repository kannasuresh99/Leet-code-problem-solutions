#my solution
class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        current_node = head
        while current_node:
            if current_node.next is not None:
                if current_node.val == current_node.next.val:
                    current_node.next = current_node.next.next
            if current_node.next is not None:
                if current_node.val == current_node.next.val:
                    current_node = current_node
                else:
                    current_node = current_node.next
            else:
                current_node = current_node.next
        return head