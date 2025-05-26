class Solution:
    def coinChange(self, ar: List[int], amount: int) -> int:
        def find(ind,t,dp):
            if t==0:
                return 0
            if ind==0:
                if t%ar[ind]==0:
                    return t//ar[ind]
                else:
                    return float('inf')
            if dp[ind][t]!=-1:
                return dp[ind][t]
            nt=0+find(ind-1,t,dp)
            ta=float('inf')
            if ar[ind]<=t:
                ta=1+find(ind,t-ar[ind],dp)
            dp[ind][t]=min(ta,nt)
            return dp[ind][t]
        dp=[[-1]*(amount+1) for j in range(len(ar))]
        res=find(len(ar)-1,amount,dp) 
        if res==float('inf') :
            return -1 
        return res   