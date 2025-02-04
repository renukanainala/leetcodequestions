class Solution:
    def maxAscendingSum(self, a: List[int]) -> int:
        c=a[0];s=a[0]
        for i in range(1,len(a)):
            if a[i]>a[i-1]:
                s+=a[i]
            else:
                c=max(c,s)
                s=a[i]
        c=max(c,s)
        return c