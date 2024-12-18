class Solution:
    def canFinish(self, V: int, p: List[List[int]]) -> bool:
        adj={i:[] for i in range(V)}
        v1=[0]*V
        for u,v in p :
            adj[v].append(u)
            v1[u]+=1
             # got adjacency directed atrix..
        q=deque()
        for i in range(V):
            if v1[i]==0:
                q.append(i)
        c=0
        while q:
            n=q.popleft()
            c+=1
            for j in adj[n]:
                v1[j]-=1
                if v1[j]==0:
                    q.append(j)
        return c==V
        
        