class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def find(ind,nums,target):
            if target==0:
                return True
            if ind ==0:
                return (nums[0]==target)
            nottake=find(ind-1,nums,target)
            take=False
            if (nums[ind]<=target):
                take=find(ind-1,nums,target-nums[ind])
            return take or nottake
        s=sum(nums)
        if s%2:
            return False
        return find(len(nums)-1,nums,s//2)