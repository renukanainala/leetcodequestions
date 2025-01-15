class NumArray:

    def __init__(self, nums: List[int]):
       # self.s=nums  
        self.p=[0]*len(nums)
        self.p[0]=nums[0]
        for i in range(1,len(nums)):
            self.p[i]=self.p[i-1]+nums[i]

    def sumRange(self, l: int, r: int) -> int:
        return self.p[r] if l==0 else self.p[r]-self.p[l-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)