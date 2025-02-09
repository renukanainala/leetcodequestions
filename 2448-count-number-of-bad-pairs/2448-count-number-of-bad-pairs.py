class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        g=0
        n=len(nums)
        t=(n*(n-1))//2
        h=defaultdict(int)
        for i in range(len(nums)):
            g+=h[i-nums[i]]
            h[i-nums[i]]+=1
        return t-g
        