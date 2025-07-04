class Solution:
    def floodFill(self, g: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(g)
        m=len(g[0])
        s=set()
        nr=[0,-1,0,1]
        nc=[-1,0,1,0]
        def bfs(i,j):
            q=collections.deque()
            q.append((i,j))
            s.add((i,j))
            e=g[i][j]
            g[i][j]=color
            while q:
                r,c=q.popleft()
                for i in range(4):
                    r1,c1=nr[i]+r,nc[i]+c
                    if 0<=r1<n and 0<=c1<m and (r1,c1) not in s and g[r1][c1]==e:
                        g[r1][c1]=color
                        q.append((r1,c1))
                        s.add((r1,c1))

        if g[sr][sc]==color:
            return g
        bfs(sr,sc)
        return g
        
