class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d={i :[] for i in range(1,n+1)}
        t=[0]*n
        et=[0]*n
        for i,j in trust:
            d[i].append(j)
            t[j-1]+=1
            et[i-1]+=1
        print(t,et)
        for i in range(n):
            if t[i]==n-1 and et[i]==0:
                return i+1
        return -1
