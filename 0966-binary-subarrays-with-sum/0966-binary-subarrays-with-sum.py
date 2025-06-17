class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d=defaultdict(int)
        d[0]=1;c=0;c1=0
        for i in nums:
            c+=i
            if c-goal in d:
                c1+=d[c-goal]
            d[c]+=1
        return c1