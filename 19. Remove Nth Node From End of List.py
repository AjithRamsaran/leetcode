from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        while n  > 0:
            fast = fast.next
            n -= 1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next if slow.next else None
        return dummy.next
    def print(self, node):
        while node:
            print(node.val)
            node = node.next    
s = Solution()
a = ListNode(1)
a.next =  ListNode(2)
a.next.next =  ListNode(3)
a.next.next.next =  ListNode(4)
a.next.next.next.next =  ListNode(5)

s.print(s.removeNthFromEnd(a, 2))