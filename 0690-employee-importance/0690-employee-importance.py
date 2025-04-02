"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, e: List['Employee'], id: int) -> int:
        h={}
        for e1 in e:
            h[e1.id]=e1.importance
        h1={}
        for e1 in e:
            h1[e1.id]=e1.subordinates
        c=0
        q=deque()
        q.append(id)
        while q:
            n=q.popleft()
            c+=h[n]
            for j in h1[n]:
                q.append(j)
        return c
