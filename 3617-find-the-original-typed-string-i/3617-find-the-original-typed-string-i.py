class Solution:
    def possibleStringCount(self, s: str) -> int:
        c=1
        e=s[0]
       
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
        return c
                

