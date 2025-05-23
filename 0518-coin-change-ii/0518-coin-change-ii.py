class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        def  find(ind,amount,dp):
            if ind==0:
                if amount%coins[ind]==0:
                    return 1
                else:
                    return 0
            if dp[ind][amount]!=-1:
                return dp[ind][amount]
            nottake=find(ind-1,amount,dp)
            take=0
            if coins[ind]<=amount:
                take=find(ind,amount-coins[ind],dp)
            dp[ind][amount]=take+nottake
            return dp[ind][amount]
        dp=[[-1]*(amount+1) for  i in range(n)]
        return find(len(coins)-1,amount,dp)