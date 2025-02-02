class Solution:
    def check(self, s: List[int]) -> bool:
        k=[];j=-1
        for i in range(len(s)-1):
            if s[i]>s[i+1]:
                j=i
                k=s[i+1:]
                break
        #print(k,s[:j+1])
        if j!=-1:
            l1=k+s[:j+1]
            return l1==sorted(s)
       # print(k,s[i+1:])
        return True