class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        c=0
        l=0
        for i in range(1,len(nums)-1):
            if (nums[i]>nums[i+1] and nums[i]>nums[l]) or  (nums[i]<nums[i+1]   and nums[i]<nums[l]):
                c+=1
                l=i
        return c 
                
                
                