#time taken to solve: 25 mins
from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBBTree(node, height):
            if not node: 
                return [True, height]
            leftHeight = 0 
            leftBalanced,leftHeight = isBBTree(node.left, height + 1)
            rightHeight = 0
            rightBalanced,rightHeight = isBBTree(node.right, height + 1)
            return [leftBalanced and rightBalanced and abs(leftHeight - rightHeight) < 2, max(leftHeight, rightHeight)]
        return isBBTree(root, 1)[0]