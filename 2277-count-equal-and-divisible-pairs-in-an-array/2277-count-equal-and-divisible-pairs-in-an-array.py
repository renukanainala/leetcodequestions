class Solution:
    def countPairs(self, nums: List[int], k1: int) -> int:
        from collections import defaultdict
        h=defaultdict(list)
        for i in range(len(nums)):
            h[nums[i]].append(i)
        c=0
        for j in h.values():
            for i in range(len(j)):
                for k in range(i+1,len(j)):
                    if (j[i]*j[k])%k1==0:
                        c+=1
        return c
