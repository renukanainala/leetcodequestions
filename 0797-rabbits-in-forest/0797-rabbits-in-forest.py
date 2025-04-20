class Solution:
    from collections import defaultdict
    def numRabbits(self, answers: List[int]) -> int:
        s=defaultdict(int)
        c=0
        for i in answers:
            s[i]+=1
            if s[i]==i+1:
                c+=s[i]
                s[i]=0
        for i in s.keys():
            if s[i]!=0:
                c+=i+1
        return c
            

        