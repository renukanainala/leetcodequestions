class Solution:
    import heapq
    def minPathSum(self, grid: List[List[int]]) -> int:
        nr=[1,0]
        nc=[0,1]
        h=[]
       # d=[[float('inf')]*]
        #heapify(h)
        m=len(grid[0]) #colums
        n=len(grid)#rows
        d=[[float('inf')]*m for i in range(n)]
        d[0][0]=grid[0][0]
        heapq.heappush(h,(grid[0][0],0,0)) #dist,x,y
        while len(h)>0:
            d1,r,c=heapq.heappop(h)
            if r==n-1 and c==m-1:
                return d1
            for i in range(2):
                r1=r+nr[i]
                c1=c+nc[i]
                if 0<=r1<n and 0<=c1<m:
                    if d[r1][c1]>d1+grid[r1][c1]:
                        d[r1][c1]=d1+grid[r1][c1]
                        heapq.heappush(h,(d1+grid[r1][c1],r1,c1))
        return -1