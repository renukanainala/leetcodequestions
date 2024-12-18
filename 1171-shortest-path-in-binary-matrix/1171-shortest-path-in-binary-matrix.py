class Solution:
    def shortestPathBinaryMatrix(self, g: List[List[int]]) -> int:
        if g[0][0]==1:
            return -1
        q=deque([(0,0,1)])
        s=set()
        s.add((0,0))
        vr=[0,-1,-1,-1,0,1,1,1]
        vc=[-1,-1,0,1,1,1,0,-1]
        row=len(g)
        col=len(g[0])
        while q:
            r,c,l=q.popleft()
            if r==row-1 and c==col-1:
                return l
            for i in range(8):
                r1,c1=r+vr[i],c+vc[i]
                if 0<=r1<row and 0<=c1<col and g[r1][c1]==0 and (r1,c1) not in s:
                    s.add((r1,c1))
                    q.append((r1,c1,l+1))
        return -1