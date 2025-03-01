class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s=[];ind=0
        for i in range(len(pushed)):
            s.append(pushed[i])
            while s and s[-1]==popped[ind]:
                s.pop()
                ind+=1
            #s.append(pushed[i])
        
        return len(s)==0