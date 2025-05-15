# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        current = head
        nex = current.next 
        while nex:
            current.next = prev
            prev = current
            current = nex
            nex = nex.next
        current.next = prev
        return current