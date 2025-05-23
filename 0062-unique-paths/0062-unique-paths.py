class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def find(i,j,dp):
            if i==0  and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            left=find(i-1,j,dp)
            up=find(i,j-1,dp)
            dp[i][j]= left+up
            return dp[i][j]
        dp=[[-1]*n for i in range(m)]
        return find(m-1,n-1,dp)
        return dp[m-1][n-1]
        