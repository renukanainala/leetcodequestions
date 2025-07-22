class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        rs=0
        l=0
        r=0
        rs1=float('-inf')
        while r<len(nums):
            while nums[r] in s:
                s.remove(nums[l])
                rs-=nums[l]
                l+=1
            s.add(nums[r])
            rs+=nums[r]
            if r-l+1==len(s):
                rs1=max(rs1,rs)
            r+=1
        return rs1