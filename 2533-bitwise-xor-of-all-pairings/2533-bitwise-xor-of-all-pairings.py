class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x1=0
        l1=len(nums1)
        l2=len(nums2)
        x2=0
        if l2%2!=0:
            for i in nums1:
                x1=x1^i
        if l1%2!=0:
            for j in nums2:
                x2=x2^j
        return x1^x2