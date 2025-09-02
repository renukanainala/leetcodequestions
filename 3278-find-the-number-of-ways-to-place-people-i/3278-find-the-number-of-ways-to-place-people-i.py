class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n=len(points)
        c=0
        for i in range(n):
            ax,ay=points[i]
            for j in range(n):
                if i==j:
                    continue
                bx,by=points[j]
                if bx>=ax and by<=ay:
                    f=True
                    for k in range(n):
                        if k==i or k==j:
                            continue
                        cx,cy=points[k]                    
                        if (ax<=cx<=bx and by<=cy<=ay):
                            f=False
                            break
                    if f:
                        c+=1
        return c
                    