class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        s=set()
        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def cc(i):
            q=deque()
          #  c=0# total no of connected componenrs
            q.append(i)
            c1=0
            s.add(i)
            n1=0
            while q:
                n=q.popleft()
                #c+=1 # no of connected components
                n1+=1 # no of nodes
                #print(n,c1)
                for i in adj[n]:
                    c1+=1
                    if i not in s:
                        s.add(i)
                        q.append(i)
                      #  l=[]
           # print(n1,c1)
            return c1//2==(n1*(n1-1))//2
        c=0
        for i in range(n):
            if i not in s:
                 c+=cc(i)
        return c