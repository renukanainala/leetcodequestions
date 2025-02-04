class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        n=len(a)
        if n==1:
            return 0
        if a[0]>a[1]:
            return 0
        if a[n-1]>a[n-2]:
            return n-1
        l=1;h=n-2
        while l<=h:
            m=(l+h)//2
            if a[m]>a[m-1] and a[m]>a[m+1]:
                return m
            elif a[m]>a[m-1]:
                l=m+1
            else:
                h=m-1
        