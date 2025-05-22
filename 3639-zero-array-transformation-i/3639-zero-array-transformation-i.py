class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        d=[0]*(n+1)
        for l,r in queries:
            d[l]+=1
            d[r+1]-=1
        p=[0]*(n)
        p[0]=d[0]
        for i in range(1,len(nums)):
            p[i]=p[i-1]+d[i]
        for i in range(len(nums)):
            if p[i]<nums[i]:
                return False
        return True