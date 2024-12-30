class Solution:
    def merge(self, i: List[List[int]]) -> List[List[int]]:
        i.sort()
        l=i[0]
        ans=[]
        for j in i[1:]:
            if j[0]<=l[1]:
                l[1]=max(l[1],j[1])
            else:
                ans.append(l)
                l=j
        ans.append(l)
        return ans
