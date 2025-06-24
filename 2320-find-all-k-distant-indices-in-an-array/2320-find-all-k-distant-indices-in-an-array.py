class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ind=[]
        n=len(nums)
        for i in range(len(nums)):
            for j in range(n):
                if nums[j]==key and abs(i-j)<=k:
                    ind.append(i)
                    break
        return ind