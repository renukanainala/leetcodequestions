class Solution:
    from collections import deque
    def maxDistance(self, g: List[List[int]]) -> int:
        n=len(g)
        m=len(g[0])
        s=set()
        nr=[0,-1,0,1]
        nc=[-1,0,1,0]
        q=deque()
        c2=0
        for i in range(n):
            for j in range(m):
                if g[i][j]==1: # land
                    q.append((i,j,0))
                    s.add((i,j))
                if g[i][j]==0:
                    c2+=1
        if not q or not c2:
            return -1

        dmax=-1
        while q :
            r,c,d=q.popleft()
            dmax=max(dmax,d)
            for i in range(4):
                r1=r+nr[i]
                c1=c+nc[i]
                if 0<=r1<n and 0<=c1<m and g[r1][c1]==0 and (r1,c1) not in s:
                    q.append((r1,c1,d+1))
                    s.add((r1,c1))
                    
        return dmax

