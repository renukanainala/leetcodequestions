class Solution:
    def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
        '''def count(i,j,dp):
            if i==0 and j==0 and a[i][j]==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if a[i][j]==1:
                return 0
            up=count(i-1,j,dp)
            left=count(i,j-1,dp)
            dp[i][j]= up+left
            return dp[i][j]
        dp=[[-1]*len(a[0]) for i in range(len(a))]
        return count(len(a)-1,len(a[0])-1,dp0)'''
        n=len(a)
        m=len(a[0]) 
        dp=[[0]*m for i in range(n)]
        if a[0][0]==0:
            dp[0][0]=1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if a[i][j]==1 :
                    dp[i][j]=0
                else:
                    up=dp[i-1][j] if i>0 else 0
                    left=dp[i][j-1] if j>0 else 0
                    dp[i][j]=up+left
        return dp[n-1][m-1]