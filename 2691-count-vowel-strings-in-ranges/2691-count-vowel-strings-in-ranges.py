class Solution:
    def vowelStrings(self, words: List[str], q: List[List[int]]) -> List[int]:
        v='aeiou'
        p=[0]*len(words)
        if words[0][0] in v and words[0][-1] in v:
            p[0]=1
        for i in range(1,len(words)):
            if words[i][0] in v and words[i][-1] in v:
                p[i]=p[i-1]+1
            else:
                p[i]=p[i-1]+0
        
        ans=[]
        for u,v in q:
            if u!=0:
                ans.append(p[v]-p[u-1])
            else:
                ans.append(p[v])
        return ans