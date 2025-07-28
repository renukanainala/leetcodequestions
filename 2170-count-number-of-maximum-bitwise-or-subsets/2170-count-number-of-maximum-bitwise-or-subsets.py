class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int: 
        def find(i,s,nums,j):
            if i<0:
                return s==j    
            l=find(i-1,nums[i]|s,nums,j)
            h=find(i-1,s,nums,j)
            return l+h       
        maxi=0
        for i in nums: 
            maxi=maxi|i
        s=0
        
        return find(len(nums)-1,s,nums,maxi)
        