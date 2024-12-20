class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1=s[:len(s)//2]
        s2=s[len(s)//2:]
        a='aeiouAEIOU';c=0;c2=0
        for i in range(len(s)//2):
            if s1[i] in a:
                c+=1
            if s2[i] in a:
                c2+=1
        return True if c==c2 else False