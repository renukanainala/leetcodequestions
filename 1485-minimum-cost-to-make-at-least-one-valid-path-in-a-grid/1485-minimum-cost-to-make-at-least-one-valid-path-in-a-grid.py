import heapq
class Solution:
    def minCost(self, g: List[List[int]]) -> int:
        s=set()
        c=0
        n=len(g[0])
        m=len(g)
        h=[]
        heapq.heappush(h,(0,0,0)) #cost,x,y coordinate
        d={1:[0,1],2:[0,-1],3:[1,0],4:[-1,0]}
        while h:
            c,x,y=heapq.heappop(h)
            if x==m-1 and y==n-1:
                return c
            if (x,y) in s:
                continue
            s.add((x,y))
            for k,v in d.items():
                dr=x+v[0]
                dc=y+v[1]
                if 0<=dr<m and 0<=dc<n and (dr,dc) not in s:
                    if g[x][y]==k:
                        heapq.heappush(h,(c,dr,dc))
                    else:
                        heapq.heappush(h,(c+1,dr,dc))
        return 0