class Solution:
    def makeFancyString(self, s: str) -> str:
        prev=[]
        c=0
        res=""
        for i in s:
            if not prev or prev[0]!=i:
                prev=[i,1]
            else:
                prev[1]+=1
            if prev[1]<3:
                res+=i
        return res


