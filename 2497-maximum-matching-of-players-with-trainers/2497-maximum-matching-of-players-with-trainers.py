class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        p.sort()
        t.sort()
        i=len(p)-1
        c=0
        j=len(t)-1
        while (j>=0 and i>=0):
            if t[j]>=p[i]:
                c+=1
                j-=1
            i-=1
        return c