class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        '''n=len(t)
        
        dp=[[float('inf')]*len(t[i]) for i in range(n)]
        for i in range(n):
            for j in range(len(t[i])):
                if i==0 and j==0:
                    dp[i][j]=t[i][j]
                    continue
                else:
                    up=dp[i-1][j] if i>0 else 0
                    diag=dp[i-1][j-1] if (i>0 and j>0) else 0
                    dp[i][j]=t[i][j]  +min(up,diag)
        return min(dp[n-1])
        
        def path(i,j,d):
            if i==n-1:
                return t[i][j]
            if d[i][j]==-1:
                return d[i][j]
            d1=t[i][j]+path(i+1,j,d)
            diag=t[i][j]+path(i+1,j+1,d)
            d[i][j]=min(d1,diag)
            return d[i][j]
        d=[[float('inf')]*n for i in range(n)]
        return path(0,0,d)'''
        n=len(t)
        d=[[0]*n for i in range(n)]
        for i in range(n):
            d[n-1][i]=t[n-1][i]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                d1=d[i+1][j]
                diag=d[i+1][j+1]
                d[i][j]=t[i][j]+min(d1,diag)
        return d[0][0]

        