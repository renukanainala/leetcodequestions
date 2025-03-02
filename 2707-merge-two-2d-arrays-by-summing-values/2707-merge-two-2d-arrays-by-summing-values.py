class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i=0;j=0
        l=[]
        while i<len(nums1) and j<len(nums2):
            id1,e1=nums1[i]
            id2,e2=nums2[j]
            if id1<id2:
                l.append([id1,e1])
                i+=1
            elif id2<id1:
                l.append([id2,e2])
                j+=1
            else:
                l.append([id1,e1+e2])
                i+=1
                j+=1
        while i<len(nums1):
            id1,e1=nums1[i]
            l.append([id1,e1])
            i+=1
        while j<len(nums2):
            id2,e2=nums2[j]
            l.append([id2,e2])
            j+=1
        return l        

