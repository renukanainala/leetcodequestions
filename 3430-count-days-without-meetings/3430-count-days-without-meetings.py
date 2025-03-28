class Solution:
    def countDays(self, days: int, m: List[List[int]]) -> int:
        # do merge subintervals
        m.sort()
        s,e=m[0]
        a=[]
        for i in m[1:]:
            st,end=i
            if st<=e:
                e=max(e,end)
            else:
                a.append([s,e])
                s,e=st,end
        a.append([s,e])
        c=0
        for s,e in a:
            c+=e-s+1
        return days-c
        