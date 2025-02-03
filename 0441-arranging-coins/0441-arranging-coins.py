class Solution:
    def arrangeCoins(self, n: int) -> int:
        r=1
        c=0
        while n>=r:
            r+=1
            c+=1
            n=n-r
        return c