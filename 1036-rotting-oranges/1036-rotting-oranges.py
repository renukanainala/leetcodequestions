class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        n=len(g)
        m=len(g[0])
        c2=0;q=collections.deque()
        for i in range(n):
            for j in range(m):
                if g[i][j]==1:
                    c2+=1#count total fresh fruits
                if g[i][j]==2:
                    q.append((i,j))
        t=0
        nr=[0,-1,0,1]
        nc=[-1,0,1,0]
        while q and c2>0:
            s=len(q)
            for k in range(s):
                r,c=q.popleft()
                for i in range(4):
                    r1,c1=nr[i]+r,nc[i]+c
                    if 0<=r1<n and 0<=c1<m and g[r1][c1]==1:
                        q.append((r1,c1))
                        g[r1][c1]=2
                        c2-=1
            t+=1
        return t if c2==0 else -1