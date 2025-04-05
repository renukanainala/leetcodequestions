class Solution:
    import heapq
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        nr=[0,-1,0,1]
        nc=[-1,0,1,0]
        h=[]
        cal=0 if grid[0][0]==0 else 1
        heapq.heappush(h,(cal,0,0)) # caloriex,coordinates(x,y)
        s=set()
        s.add((0,0))
        while h:
            d,r,c=heapq.heappop(h)
            if r==len(grid)-1 and c== len(grid[0])-1:
                print(d)
                if d<health:
                    return True
            for i in range(4):
                r1=r+nr[i]
                c1=c+nc[i] 
                if 0<=r1<len(grid) and 0<=c1<len(grid[0]) and (r1,c1) not in s:
                    heapq.heappush(h,(d+1 if grid[r1][c1]==1 else d ,r1,c1))
                    s.add((r1,c1))
        return False

        