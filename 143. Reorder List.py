from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        #approach with stack
        # l = []
        # current = head
        # while current:
        #     l.append(current)
        #     current = current.next
            
        # res = ListNode()
        # current = res
        # n = len(l) if (len(l) % 2) ==0 else len(l) - 1 
        # for i in range(0, int(n/2)):
        #     current.next = l.pop(0)
        #     current = current.next
        #     current.next = l.pop()
        #     current = current.next
        #     current.next = None
        # if l:
        #     current.next = l[0]
        #     current.next.next = None
        # return res.next
        
        #Approach without stack
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        print("Mid", mid.val)
        #reversing second half
        prev = None
        current = mid
        while current.next:
            nex = current.next
            current.next = prev
            prev = current
            current = nex
        current.next = prev
        s.print(current)
    
        res = ListNode()
        dummy = res
        first = head
        second =current
        while first != mid:
            res.next = first
            first = first.next
            res.next.next = second
            res = res.next.next
            second = second.next
        return dummy.next
    
    def print(self, node):
        print('')
        while node:
            print(node.val, end= ' ')
            node = node.next    

        
s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next= ListNode(4)
s.print(s.reorderList(node))
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next= ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(6)
s.print(s.reorderList(node))
#node.next.next.next.next = ListNode(5)
#node.next.next.next.next.next = ListNode(6)
