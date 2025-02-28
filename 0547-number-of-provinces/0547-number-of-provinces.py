class Solution:
    def findCircleNum(self, g: List[List[int]]) -> int:
        s=set()
        n=len(g)
        def bfs(i):
            s.add(i)
            for k in range(n):
                if g[i][k]==1 and k not in s:
                    bfs(k)
        c=0

        for i in range(n):
            if not i in s:
                c+=1
                bfs(i)
        return c