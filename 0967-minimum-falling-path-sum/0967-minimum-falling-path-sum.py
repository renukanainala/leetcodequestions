class Solution:
    def minFallingPathSum(self, a: List[List[int]]) -> int:
        n=len(a)
        d=[['s']*n for i in range(n)]
        for i in range(n):
            d[0][i]=a[0][i]
        for i in range(1,n):
            for j in range(n):
                up=d[i-1][j] if i>=0 else float('inf')
                ld=d[i-1][j-1] if (i>=0 and j>0) else float('inf')
                rd=d[i-1][j+1] if (i>0 and j>=0 and j<n-1) else float('inf')
                d[i][j]=a[i][j]+min(up,min(ld,rd))
        return min(d[n-1])

