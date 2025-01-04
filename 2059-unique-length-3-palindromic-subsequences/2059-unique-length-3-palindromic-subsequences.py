class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        h={}
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]]=[i,i]
            else:
                h[s[i]][1]=i
        ans=0
        for u,v in h.values():
            if u!=v:
                s1=set()
                for j in range(u+1,v):
                    s1.add(s[j])
                ans+=len(s1)
        return ans