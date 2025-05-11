# Definition for singly-linked list.
from typing import Optional
from heapq import heappush, heappop, heapify
import itertools 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def merge2list(self, a, b):
        result = ListNode()
        head = result
        while(a != None and b != None):
            if a.val < b.val:
                result.next = ListNode(a.val)
                a = a.next
            else: 
                result.next = ListNode(b.val)
                b = b.next
            result = result.next
        if a != None:
            result.next = a
        if b != None: 
            result.next = b 
        return head.next           
    
    def print(self, node):
        while node:
            print(node.val)
            node = node.next
    #Approach 1 with divide and conquer
    def mergeKLists1(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i+1] if i+1 < len(lists) else None
                temp.append(self.merge2list(a,b))
            lists = temp
        return lists[0]        
    def mergeKLists2(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        counter = itertools.count()
        for node in lists:
            heappush(minHeap, (node.val,next(counter), node))
        
        dummy  = ListNode()
        current = dummy
        while minHeap:
            val, _, node = heappop(minHeap)
            current.next = node
            current = current.next
            
            if node.next:
                heappush(minHeap, (node.next.val, next(counter), node.next))
        return dummy.next
            
s = Solution()
a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)

b= ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

c = ListNode(2)
c.next = ListNode(6)
s.print(s.mergeKLists2([a,b,c]))    