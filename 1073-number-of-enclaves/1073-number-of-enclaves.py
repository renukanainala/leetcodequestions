class Solution:
    def numEnclaves(self, g: List[List[int]]) -> int:
        c=0
        row=len(g)
        col=len(g[0])
        s=set()
        vr=[0,-1,0,1]
        vc=[-1,0,1,0]
        self.l=0
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            s.add((i,j))
            while q:
                r,c=q.popleft()
                self.l-=1
                for k in range(4):
                    r1,c1=r+vr[k],c+vc[k]
                    if 0<=r1<row and 0<=c1<col and g[r1][c1]==1 and (r1,c1) not in s:
                        q.append((r1,c1))
                        
                        s.add((r1,c1))
                
        for i in range(row):
            for j in range(col):
                if g[i][j]==1:
                    self.l+=1
        for i in range(col):
            if g[0][i]==1 and (0,i) not in s:
                bfs(0,i)
            if g[row-1][i]==1 and (row-1,i) not in s:
                bfs(row-1,i)
        for i in range(row):
            if g[i][0]==1 and (i,0) not in s:
                bfs(i,0)
            if g[i][col-1]==1 and (i,col-1) not in s:
                bfs(i,col-1)
        return self.l
        
