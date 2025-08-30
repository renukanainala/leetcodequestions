class Solution:
    def toGoatLatin(self, s: str) -> str:
        vo='aeiouAEIOU'
        s=s.split()
        ans=[]
        for i,w in enumerate(s):
            if w[0] in vo:
                nw=w+'ma'
            else:
                nw=w[1:]+w[0]+'ma'
            nw+='a'*(i+1)
            ans.append(nw)
            
        return " ".join(ans)
