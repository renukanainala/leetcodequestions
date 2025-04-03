class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=[0]*26;r=0
        for i in range(len(chars)):
            c[ord(chars[i])-ord('a')]+=1
        for j in words:
            c1=[0]*26
            g=True
            for k in range(len(j)):
                c1[ord(j[k])-ord('a')]+=1
                if c1[ord(j[k])-ord('a')]>c[ord(j[k])-ord('a')]:
                    g=False
                    break
            if g:
                r+=len(j)
        return r