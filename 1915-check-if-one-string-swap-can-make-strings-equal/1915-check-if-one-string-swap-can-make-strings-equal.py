class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        p=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                p.append(i)
        if len(p)==0:
            return True
        if len(p)==2:
            x,y=p
            if s1[x]==s2[y] and s2[x]==s1[y]:
                return True
        return False