class Solution:
    def minimumLength(self, s: str) -> int:
        l=Counter(s)
        c=0
        for i in l.values():
            if i%2:
                c+=1
            else:
                c+=2
        return c
