class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        s=set()
        n=len(g)#no of row
        m=len(g[0]) #len of cols
        def rec(i,j):
            if i<0 or i>=n or j<0 or j>=m or g[i][j]==0:
                return 1
            if (i,j) in s:
                return 0
            if (i,j) not in s:
                s.add((i,j))
            return rec(i-1,j)+rec(i+1,j)+rec(i,j-1) +rec(i,j+1)
        for i in range(n):
            for j in range(m):
                if g[i][j]==1:
                    return rec(i,j)

        