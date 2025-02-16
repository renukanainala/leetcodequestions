class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        t=sorted(nums)
        l=[]
        h={}
        n=len(nums)-1
        for i in range(len(t)):
            if t[i] not in h:
                h[t[i]]=i
        for i in range(len(nums)):
            l.append(h[nums[i]])
        return l