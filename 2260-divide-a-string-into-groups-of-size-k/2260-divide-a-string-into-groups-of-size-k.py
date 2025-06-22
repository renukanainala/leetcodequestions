class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans=[]
        n=len(s)
        res=""
        i=0
        while i<n:
            res+=s[i]
            i+=1
            if len(res)==k:
                ans.append(res)
                res=""
        if res:
            while len(res)!=k:
                res+=fill
            ans.append(res)
        return ans
            