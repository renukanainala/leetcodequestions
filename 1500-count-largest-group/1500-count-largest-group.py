class Solution:
    from collections import defaultdict
    def countLargestGroup(self, n: int) -> int:
        h=defaultdict(int)
        l=0
        for i in range(1,n+1):
            s=[int(j) for j in str(i)]
            h[sum(s)]=h[sum(s)]+1
            l=max(l,h[sum(s)])
        c=0
        for j in h.values():
            if j==l:
                c+=1
        return c
             
