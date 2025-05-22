class Solution:
    def minFallingPathSum(self, a: List[List[int]]) -> int:
        def path(i,j,dp):
            if j<0 or j>=n or i>=n:
                return float('inf')
            if i==0:
                return a[0][j]
            if dp[i][j]!='s':
                return dp[i][j]
            up=path(i-1,j,dp)
            ld=path(i-1,j-1,dp)
            rd=path(i-1,j+1,dp)
            dp[i][j]=a[i][j]+min(up,ld,rd)
            return dp[i][j]
        mini=float('inf')
        n=len(a)
        dp=[['s']*n for i in range(n)]
        for i in range(n):
            mini=min(mini,path(n-1,i,dp))
        return mini

