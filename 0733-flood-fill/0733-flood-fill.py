class Solution:
    def floodFill(self, g: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(g)
        m=len(g[0])
        s=set()
        nr=[0,-1,0,1]
        nc=[-1,0,1,0]
        def bfs(i,j,e,color):
            '''q=collections.deque()
            q.append((i,j))
            s.add((i,j))
            e=g[i][j]
            g[i][j]=color
            val=g[i][j]
            while q:
                r,c=q.popleft()
                for i in range(4):
                    r1,c1=nr[i]+r,nc[i]+c
                    if 0<=r1<n and 0<=c1<m and (r1,c1) not in s and g[r1][c1]==e:
                        g[r1][c1]=val
                        q.append((r1,c1))
                        s.add((r1,c1))'''
            if i<0 or i>=n or j<0 or j>=m or (i,j) in s or g[i][j]!=e:
                return
            s.add((i,j))
            g[i][j]=color
            bfs(i,j-1,e,color)
            bfs(i,j+1,e,color)
            bfs(i-1,j,e,color)
            bfs(i+1,j,e,color)

        if g[sr][sc]==color:
            return g
        e=g[sr][sc]
        bfs(sr,sc,e,color)
        return g
        
