class Solution:
    def vowelStrings(self, words: List[str], q: List[List[int]]) -> List[int]:
        v='aeiou'
        p=[0]*len(words)
        s=0
        for i in range(0,len(words)):
            cur=words[i]
            if cur[0] in v and cur[-1] in v:
               s+=1
            p[i]=s
        ans=[]
        for u,v in q: 
            if u!=0:
                ans.append(p[v]-p[u-1])
            else:
                ans.append(p[v])
        return ans