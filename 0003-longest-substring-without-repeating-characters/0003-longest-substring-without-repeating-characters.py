class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l=0;r=0;d=set();s1=0
        while r<len(s):
            while s[r] in d :
                d.remove(s[l])
                l+=1
            d.add(s[r])
            if len(d)==r-l+1:
                s1=max(s1,r-l+1)
            r+=1
        return s1
