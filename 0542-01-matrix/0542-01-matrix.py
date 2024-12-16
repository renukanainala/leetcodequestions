class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat);m=len(mat[0])
        q=deque()
        v=[[0]*m for i in range(n)]
        d=[[0]*m for i in range(n)] #resultmatrix
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    v[i][j]=1
                    q.append((i,j,0))
        dr=[-1,0,1,0];dc=[0,1,0,-1]
        while q:
            r,c,t=q.popleft()
            d[r][c]=t
            for i in range(4):
                nrow=r+dr[i]
                ncol=c+dc[i]
                if 0<=nrow<n and 0<=ncol<m and v[nrow][ncol]==0:
                    q.append((nrow,ncol,t+1))
                    v[nrow][ncol]=1
        return d
                    
            
            