class Solution:
    import heapq
    def shortestPathBinaryMatrix(self, g: List[List[int]]) -> int:
        n=len(g)
        m=len(g[0])
        h=[]
        if g[0][0]==1:
            return -1
        heapq.heappush(h,[1,0,0])
        s=set()
        s.add((0,0))
        nr=[0,-1,-1,-1,0,1,1,1]
        nc=[-1,-1,0,1,1,1,0,-1]
        while h:
            d,r,c=heapq.heappop(h)
            if r==n-1 and c==n-1:
                return d
            for i in range(8):
                nrow=r+nr[i]
                ncol=c+nc[i]
                if 0<=nrow<n and 0<=ncol<m  and g[nrow][ncol]==0 and (nrow,ncol) not in s:
                    heapq.heappush(h,[d+1,nrow,ncol])
                    s.add((nrow,ncol))
        return -1


