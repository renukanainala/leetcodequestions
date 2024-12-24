class Solution:
    def maxProfit(self, p: List[int]) -> int:
        d=0
        c=0
        for i in range(1,len(p)):
           # c=p[i]-p[i-1] #should be negeative
            if p[i]>p[i-1]:
                d+=p[i]-p[i-1]
        return d