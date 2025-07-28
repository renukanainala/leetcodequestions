class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int: 
        def find(i,s,nums,j,dp):
            if i<0:
                return s==j  
            if dp[i][s]!=-1 :
                return dp[i][s]
            l=find(i-1,nums[i]|s,nums,j,dp)
            h=find(i-1,s,nums,j,dp)
            dp[i][s]= l+h    
            return  dp[i][s]  
        maxi=0
        for i in nums: 
            maxi=maxi|i
        s=0
        dp=[[-1] * (maxi+1) for i in range(len(nums)) ]
        return find(len(nums)-1,s,nums,maxi,dp)
        