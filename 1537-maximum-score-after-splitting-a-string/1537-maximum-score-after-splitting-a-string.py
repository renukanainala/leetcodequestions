class Solution:
    def maxScore(self, s: str) -> int:
        ans=0
        for i in range(1,len(s)):
            c1=s[:i].count('0')
            c2=s[i:].count('1')
            if ans<c1+c2:
                ans=c1+c2
        return ans