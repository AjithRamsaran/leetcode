#time taken solve: 30 mins
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, minimum, maximum):
            if not node:
                return True
            if node.val <= minimum or node.val >= maximum:
                return False
            return check(node.left, minimum ,node.val) and check(node.right,node.val,maximum)
        return check(root, float("-inf"), float("inf"))
        # preorder = []
        # def preorderTraverse(node):
        #     if not node:
        #         return None
        #     preorderTraverse(node.left)
        #     preorder.append(node.val)
        #     preorderTraverse(node.right)
        # preorderTraverse(root)
        # print(preorder)
        # for i in range(len(preorder) - 1):
        #     if preorder[i] >=  preorder[i+1]:
        #         return False
        # return True