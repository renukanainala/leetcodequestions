class Solution:
    def calculateScore(self, ins: List[str], v: List[int]) -> int:
        n=len(v)
        vis=[0]*(n)
        s=0
        i=0
        while 0<=i<n:
            if vis[i]:
                break
            vis[i]=1
            if ins[i]=="add":
                s+=v[i]
                i+=1
            elif ins[i]=="jump" :
                i=i+v[i]
        return s

