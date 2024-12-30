class Solution:
    def findMin(self, a: List[int]) -> int:
        ans=float('inf')
        l=0;h=len(a)-1
        while l<=h:
            m=l+(h-l)//2
            if a[l]<=a[m]<=a[h]:
                ans=min(ans,a[l])
                break
            elif a[l]<=a[m]:
                ans=min(ans,a[l])
                l=m+1
            else:
                ans=min(ans,a[m])
                h=m-1
        return ans