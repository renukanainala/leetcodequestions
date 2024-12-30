class Solution:
    def insert(self, s: List[List[int]], new: List[int]) -> List[List[int]]:
        i=0
        ans=[]
        n=len(s)
        while i<n and new[0]>s[i][1]:
            ans.append(s[i])
            i+=1
        while i<n and new[1]>=s[i][0]:
            new[0]=min(new[0],s[i][0])
            new[1]=max(new[1],s[i][1])
            #print(new)
            i+=1
        ans.append(new)
        while i<n:
            ans.append(s[i])
            i+=1
        return ans
