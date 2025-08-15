class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        k=math.log(n,4)
        return k.is_integer()
