class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def bitcount(x):
          r=0
          while x:
             x=x&(x-1)
             r+=1
          return r
        b=bitcount(num2)
        res=0
        for i in range(31,-1,-1):
            if b>0 and (num1&(1<<i)):
                b-=1
                res+=1<<i
        for i in range(32):
            if b>0 and not(num1&(1<<i)):
                b-=1
                res+=1<<i
        return res
        
