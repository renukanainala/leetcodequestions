class Solution:
    def findOrder(self, V: int, p: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(V)}
        inde=[0]*V
        for u,v in p:
            adj[v].append(u)
            inde[u]+=1
        q=deque()
        for i in range(V):
            if inde[i]==0:
                q.append(i)
        t=[]
        while q:
            n=q.popleft()
            t.append(n)
            for j in adj[n]:
                inde[j]-=1
                if inde[j]==0:
                    q.append(j)
        return t if len(t)==V else []