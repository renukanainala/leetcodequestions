class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)-1
        pos=n
        for i in range(n-1,-1,-1):
            if nums[i]+i>=pos:
                pos=i
        return pos==0