class Solution:
    def numEquivDominoPairs(self, a: List[List[int]]) -> int:
        h={}
        c=0
        for i,j in a:
            k=(min(i,j),max(i,j))
            if k in h:
                c+=h[k]
                h[k]+=1
            else:
                h[k]=1
        return c