#time taken to solve: 30 mins (read solution and then wrote the code)
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def buildAdjacencyList(n, edgesList):
            adjList = [[] for _ in range(n)]

            for c1, c2 in edgesList:
                adjList[c2].append(c1)
            return adjList

        adjList = buildAdjacencyList(numCourses, prerequisites)
        state = [0] * numCourses
        
        def hasCycle(v):
            if state[v] == 1:
                return False
            
            if state[v] == -1:
                return True

            state[v] = -1

            for i in adjList[v]:
                if hasCycle(i):
                    return True
            state[v] = 1
            return False
        
        for v in range(numCourses):
            if hasCycle(v):
                return False
        return True