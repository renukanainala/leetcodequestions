class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        p=[0]*len(a)
        f=[0]*(len(a)+1)
        c=0
        for i in range(len(a)):
            f[a[i]]+=1
            if f[a[i]]==2:
                c+=1
            f[b[i]]+=1
            if f[b[i]]==2:
                c+=1
            p[i]=c
        return p

