class FindSumPairs:
    from collections import defaultdict,Counter
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2
        self.h=Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        old=self.nums2[index]
        new=old+val
        self.h[old]-=1
        if self.h[old]==0:
            del self.h[old]
        self.nums2[index]=new
        self.h[new]+=1

    def count(self, tot: int) -> int:
        c=0
        for i in self.nums1:
            if (tot-i) in self.h:
                c+=self.h[tot-i]
        return c
            


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)