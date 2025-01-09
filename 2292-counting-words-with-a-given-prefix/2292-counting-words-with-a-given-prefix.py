class Solution:
    def prefixCount(self, w: List[str], pref: str) -> int:
        n=len(pref)
        c=0
        for i in range(len(w)):
            if w[i][:n]==pref:
                c+=1
        return c