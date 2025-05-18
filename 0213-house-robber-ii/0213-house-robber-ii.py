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
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        t1=[]
        t2=[]
        for i in range(len(nums)):
            if i!=0:
                t1.append(nums[i])
            if i!=len(nums)-1:
                t2.append(nums[i])
        dp1=[-1]*len(t1)
        dp2=[-1]*len(t2)
        q1=robber(len(t1)-1,t1,dp1)
        q2=robber(len(t2)-1,t2,dp2)
        return max(q1,q2)
