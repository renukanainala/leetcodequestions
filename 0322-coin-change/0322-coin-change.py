class Solution:
    def coinChange(self, ar: List[int], t: int) -> int:
        '''def find(ind,t,dp):
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
            return dp[ind][t]'''
        n=len(ar)
        dp=[[-1]*(t+1) for j in range(len(ar))]
        for i in range(t+1):
            if i%ar[0]==0:
                dp[0][i]=i//ar[0]
            else:
                dp[0][i]=float('inf')
        for i in range(n):
            dp[i][0]=0
        for i in range(1,len(ar)):
            for j in range(1,t+1):
                nt=0+dp[i-1][j]
                ta=float('inf')
                if ar[i]<=j:
                    ta=1+dp[i][j-ar[i]] 
                dp[i][j]=min(ta,nt)
        return -1 if dp[n-1][t]==float('inf') else dp[n-1][t]