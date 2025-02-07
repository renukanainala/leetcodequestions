class Solution:
    def queryResults(self, l: int, q: List[List[int]]) -> List[int]:
        color=defaultdict(int)
        f=defaultdict(int)
        r=[0]*len(q)
        for k in range(len(q)):
            i=q[k][0]
            j=q[k][1]
            if i in color:
                e=color[i]
                f[e]-=1
                if f[e]==0:
                    del f[e]
            color[i]=j
            f[j]+=1
            #print(f)
            r[k]=len(f)
        return r