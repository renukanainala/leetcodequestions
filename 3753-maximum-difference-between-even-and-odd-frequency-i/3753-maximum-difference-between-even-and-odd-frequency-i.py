class Solution:
    def maxDifference(self, s: str) -> int:
        c=[0]*26
        emin=float('inf')
        omax=float('-inf')
        for i in s:
            c[ord(i)-ord('a')]+=1
        for j in c:
            if j>0:
                if j%2==0:
                    if j<emin:
                        emin=j
                else:
                    if j>omax:
                        omax=j
        if omax==float('-inf') or emin==float('inf'):
            return -1
        return omax-emin
