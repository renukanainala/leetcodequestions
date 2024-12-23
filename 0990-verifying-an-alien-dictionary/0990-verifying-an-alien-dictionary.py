class Solution:
    def isAlienSorted(self, w: List[str], order: str) -> bool:
        d={c:i for i,c in enumerate(order)}
        for i in range(len(w)-1):
            s1=w[i]
            s2=w[i+1]
            for j in range(len(s1)):
                if j==len(s2):
                    return False
                elif s1[j]!=s2[j]:
                    if d[s1[j]]>d[s2[j]]:
                        return False
                    break
        return True
                