class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        k=0
        s=0
        for i in range(n):
            k+=gain[i]
            s=max(s,k)
        return s
