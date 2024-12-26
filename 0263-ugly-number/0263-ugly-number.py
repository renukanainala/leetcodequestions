class Solution:
    def isUgly(self, n1: int) -> bool:
        if n1 ==0:
            return False
        while n1%2==0 :
            n1//=2
        while n1%3==0:
            n1//=3
        while n1%5==0:
            n1//=5
        return n1==1      