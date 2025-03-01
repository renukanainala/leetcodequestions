class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        print(nums)
        ind=-1;n=len(nums)
        for i in range(n):
            if nums[i]==0:
                ind=i
                break
        for j in range(ind+1,n):
            if nums[j]!=0:
                nums[ind],nums[j]=nums[j],nums[ind]
                ind+=1
        return nums

