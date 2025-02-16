class Solution:
    def countElements(self, nums: List[int]) -> int:
        ma=max(nums)
        mi=min(nums)
        c=0
        for i in nums:
            if i<ma and i>mi:
                c+=1
        return c