class Solution:
    from collections import defaultdict
    import re
    def mostCommonWord(self, str1: str, banned: List[str]) -> str:
        s=set()
        for i in banned:
            s.add(i.lower())
        #str1=str1.lower().replace(',',' ').split(' ')
        str1 = re.findall(r'\w+', str1.lower())
        l=0
        h=defaultdict(int)
        w2=''
        for w in str1:
            w1=w.lower()
            if w1 not in s:
                h[w1]+=1
                if h[w1]>l:
                    l=h[w1]
                    w2=w1
        return w2


            
