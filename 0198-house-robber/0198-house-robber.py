class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(i,nums,dp):
            if dp[i]!=-1:
                return dp[i]
            if i==0:
                return nums[0]
            if i<0:
                return 0
            pick=nums[i]+robber(i-2,nums,dp)
            notpick=robber(i-1,nums,dp)
            dp[i]= max(pick,notpick)
            return dp[i]
        dp=[-1]*len(nums)
        return robber(len(nums)-1,nums,dp)
