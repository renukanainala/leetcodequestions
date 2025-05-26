class Solution:
    def maxProfit(self, ar: List[int]) -> int:
        buy=ar[0]
        pro=float('-inf')
        for i in range(1,len(ar)):
            if ar[i]<buy:
                buy=ar[i]
            else:
                pro=max(pro,ar[i]-buy)
        return 0 if pro==float('-inf') else pro

