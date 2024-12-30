class Solution:
    def eraseOverlapIntervals(self, s: List[List[int]]) -> int:
        s.sort(key=lambda x:x[1])
        limit=s[0][1];c=1
        for j in range(1,len(s)):
            if s[j][0]>=limit:
                c+=1
                limit=s[j][1]
        return len(s)-c