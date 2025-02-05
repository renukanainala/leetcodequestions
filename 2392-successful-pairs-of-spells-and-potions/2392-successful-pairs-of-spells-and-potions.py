class Solution:
    def successfulPairs(self, s: List[int], p: List[int], ss: int) -> List[int]:
        p.sort()
        r=[]
        for i in s:
            l=0;h=len(p)-1
            idx=len(p)
            while l<=h:
                m=(l+h)//2
                if i*p[m]>=ss:
                    idx=m
                    h=m-1
                else:
                    l=m+1
            r.append(len(p)-idx)
        return r
