#time taken to solve: 20 mins
# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
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
