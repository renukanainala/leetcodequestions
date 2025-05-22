class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=[]
        ans=[-1]*len(nums)
        for i in range(2*n-1,-1,-1):
            while s and s[-1]<=nums[i%n]:
                s.pop()
            if i<n:
                ans[i]=s[-1] if s else -1
            s.append(nums[i%n])
        return ans