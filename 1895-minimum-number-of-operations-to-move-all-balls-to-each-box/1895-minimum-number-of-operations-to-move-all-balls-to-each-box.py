class Solution:
    def minOperations(self, b: str) -> List[int]:
        n=len(b)
        ans=[]
        for i in range(n):
            s=0
            for j in range(0,n):
                if b[j]=='1':
                   # print("bnm")
                    s+=abs(j-i)
            ans.append(s)
        return ans