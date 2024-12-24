class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i=0
        j=0
        ans=[]
        while i<len(s):
            j=i
            c=0
            while j<len(s) and s[j]==s[i]:
                c+=1
                j+=1
            if c>=3:
                ans.append([i,j-1])
            i=j
        return ans