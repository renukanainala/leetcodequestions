class Solution:
    def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
        def count(i,j,dp):
            if i==0 and j==0 and a[i][j]==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            if i<0 or j<0:
                return 0
            if a[i][j]==1:
                return 0
            up=count(i-1,j,dp)
            left=count(i,j-1,dp)
            return dp[i][j]= up+left
        dp=[[-1]*len(a[0]) for i in range(len(a))]
        return count(len(a)-1,len(a[0])-1,dp)