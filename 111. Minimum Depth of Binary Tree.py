from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)
        # res = 0

        # if left != 0 and right != 0:
        #     res = min(left, right)
        # elif left == 0:
        #     res = right
        # else:
        #     res = left
        # return 1 + res

        if not root:
            return 0
        c = 0
        que = deque([root])
        while que:
            l = len(que)
            
            for _ in range(l):
                node = que.popleft()
                if not node.left and not node.right:
                    c +=1 
                    return c
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            c += 1 