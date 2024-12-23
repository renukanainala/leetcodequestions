"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        d={} #maping old to new
        e=Node(node.val)
        d[node]=e
        q=deque()
        q.append(node) #old node 
        while q:
            cur=q.popleft()
            for nei in cur.neighbors: #using old node cr
                if nei not in d:
                    d[nei]=Node(nei.val)
                    q.append(nei)
                d[cur].neighbors.append(d[nei])
        return d[node]
                
