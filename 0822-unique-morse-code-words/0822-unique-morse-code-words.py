class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        h={}
        c=0
        for i in range(97,123):
            h[chr(i)]=s[c]
            c+=1
        s=set()
        for i in words:
            t=""
            for j in i:
                t+=h[j]
            s.add(t)
        return len(s)