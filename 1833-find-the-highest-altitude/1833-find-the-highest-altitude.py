class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        p=[0]*(n+1)
        s=0
        for i in range(1,n+1):
            p[i]=gain[i-1]+p[i-1]
            s=max(s,p[i])
        return s
