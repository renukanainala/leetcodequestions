class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        def check(s,i,b):
            c=0
            for j in range(i+1):
                if b[j] in s:
                    c+=1
            return c
        s=set()
        ans=[]
        for i in range(len(a)):
            s.add(a[i])
            ans.append(check(s,i,b))
        return ans