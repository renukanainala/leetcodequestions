class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        #[[1,2,3],[0,2],[0,1,3],[0,2]] # 0 row 0 node neughbours..
        row=len(g)
        color=[-1]*row
        def bfs(i):
            q=deque()
            q.append(i)
            color[i]=1
            while q:
                node=q.popleft()
                for j in g[node]:
                    if color[j]==-1:
                        color[j]=1-color[node]
                        q.append(j)
                    elif color[j]!=color[node]:
                        continue
                    elif color[j]==color[node]:
                        return False
            return True
        for i in range(row):
            if color[i]==-1:
                if not bfs(i):
                    return False
        return True