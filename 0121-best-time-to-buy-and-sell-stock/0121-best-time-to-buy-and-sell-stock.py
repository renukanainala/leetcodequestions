class Solution:
    def maxProfit(self, p: List[int]) -> int:
        '''
        k=min(prices)
        s=prices.index(k)
        f=[]
        for j in range(s,len(prices)):
            f.append(prices[j])
        l=max(f)
        return l-k
        '''
        d=p[0] #to buy
        profit=0
        for i in range(1,len(p)):
            d=min(d,p[i]) #tobuy
            profit=(max(profit,p[i]-d))
        return profit