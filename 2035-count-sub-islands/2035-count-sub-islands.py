class Solution:
    def countSubIslands(self, g: List[List[int]], g1: List[List[int]]) -> int:    
        q=deque()
        vr=[0,1,0,-1]
        vc=[-1,0,1,0]
        s=set()
        def bfs(i,j):
            island=True
            q.append((i,j))
            s.add((i,j))
           # g1[i][j]=0
            while q:
                r,c=q.popleft()
                if g[r][c]==0:
                    island=False
                for k in range(4):
                    r1,c1=r+vr[k],c+vc[k]
                    if 0<=r1<row and 0<=c1<col and g1[r1][c1]==1 and (r1,c1) not in s:
                        q.append((r1,c1))
                        s.add((r1,c1))
            return island
        row=len(g);col=len(g[0]);iland=0
        for i in range(row):
            for j in range(col):
                if g1[i][j]==1 and(i,j) not in s:
                    if bfs(i,j):
                        iland+=1
        return iland