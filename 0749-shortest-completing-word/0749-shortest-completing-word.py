class Solution:
    from collections import defaultdict
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        h=defaultdict(int)
        for i in licensePlate:
            if i.isalpha():
                h[i.lower()]+=1
        words.sort(key=len)
        print(words)
        
        for j in words:
            s1=Counter(j)
            c=0
            for i in h:
                if h[i]<=s1[i]:
                    c+=1
            if c==len(h):
                return j

