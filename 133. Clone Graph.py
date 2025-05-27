#time taken to solve: 20 mins
# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #dfs approach
        clones = {}
        def clone(node):
            if node.val in clones:
                return clones[node.val]
            clones[node.val] = Node(node.val, [])
            for nbr in node.neighbors:
                clones[node.val].neighbors.append(clone(nbr))
            return clones[node.val]
        return clone(node) if node else node
        
        #bfs approach
        if not node:
            return node
        q = deque()
        q.append(node)
        clones = {node.val : Node(node.val, [])}
        while q:
           cur = q.popleft()
           curClone = clones[cur.val]
           for nbr in cur.neighbors:
                if nbr.val not in clones:
                    clones[nbr.val] = Node(nbr.val, [])
                    q.append(nbr)
                curClone.neighbors.append(clones[nbr.val])
        return clones[node.val]
    
    
