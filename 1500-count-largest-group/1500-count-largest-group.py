class Solution:
    from collections import defaultdict
    def countLargestGroup(self, n: int) -> int:
        h=defaultdict(list)
        l=0
        for i in range(1,n+1):
            s=[int(j) for j in str(i)]
            h[sum(s)].append(i)
            l=max(l,len(h[sum(s)]))
        c=0
        for j in h.values():
            if len(j)==l:
                c+=1
        return c
             
