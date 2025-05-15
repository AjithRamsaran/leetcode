from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        def maxPath(node):
            nonlocal maxSum
            if not node:
                return -1001
            leftSum = maxPath(node.left)
            rightSum = maxPath(node.right)            
            maxVal = max(node.val,leftSum + node.val,rightSum + node.val)
            maxSum = max(maxVal, maxSum, leftSum + rightSum + node.val)
            return maxVal
        maxPath(root)
        return maxSum