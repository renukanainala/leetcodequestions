class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        t=(n*(n+1))//2
        ds=0
        for i in range(1,n+1):
            if i%m==0:
                ds+=i
        return   t-2*ds 

