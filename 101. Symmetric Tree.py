#time taken to solve: 30 mins both rucursion and iterative solution
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def isSame(p, q):
            if not p and not q:
                return True
            
            if not p or not q or p.val != q.val:
                return False
            
            return isSame(p.left, q.right) and isSame(p.right, q.left)
        return isSame(root.left, root.right)

        # q = deque()
        # q.append(root)
        # while q:
        #     n = len(q)
        #     l = []
        #     for _ in range(n):
        #         node = q.popleft()
        #         l.append(node.left)
        #         if node.left:
        #             q.append(node.left)
        #         l.append(node.right)
        #         if node.right:
        #             q.append(node.right)
        #     lenL = len(l)
        #     if lenL % 2 != 0:
        #         return False
        #     for i in range(0, lenL //2):
        #         nodeA = l[i]
        #         nodeB = l[lenL - i - 1]
        #         if not nodeA and not nodeB:
        #             continue
        #         if not nodeA or not nodeB or nodeA.val != nodeB.val:
        #             return False
        # return True