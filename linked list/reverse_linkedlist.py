"""
question link: https://leetcode.com/problems/reverse-linked-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        
        return prev

