class Solution:
    import heapq
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h=[]
        ans=[]
        heapq.heappush(h,(nums1[0]+nums2[0],0,0))
        s=set()
        s.add((0,0))
        while h and k>0:
            s1,i,j=heapq.heappop(h)
            ans.append([nums1[i],nums2[j]])
            if i+1<len(nums1) and (i+1,j) not in s:
                heapq.heappush(h,(nums1[i+1]+nums2[j],i+1,j))
                s.add((i+1,j))
            if j+1<len(nums2) and (i,j+1) not in s:
                heapq.heappush(h,(nums1[i]+nums2[j+1],i,j+1))
                s.add((i,j+1))
            k-=1
        return ans


            