class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        p=nums.pop(0)
        nums.sort()
        return p+nums[0]+nums[1]
