from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current = ListNode()
        head = current

        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        
        if list1:
            current.next = list1
        
        if list2:
            current.next = list2
        return head.next

    def print(self, node):
        while node:
            print(node.val)
            node = node.next
    
s = Solution()
a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)

b= ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)


s.print(s.mergeTwoLists(a,b))    