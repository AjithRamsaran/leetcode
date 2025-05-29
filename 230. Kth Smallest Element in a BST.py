from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthElement = -1
        def inorder(node):
            nonlocal kthElement, k
            if not node:
                return node
            if k == 0:
                return kthElement
            left = inorder(node.left)
            # if left:
            #     return left
            if k > 0:
                kthElement = node.val
                k -= 1
            right = inorder(node.right)
            # if right:
            #     return right
        inorder(root)
        return kthElement