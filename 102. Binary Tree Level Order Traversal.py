from typing import Optional
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)
        result.append([root.val])
        while(q):
            n = len(q)  
            l = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    l.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    l.append(node.right.val)
                    q.append(node.right)
            if l:
                result.append(l)
        return result
                    
        
s = Solution()
node = TreeNode(3, TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
output = s.levelOrder(node)
print(output)