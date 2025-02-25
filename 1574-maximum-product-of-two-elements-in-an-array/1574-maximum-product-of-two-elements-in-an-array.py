class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1=float('-inf')
        m2=float('-inf')
        for i in range(len(nums)):
            if nums[i]>=m1:
                m2=m1
                m1=nums[i]
            elif nums[i]<m1 and nums[i]>m2:
                m2=nums[i]
        return (m1-1)*(m2-1)