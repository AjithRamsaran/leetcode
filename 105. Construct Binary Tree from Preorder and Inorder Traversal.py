#time taken solve: 45 mins
# Definition for a binary tree node.
from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        ind = inorder.index(preorder[0]) #if preorder[0] in inorder else -1
        # if ind == -1:
        #     return None
        head = TreeNode(preorder[0])
        preorder.pop(0)
        head.left = self.buildTree(preorder, inorder[:ind])
        head.right = self.buildTree(preorder, inorder[ind+1:])
        return head