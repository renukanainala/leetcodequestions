class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        if n==1:
            if '0' not in nums:
                return '0'
        if n==2:
            if '00' not in nums:
                return '00'
        p=2**(n-1)
        p1=2**n
        for i in range(p,p1):
            s=bin(i)[2:]
            print(s)
            if s not in nums:
                return s
        return -1