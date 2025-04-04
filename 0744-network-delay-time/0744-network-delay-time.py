class Solution:
    from collections import defaultdict
    import heapq
    def networkDelayTime(self, times: List[List[int]], no: int, k: int) -> int:
        s=set()
        h=[]
        adj=defaultdict(list)
        heapq.heappush(h,(0,k))
        for u,v,w in times:
            adj[u].append((v,w))
        dmax=float('-inf')
        while h:
            d,n=heapq.heappop(h)
            if n not in s:
                s.add(n)
                dmax=max(dmax,d)
                print(dmax)
            if len(s)==no:
                return dmax
            for v,w in adj[n]:
                if  v not in s:
                    heapq.heappush(h,(d+w,v))
        return -1

                
            
