class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        i=1;d=1
        ci=1;cd=1
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                i+=1
                ci=max(ci,i)
                d=1
            elif nums[j]<nums[j+1]:
                d+=1
                cd=max(cd,d)
                i=1
            else:
                d=1
                i=1
        return max(ci,cd)
