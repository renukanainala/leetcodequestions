class Solution:
    def check(self, s: List[int]) -> bool:
        c=0
        for i in range(len(s)):
            if s[i]>s[(i+1)%len(s)]:
                c+=1
        if c<=1:
            return True
        return False