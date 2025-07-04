class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx]<0:
                continue
            nums[idx]*=-1
        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
        return ans