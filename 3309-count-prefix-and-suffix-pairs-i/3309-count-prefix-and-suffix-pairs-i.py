class Solution:
    def countPrefixSuffixPairs(self, w: List[str]) -> int:
        n=len(w)
        c=0
        for i in range(n):
            n1=len(w[i])
            for j in range(i+1,n):
                if w[j][:n1]==w[i] and w[j][-n1:]==w[i]:
                    c+=1
        return c