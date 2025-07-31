class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
            ans=[]
            for i in range(len(nums)):
                val=    abs(nums[i])-1
                if nums[val]<0:
                        ans.append(     abs(nums[i]))
                else:
                    nums[val]*=-1
            return   ans

                    
                 