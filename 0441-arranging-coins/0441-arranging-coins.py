class Solution:
    def arrangeCoins(self, n: int) -> int:
        c=0
        i=1
        j=1
        while j<=n:
            c+=1
            i+=1
            j+=i
        return c